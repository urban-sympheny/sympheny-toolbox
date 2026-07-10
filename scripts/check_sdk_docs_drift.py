"""Detect drift between the SDK's public surface and the generated SDK docs.

Introspects the async client (``AsyncSympheny``), reads the REST call embedded in
each method docstring (`` `METHOD /path` ``), and checks that:

- ``docs/_data/sdk_map.yml`` (operationId → ``resource.method``) is up to date;
- every public method has its anchor (``#method-{resource}-{method}``) in
  ``docs/sdk/reference/{resource}.md``, and no anchor points at a method that no
  longer exists.

Run after any SDK surface change (CI runs it on every PR):

    uv run python scripts/check_sdk_docs_drift.py

Pass ``--write-map`` to (re)generate ``docs/_data/sdk_map.yml``. The reference
pages themselves are agent-written — on failure, follow
``.agents/skills/docs/SKILL.md`` → task ``regen-sdk-reference``.
"""

from __future__ import annotations

import inspect
import json
import re
import sys
from pathlib import Path

from sympheny_toolbox import AsyncSympheny


REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC = REPO_ROOT / "specs" / "sympheny_openapi.json"
SDK_MAP = REPO_ROOT / "docs" / "_data" / "sdk_map.yml"
REFERENCE_DIR = REPO_ROOT / "docs" / "sdk" / "reference"

# client.unofficial wraps endpoints outside the committed spec: it gets a
# reference page and anchors, but no operationId mapping.
UNMAPPED_RESOURCES = {"unofficial"}

_REST_CALL = re.compile(r"``(GET|POST|PUT|PATCH|DELETE) (/[^`\s]+)``")
_ANCHOR = re.compile(r"\{ #(method-[A-Za-z0-9_-]+) \}")

MAP_HEADER = (
    "# GENERATED — do not edit by hand. operationId → SDK method (client.<resource>.<method>).\n"
    "# Regenerate: uv run python scripts/check_sdk_docs_drift.py --write-map\n"
)


def normalize_path(path: str) -> str:
    """Collapse ``{param}`` placeholders so path-parameter names don't matter."""
    return re.sub(r"\{[^}]*\}", "{}", path)


def public_resources() -> dict[str, list[str]]:
    """``{resource attribute: [public method names]}`` of the async client."""
    client = AsyncSympheny("drift-check", "drift-check")
    resources: dict[str, list[str]] = {}
    for name, obj in vars(client).items():
        if name.startswith("_"):
            continue
        methods = [m for m, member in inspect.getmembers(type(obj), inspect.iscoroutinefunction) if not m.startswith("_")]
        if methods:
            resources[name] = methods
    return resources


def build_sdk_map(resources: dict[str, list[str]], errors: list[str]) -> dict[str, str]:
    """Derive ``{operationId: resource.method}`` from docstrings and the spec."""
    spec = json.loads(SPEC.read_text())
    operation_ids: dict[tuple[str, str], str] = {}
    for path, item in spec["paths"].items():
        for method, operation in item.items():
            if isinstance(operation, dict) and "operationId" in operation:
                operation_ids[(method.upper(), normalize_path(path))] = operation["operationId"]

    client = AsyncSympheny("drift-check", "drift-check")
    mapping: dict[str, str] = {}
    for resource, methods in resources.items():
        if resource in UNMAPPED_RESOURCES:
            continue
        for method_name in methods:
            qualified = f"{resource}.{method_name}"
            docstring = inspect.getdoc(getattr(type(vars(client)[resource]), method_name)) or ""
            calls = _REST_CALL.findall(docstring)
            if len(calls) != 1:
                errors.append(f"client.{qualified}: expected exactly one ``METHOD /path`` in the docstring, found {len(calls)}")
                continue
            http_method, path = calls[0]
            operation_id = operation_ids.get((http_method, normalize_path(path)))
            if operation_id is None:
                errors.append(f"client.{qualified}: `{http_method} {path}` has no matching operation in specs/sympheny_openapi.json")
                continue
            if operation_id in mapping:
                errors.append(f"operationId {operation_id} claimed by both client.{mapping[operation_id]} and client.{qualified}")
                continue
            mapping[operation_id] = qualified
    return mapping


def render_map(mapping: dict[str, str]) -> str:
    return MAP_HEADER + "".join(f"{operation_id}: {qualified}\n" for operation_id, qualified in sorted(mapping.items()))


def check_anchors(resources: dict[str, list[str]], errors: list[str]) -> None:
    """Every method needs its anchor in its page; every anchor needs its method."""
    expected = {f"method-{resource}-{method}": resource for resource, methods in resources.items() for method in methods}
    found: set[str] = set()
    for page in sorted(REFERENCE_DIR.glob("*.md")) if REFERENCE_DIR.exists() else []:
        for anchor in _ANCHOR.findall(page.read_text()):
            if anchor not in expected:
                errors.append(f"docs/sdk/reference/{page.name}: anchor #{anchor} does not match any public client method")
            found.add(anchor)
    for anchor, resource in sorted(expected.items()):
        page = REFERENCE_DIR / f"{resource}.md"
        if not page.exists():
            errors.append(f"docs/sdk/reference/{resource}.md is missing (needed for client.{resource})")
        elif anchor not in found:
            errors.append(f"docs/sdk/reference/{resource}.md: missing anchor #{anchor}")


def main() -> None:
    write_map = "--write-map" in sys.argv[1:]
    errors: list[str] = []
    resources = public_resources()
    rendered = render_map(build_sdk_map(resources, errors))

    if write_map:
        if errors:
            print("\n".join(f"ERROR: {e}" for e in errors))
            sys.exit(1)
        SDK_MAP.parent.mkdir(parents=True, exist_ok=True)
        SDK_MAP.write_text(rendered)
        print(f"Wrote {SDK_MAP.relative_to(REPO_ROOT)}")
        return

    if not SDK_MAP.exists() or SDK_MAP.read_text() != rendered:
        errors.append("docs/_data/sdk_map.yml is out of date (run: uv run python scripts/check_sdk_docs_drift.py --write-map)")
    check_anchors(resources, errors)

    if errors:
        print("SDK docs drift detected — regenerate per .agents/skills/docs/SKILL.md → task regen-sdk-reference:")
        print("\n".join(f"  {e}" for e in errors))
        sys.exit(1)
    unique_methods = sum(len(m) for m in resources.values())
    print(f"SDK docs are in sync ({len(resources)} resource groups, {unique_methods} methods)")


if __name__ == "__main__":
    main()
