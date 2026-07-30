"""Generate the REST API reference pages from the merged OpenAPI spec.

Renders ``specs/sympheny_openapi.json`` into one Markdown page per tag under
``docs/api/reference/`` — deterministic output, no network access. Rerun after
any spec change:

    uv run python scripts/generate_api_reference.py

Pass ``--check`` to verify the committed pages are up to date (used by CI).

SDK cross-links come from ``docs/_data/sdk_map.yml`` (flat ``operationId:
resource.method`` mapping, built in a later phase); missing entries are
tolerated and simply omit the link.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC = REPO_ROOT / "specs" / "sympheny_openapi.json"
OUTPUT_DIR = REPO_ROOT / "docs" / "api" / "reference"
SDK_MAP = REPO_ROOT / "docs" / "_data" / "sdk_map.yml"
# Verbatim spec copy served next to the beta Scalar explorer (docs/api/explorer.html).
# Emitted here so it can never drift from specs/sympheny_openapi.json; the --check
# below covers it. Drop with the explorer experiment if it isn't kept.
SERVED_SPEC = REPO_ROOT / "docs" / "api" / "openapi.json"

GENERATED_HEADER = (
    "<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.\n"
    "     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->\n"
)

# Tag → (output file stem, page title). Order defines nav/reading order:
# platform resources first, then account, then solver. A spec tag missing from
# this mapping is an error so new tags force a deliberate docs decision.
TAG_PAGES: dict[str, tuple[str, str]] = {
    "project-controller": ("projects", "Projects"),
    "analysis-controller": ("analyses", "Analyses"),
    "scenario-controller": ("scenarios", "Scenarios"),
    "stage-controller": ("stages", "Stages"),
    "hub-controller": ("hubs", "Hubs"),
    "energy-carrier-controller": ("energy-carriers", "Energy carriers"),
    "energy-demand-controller": ("energy-demands", "Energy demands"),
    "profile-controller": ("profiles", "Profiles"),
    "solar-on-site-resource-controller": ("solar-resources", "Solar resources"),
    "conversion-technology-controller": ("conversion-technologies", "Conversion technologies"),
    "storage-technology-controller": ("storage-technologies", "Storage technologies"),
    "technology-package-controller": ("technology-packages", "Technology packages"),
    "network-technology-controller": ("network-technologies", "Network technologies"),
    "network-link-controller": ("network-links", "Network links"),
    "intra-hub-network-link-controller": ("intra-hub-network-links", "Intra-hub network links"),
    "impex-controller": ("impex", "Imports and exports (impex)"),
    "Auth External": ("auth", "Auth"),
    "External Users": ("users", "Users"),
    "External Solver Jobs": ("solver-jobs", "Solver jobs"),
}

HTTP_METHODS = ("get", "post", "put", "patch", "delete")
_MAX_EXAMPLE_DEPTH = 8


def load_sdk_map() -> dict[str, str]:
    """Parse the flat ``operationId: resource.method`` mapping; empty if absent."""
    if not SDK_MAP.exists():
        return {}
    mapping: dict[str, str] = {}
    for line in SDK_MAP.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition(":")
        if value.strip():
            mapping[key.strip()] = value.strip().strip("\"'")
    return mapping


def resolve(spec: dict[str, Any], schema: dict[str, Any]) -> dict[str, Any]:
    """Follow a ``$ref`` (if any) to its schema definition."""
    while "$ref" in schema:
        name = schema["$ref"].rsplit("/", 1)[-1]
        schema = spec["components"]["schemas"][name]
    return schema


def ref_name(schema: dict[str, Any]) -> str | None:
    """The schema name a ``$ref`` (possibly wrapped in a nullable anyOf) points to."""
    if "$ref" in schema:
        return str(schema["$ref"].rsplit("/", 1)[-1])
    variants = [v for v in schema.get("anyOf", schema.get("oneOf", [])) if v.get("type") != "null"]
    if len(variants) == 1:
        return ref_name(variants[0])
    return None


def primary_type(schema: dict[str, Any]) -> str | None:
    """The non-null type of a schema, unwrapping 3.1-style ``type: [X, "null"]`` arrays."""
    stype = schema.get("type")
    if isinstance(stype, list):
        non_null = [t for t in stype if t != "null"]
        return non_null[0] if non_null else None
    return stype


def type_label(schema: dict[str, Any]) -> str:
    """Human-readable type string for a schema fragment."""
    if "$ref" in schema:
        return f"`{schema['$ref'].rsplit('/', 1)[-1]}`"
    for key in ("anyOf", "oneOf"):
        if key in schema:
            labels = [type_label(v) for v in schema[key] if v.get("type") != "null"]
            nullable = any(v.get("type") == "null" for v in schema[key])
            joined = " or ".join(dict.fromkeys(labels)) or "any"
            return f"{joined}, nullable" if nullable else joined
    stype = primary_type(schema)
    if isinstance(schema.get("type"), list) and "null" in schema["type"]:
        return f"{type_label({**schema, 'type': stype})}, nullable" if stype else "any"
    if stype == "array":
        return f"array of {type_label(schema.get('items', {}))}"
    if stype is None:
        return "any"
    if schema.get("format"):
        return f"{stype} ({schema['format']})"
    return str(stype)


def example_value(spec: dict[str, Any], schema: dict[str, Any], depth: int = 0) -> Any:
    """Synthesize a deterministic example value for a schema."""
    if depth > _MAX_EXAMPLE_DEPTH:
        return None
    schema = resolve(spec, schema)
    for key in ("example", "default"):
        if key in schema and schema[key] is not None:
            return schema[key]
    if "enum" in schema:
        return schema["enum"][0]
    for key in ("anyOf", "oneOf"):
        if key in schema:
            variants = [v for v in schema[key] if v.get("type") != "null"]
            return example_value(spec, variants[0], depth + 1) if variants else None
    stype = primary_type(schema)
    if stype == "object" or "properties" in schema:
        return {name: example_value(spec, prop, depth + 1) for name, prop in schema.get("properties", {}).items()}
    if stype == "array":
        return [example_value(spec, schema.get("items", {}), depth + 1)]
    if stype == "string":
        return _STRING_EXAMPLES.get(schema.get("format", ""), "string")
    return _SCALAR_EXAMPLES.get(stype or "")


_STRING_EXAMPLES: dict[str, str] = {
    "email": "user@example.com",
    "uuid": "00000000-0000-0000-0000-000000000000",
    "guid": "00000000-0000-0000-0000-000000000000",
    "date-time": "2026-01-01T00:00:00Z",
    "date": "2026-01-01",
    "binary": "<binary>",
}
_SCALAR_EXAMPLES: dict[str, Any] = {"integer": 0, "number": 0.0, "boolean": True}


def table_cell(text: str) -> str:
    """Make free text safe inside a Markdown table cell."""
    return " ".join(text.split()).replace("|", "\\|")


def describe(schema: dict[str, Any]) -> str:
    """Description column content for a schema fragment: prose plus constraints."""
    parts = []
    if schema.get("description"):
        parts.append(table_cell(schema["description"]).rstrip(".") + ".")
    enum = schema.get("enum")
    if enum:
        parts.append("One of: " + ", ".join(f"`{v}`" for v in enum) + ".")
    if schema.get("default") is not None:
        parts.append(f"Default: `{json.dumps(schema['default'])}`.")
    return " ".join(parts)


def humanize(operation_id: str) -> str:
    """Turn an operationId into a sentence-case heading."""
    words: list[str] = []
    current = ""
    for ch in operation_id:
        if ch in "_-":
            if current:
                words.append(current)
            current = ""
        elif ch.isupper() and current and not current[-1].isupper():
            words.append(current)
            current = ch
        else:
            current += ch
    if current:
        words.append(current)
    text = " ".join(w.lower() for w in words)
    return text[:1].upper() + text[1:]


def parameters_table(spec: dict[str, Any], parameters: list[dict[str, Any]]) -> list[str]:
    lines = ["**Parameters**", "", "| Name | In | Type | Required | Description |", "| --- | --- | --- | --- | --- |"]
    for param in parameters:
        schema = param.get("schema", {})
        desc_parts = [table_cell(param["description"])] if param.get("description") else []
        extra = describe(schema)
        if extra:
            desc_parts.append(extra)
        lines.append(
            f"| `{param['name']}` | {param['in']} | {type_label(schema)} | {'yes' if param.get('required') else 'no'} | {' '.join(desc_parts)} |"
        )
    return [*lines, ""]


def fields_table(spec: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """One-level field table for an object schema (refs resolved first)."""
    schema = resolve(spec, schema)
    properties = schema.get("properties", {})
    if not properties:
        return []
    required = set(schema.get("required", []))
    lines = ["| Field | Type | Required | Description |", "| --- | --- | --- | --- |"]
    for name, prop in properties.items():
        resolved = prop if "$ref" not in prop else resolve(spec, prop)
        lines.append(f"| `{name}` | {type_label(prop)} | {'yes' if name in required else 'no'} | {describe(resolved)} |")
    return [*lines, ""]


def curl_example(spec: dict[str, Any], method: str, path: str, operation: dict[str, Any], base_url: str) -> list[str]:
    query = "&".join(f"{p['name']}={{{p['name']}}}" for p in operation.get("parameters", []) if p["in"] == "query" and p.get("required"))
    url = f"{base_url}{path}" + (f"?{query}" if query else "")
    lines = [f'curl -X {method.upper()} "{url}"']
    if operation.get("security", [{"HTTPBearer": []}]) != []:
        lines.append('  -H "Authorization: Bearer $SYMPHENY_TOKEN"')
    body = operation.get("requestBody")
    if body:
        schema = next(iter(body["content"].values())).get("schema", {})
        payload = json.dumps(example_value(spec, schema), indent=2)
        lines.append('  -H "Content-Type: application/json"')
        lines.append(f"  -d '{payload}'")
    joined = " \\\n".join(lines)
    return ["**Example request**", "", "```bash", joined, "```", ""]


def operation_section(spec: dict[str, Any], method: str, path: str, operation: dict[str, Any], sdk_map: dict[str, str], base_url: str) -> list[str]:
    operation_id = operation["operationId"]
    title = operation.get("summary") or humanize(operation_id)
    lines = [f"## {title} {{ #operation-{operation_id} }}", "", "```", f"{method.upper()} {path}", "```", ""]

    requires_auth = operation.get("security", [{"HTTPBearer": []}]) != []
    auth_note = "Requires a [Bearer token](../authentication.md)." if requires_auth else "No authentication required."
    sdk_method = sdk_map.get(operation_id)
    if sdk_method:
        resource, _, name = sdk_method.rpartition(".")
        auth_note += f" SDK method: [`client.{sdk_method}()`](../../sdk/reference/{resource}.md#method-{resource}-{name})."
    lines += [auth_note, ""]

    if operation.get("description"):
        lines += [operation["description"].strip(), ""]

    if operation.get("parameters"):
        lines += parameters_table(spec, operation["parameters"])

    body = operation.get("requestBody")
    if body:
        schema = next(iter(body["content"].values())).get("schema", {})
        lines += [f"**Request body** ({type_label(schema)})", ""]
        resolved = resolve(spec, schema)
        # For array bodies, tabulate the fields of one item.
        lines += fields_table(spec, resolved.get("items", schema) if primary_type(resolved) == "array" else schema)

    lines += curl_example(spec, method, path, operation, base_url)

    lines += ["**Responses**", "", "| Status | Description | Schema |", "| --- | --- | --- |"]
    success_example: tuple[str, Any] | None = None
    for status, response in operation["responses"].items():
        content: dict[str, dict[str, Any]] = response.get("content", {})
        resp_schema: dict[str, Any] | None = next(iter(content.values())).get("schema") if content else None
        if resp_schema is None:
            label = "n/a"
        else:
            schema_name = ref_name(resp_schema)
            label = f"`{schema_name}`" if schema_name else type_label(resp_schema)
        lines.append(f"| {status} | {table_cell(response.get('description', ''))} | {label} |")
        if resp_schema and status.startswith("2") and success_example is None:
            success_example = (status, example_value(spec, resp_schema))
    lines.append("")
    if success_example:
        status, value = success_example
        lines += [f"**Example response** ({status})", "", "```json", json.dumps(value, indent=2), "```", ""]
    return lines


def generate_pages() -> dict[str, str]:
    """Render all reference pages; returns ``{filename: content}``."""
    spec = json.loads(SPEC.read_text())
    sdk_map = load_sdk_map()
    base_url = spec["servers"][0]["url"]

    by_tag: dict[str, list[tuple[str, str, dict[str, Any]]]] = {}
    for path, item in spec["paths"].items():
        for method in HTTP_METHODS:
            if method in item:
                operation = item[method]
                tag = operation["tags"][0]
                if tag not in TAG_PAGES:
                    msg = f"Spec tag {tag!r} has no entry in TAG_PAGES — add one (and a nav entry in zensical.toml)."
                    raise SystemExit(msg)
                by_tag.setdefault(tag, []).append((method, path, operation))

    unused = [tag for tag in TAG_PAGES if tag not in by_tag]
    if unused:
        msg = f"TAG_PAGES entries without spec operations: {unused} — remove them (and their nav entries)."
        raise SystemExit(msg)

    tag_descriptions = {t["name"]: t.get("description") for t in spec.get("tags", [])}
    pages: dict[str, str] = {}
    for tag, (stem, title) in TAG_PAGES.items():
        operations = sorted(by_tag[tag], key=lambda op: (op[1], HTTP_METHODS.index(op[0])))
        lines = [GENERATED_HEADER, f"# {title}", ""]
        if tag_descriptions.get(tag):
            lines += [str(tag_descriptions[tag]), ""]
        for method, path, operation in operations:
            lines += operation_section(spec, method, path, operation, sdk_map, base_url)
        pages[f"{stem}.md"] = "\n".join(lines).rstrip() + "\n"
    return pages


def main() -> None:
    check_only = "--check" in sys.argv[1:]
    pages = generate_pages()
    served_spec = SPEC.read_text()

    if check_only:
        stale = [name for name, content in pages.items() if not (OUTPUT_DIR / name).exists() or (OUTPUT_DIR / name).read_text() != content]
        stale += [f.name for f in OUTPUT_DIR.glob("*.md") if f.name not in pages] if OUTPUT_DIR.exists() else []
        if not SERVED_SPEC.exists() or SERVED_SPEC.read_text() != served_spec:
            stale.append(f"../{SERVED_SPEC.name}")
        if stale:
            print("Out-of-date generated files (run: uv run python scripts/generate_api_reference.py):")
            print("\n".join(f"  docs/api/reference/{name}" for name in sorted(stale)))
            sys.exit(1)
        print("docs/api/reference/ is up to date")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for existing in OUTPUT_DIR.glob("*.md"):
        if existing.name not in pages:
            existing.unlink()
    for name, content in pages.items():
        (OUTPUT_DIR / name).write_text(content)
    SERVED_SPEC.write_text(served_spec)
    print(f"Generated {len(pages)} pages into docs/api/reference/ (+ docs/api/{SERVED_SPEC.name})")


if __name__ == "__main__":
    main()
