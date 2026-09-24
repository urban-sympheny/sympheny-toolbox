#!/usr/bin/env python3
"""Merge the Sympheny backend OpenAPI schemas into a single OpenAPI 3.1 document.

Only the merged output, ``specs/sympheny_openapi.json``, is committed and public. The upstream exports
below are **internal Sympheny artifacts, git-ignored** (see ``specs/.gitignore``); a fresh clone will
not have them, so this script is a **maintainer-only** step for regenerating the public spec.

The nullability contract (agreed with the webapp backend team — webapp only)
--------------------------------------------------------------
In the upstream webapp export, a property listed in a schema's ``required`` must be **present and
non-null**; every other property **may be null**. The export marks nothing ``nullable``, so
``mark_non_required_nullable`` below applies the second half of the rule when producing the public
spec: every property absent from its schema's ``required`` gains ``"null"`` in its type. Required
properties keep their declared type, and a ``null`` returned for one of them is an API bug. The other
exports (api-services, backoffice, sense) are not under this contract and keep their declared types.

Refresh the webapp and api-services exports with ``scripts/fetch_openapi.py``; it saves
``specs/<source>_openapi_latest.json`` and prints the diff — review it, then copy it over
``specs/<source>_openapi.json`` and rerun this script. The backoffice and sense exports have no docs
endpoint yet and are maintained as local files. Since the 2026-08-06 export, every operation the SDK uses (including ``renameScenario`` and
``copyScenario``, which used to be patched in manually) is present upstream, so no manual additions
remain.

Which operations of each export are published is set in ``specs/openapi_filters.toml`` (committed):
include/exclude patterns per source. api-services is an allowlist — its section must declare
``include`` — so a new upstream endpoint is never published by accident.

Private source inputs (in specs/, git-ignored):
- webapp_openapi.json       (OpenAPI 3.0.1) : upgraded to 3.1, non-required fields marked nullable,
                                              paths prefixed with /sympheny-app
- api_services_openapi.json                 : upgraded to 3.1 if needed, paths prefixed with
                                              /api-services; optional while its allowlist is empty
- backoffice_openapi.json   (OpenAPI 3.1.0)
- sense_openapi.json        (OpenAPI 3.1.0)

Output (committed, public): specs/sympheny_openapi.json

Usage: python scripts/merge_openapi.py
"""

from __future__ import annotations

import fnmatch
import json
import sys
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from collections.abc import Callable


SPECS = Path(__file__).resolve().parent.parent / "specs"
OUTPUT = SPECS / "sympheny_openapi.json"
FILTERS = SPECS / "openapi_filters.toml"

# Internal Sympheny exports, git-ignored (see specs/.gitignore); only OUTPUT is committed/public.
PRIVATE_SOURCES = ("webapp_openapi.json", "api_services_openapi.json", "backoffice_openapi.json", "sense_openapi.json")

SERVER_URL = "https://eu-north-1-api.sympheny.com"
WEBAPP_PREFIX = "/sympheny-app"
API_SERVICES_PREFIX = "/api-services"

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

# sections of FILTERS; api-services is an allowlist and must declare `include`
FILTER_SOURCES = ("webapp", "api-services", "backoffice", "sense")


def load(name: str) -> dict[str, Any]:
    path = SPECS / name
    if not path.exists():
        raise SystemExit(
            f"{name} not found in specs/. The upstream OpenAPI exports ({', '.join(PRIVATE_SOURCES)}) are "
            "internal Sympheny artifacts and are not committed; obtain them and place them in specs/. "
            "Only the merged specs/sympheny_openapi.json is public — regenerating it is a maintainer-only step."
        )
    data: dict[str, Any] = json.loads(path.read_text())
    return data


# ---------------------------------------------------------------------------
# OpenAPI 3.0 -> 3.1 upgrade helpers (webapp)
# ---------------------------------------------------------------------------


def upgrade_schema_3_0_to_3_1(node: Any) -> None:
    """Recursively convert 3.0-style schema keywords to 3.1 in-place."""
    if isinstance(node, list):
        for item in node:
            upgrade_schema_3_0_to_3_1(item)
        return
    if not isinstance(node, dict):
        return

    # boolean exclusiveMinimum/Maximum (3.0) -> numeric (3.1)
    for bound, limit in (
        ("exclusiveMinimum", "minimum"),
        ("exclusiveMaximum", "maximum"),
    ):
        if isinstance(node.get(bound), bool):
            if node[bound] and limit in node:
                node[bound] = node.pop(limit)
            else:
                del node[bound]

    # nullable: true (3.0) -> type: [T, "null"] (3.1)
    if node.pop("nullable", False):
        add_null_type(node)

    for value in node.values():
        upgrade_schema_3_0_to_3_1(value)


def add_null_type(schema: dict[str, Any]) -> None:
    """Make a single schema accept null (OpenAPI 3.1 style), in-place."""
    if "$ref" in schema:
        ref = {"$ref": schema.pop("$ref")}
        schema["anyOf"] = [ref, {"type": "null"}]
        return
    for combinator in ("anyOf", "oneOf"):
        if combinator in schema:
            if not any(sub.get("type") == "null" for sub in schema[combinator]):
                schema[combinator].append({"type": "null"})
            return
    schema_type = schema.get("type")
    if isinstance(schema_type, str):
        if schema_type != "null":
            schema["type"] = [schema_type, "null"]
    elif isinstance(schema_type, list) and "null" not in schema_type:
        schema_type.append("null")
    if "enum" in schema and None not in schema["enum"]:
        schema["enum"].append(None)


def mark_non_required_nullable(node: Any) -> None:
    """In every object schema, make properties not listed in `required` nullable."""
    if isinstance(node, list):
        for item in node:
            mark_non_required_nullable(item)
        return
    if not isinstance(node, dict):
        return

    properties = node.get("properties")
    if isinstance(properties, dict):
        required = set(node.get("required", []))
        for name, prop_schema in properties.items():
            if name not in required and isinstance(prop_schema, dict):
                add_null_type(prop_schema)

    for value in node.values():
        mark_non_required_nullable(value)


# ---------------------------------------------------------------------------
# Filtering and pruning
# ---------------------------------------------------------------------------


def filter_paths(
    spec: dict[str, Any],
    keep_op: Callable[[str, str, dict[str, Any]], bool],
) -> None:
    """Keep only operations for which keep_op(path, method, operation) is true."""
    new_paths: dict[str, Any] = {}
    for path, path_item in spec["paths"].items():
        kept = {method: op for method, op in path_item.items() if method in HTTP_METHODS and keep_op(path, method, op)}
        if kept:
            # preserve path-level fields (parameters, summary, ...)
            extras = {k: v for k, v in path_item.items() if k not in HTTP_METHODS}
            new_paths[path] = {**extras, **kept}
    spec["paths"] = new_paths


def load_filters() -> dict[str, dict[str, list[str]]]:
    filters: dict[str, dict[str, list[str]]] = tomllib.loads(FILTERS.read_text())
    missing = [name for name in FILTER_SOURCES if name not in filters]
    if missing:
        raise SystemExit(f"{FILTERS.name}: missing section(s) {missing}")
    if "include" not in filters["api-services"]:
        raise SystemExit(f"{FILTERS.name}: [api-services] must declare `include` (allowlist)")
    return filters


def matches(pattern: str, path: str, method: str, op: dict[str, Any]) -> bool:
    """Whether a filter pattern (``tag:<name>``, ``op:<operationId>`` or ``METHOD /path`` glob) selects an operation."""
    if pattern.startswith("tag:"):
        return pattern.removeprefix("tag:") in op.get("tags", [])
    if pattern.startswith("op:"):
        return pattern.removeprefix("op:") == op.get("operationId")
    return fnmatch.fnmatchcase(f"{method.upper()} {path}", pattern)


def apply_filters(spec: dict[str, Any], rules: dict[str, list[str]], prefix: str, label: str) -> None:
    """Keep the operations selected by `rules`, matched against their public path (`prefix` + path)."""
    include, exclude = rules.get("include"), rules.get("exclude", [])
    used: set[str] = set()

    def keep(path: str, method: str, op: dict[str, Any]) -> bool:
        public = prefix + path
        included = [p for p in include if matches(p, public, method, op)] if include is not None else []
        excluded = [p for p in exclude if matches(p, public, method, op)]
        used.update(included, excluded)
        return (include is None or bool(included)) and not excluded

    filter_paths(spec, keep)
    for pattern in [*(include or []), *exclude]:
        if pattern not in used:
            print(f"warning: [{label}] filter pattern matched nothing: {pattern!r}", file=sys.stderr)


def collect_refs(node: Any, refs: set[str]) -> None:
    if isinstance(node, list):
        for item in node:
            collect_refs(item, refs)
    elif isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str):
            refs.add(ref)
        for value in node.values():
            collect_refs(value, refs)


def prune_components(spec: dict[str, Any]) -> None:
    """Drop component schemas not (transitively) referenced from paths."""
    schemas = spec.get("components", {}).get("schemas", {})
    reachable: set[str] = set()
    frontier: set[str] = set()
    collect_refs(spec["paths"], frontier)
    while frontier:
        names = {ref.rsplit("/", 1)[-1] for ref in frontier if ref.startswith("#/components/schemas/")}
        new = names - reachable
        reachable |= new
        frontier = set()
        for name in new:
            if name in schemas:
                collect_refs(schemas[name], frontier)
    spec["components"]["schemas"] = {name: schema for name, schema in schemas.items() if name in reachable}


def rename_schema(spec: dict[str, Any], old: str, new: str) -> None:
    schemas = spec["components"]["schemas"]
    schemas[new] = schemas.pop(old)

    old_ref = f"#/components/schemas/{old}"
    new_ref = f"#/components/schemas/{new}"

    def rewrite(node: Any) -> None:
        if isinstance(node, list):
            for item in node:
                rewrite(item)
        elif isinstance(node, dict):
            if node.get("$ref") == old_ref:
                node["$ref"] = new_ref
            for value in node.values():
                rewrite(value)

    rewrite(spec)


# ---------------------------------------------------------------------------
# Merge
# ---------------------------------------------------------------------------


def is_superset_schema(a: dict[str, Any], b: dict[str, Any]) -> bool:
    """True if object schema `a` equals `b` except for extra optional properties."""
    if a.get("required", []) != b.get("required", []):
        return False
    props_a, props_b = a.get("properties", {}), b.get("properties", {})
    if not set(props_a) >= set(props_b):
        return False
    if any(props_a[k] != props_b[k] for k in props_b):
        return False
    rest_a = {k: v for k, v in a.items() if k != "properties"}
    rest_b = {k: v for k, v in b.items() if k != "properties"}
    return rest_a == rest_b


def merge_schemas(target: dict[str, Any], source_spec: dict[str, Any], label: str) -> None:
    target_schemas = target["components"]["schemas"]
    for name in list(source_spec["components"]["schemas"]):
        schema = source_spec["components"]["schemas"][name]
        existing = target_schemas.get(name)
        if existing is None:
            target_schemas[name] = schema
        elif existing == schema:
            continue
        elif is_superset_schema(schema, existing):
            target_schemas[name] = schema  # keep richer variant
        elif is_superset_schema(existing, schema):
            continue
        else:
            new_name = f"{label}{name}"
            rename_schema(source_spec, name, new_name)
            target_schemas[new_name] = source_spec["components"]["schemas"][new_name]


def used_tags(spec: dict[str, Any]) -> set[str]:
    tags: set[str] = set()
    for path_item in spec["paths"].values():
        for method, op in path_item.items():
            if method in HTTP_METHODS:
                tags.update(op.get("tags", []))
    return tags


def set_default_security(spec: dict[str, Any], security: list[dict[str, list[str]]]) -> None:
    """Copy a document-level security requirement onto each operation lacking one."""
    for path_item in spec["paths"].values():
        for method, op in path_item.items():
            if method in HTTP_METHODS and "security" not in op:
                op["security"] = security


def sort_output(spec: dict[str, Any]) -> None:
    """Sort paths, and the methods within each (path-level fields first), so upstream export order
    never shows up as churn in the committed spec.

    Component schemas deliberately keep their merge order: datamodel-codegen numbers inline enums
    (``Version``, ``Version1``, ...) by encounter order, so sorting them renames public SDK models.
    """
    spec["paths"] = {path: dict(sorted(item.items(), key=lambda kv: (kv[0] in HTTP_METHODS, kv[0]))) for path, item in sorted(spec["paths"].items())}


def prepare_api_services(rules: dict[str, list[str]]) -> dict[str, Any]:
    """Load, upgrade (if 3.0), filter and prefix the api-services export — no nullability contract."""
    # nothing is published from api-services until its allowlist names something, so the export
    # is only required then
    if not rules["include"] and not (SPECS / "api_services_openapi.json").exists():
        return {"openapi": "3.1.0", "paths": {}, "components": {"schemas": {}}}
    spec = load("api_services_openapi.json")
    if str(spec.get("openapi", "")).startswith("3.0"):
        upgrade_schema_3_0_to_3_1(spec.get("components", {}))
        upgrade_schema_3_0_to_3_1(spec["paths"])
    set_default_security(spec, [{"HTTPBearer": []}])
    apply_filters(spec, rules, API_SERVICES_PREFIX, "api-services")
    spec.setdefault("components", {}).setdefault("schemas", {})
    prune_components(spec)
    spec["paths"] = {API_SERVICES_PREFIX + path: item for path, item in spec["paths"].items()}
    return spec


def main() -> int:
    filters = load_filters()
    webapp = load("webapp_openapi.json")
    backoffice = load("backoffice_openapi.json")
    sense = load("sense_openapi.json")
    api_services = prepare_api_services(filters["api-services"])

    # --- webapp: upgrade to 3.1, nullability, path prefix -------------------
    upgrade_schema_3_0_to_3_1(webapp["components"])
    upgrade_schema_3_0_to_3_1(webapp["paths"])
    mark_non_required_nullable(webapp["components"])
    mark_non_required_nullable(webapp["paths"])
    set_default_security(webapp, [{"HTTPBearer": []}])
    apply_filters(webapp, filters["webapp"], WEBAPP_PREFIX, "webapp")
    prune_components(webapp)
    webapp["paths"] = {WEBAPP_PREFIX + path: item for path, item in webapp["paths"].items()}

    # --- backoffice ----------------------------------------------------------
    apply_filters(backoffice, filters["backoffice"], "", "backoffice")
    # token endpoint authenticates via credentials in the body
    backoffice["paths"]["/backoffice/auth/ext/token"]["post"]["security"] = []
    prune_components(backoffice)

    # --- sense ---------------------------------------------------------------
    apply_filters(sense, filters["sense"], "", "sense")
    prune_components(sense)

    # --- merge ---------------------------------------------------------------
    merged: dict[str, Any] = {
        "openapi": "3.1.0",
        "info": {
            "title": "Sympheny API",
            "summary": "Programmatic access to the Sympheny energy system optimization platform.",
            "description": (
                "The Sympheny API gives you programmatic access to the Sympheny platform "
                "for designing and optimizing multi-energy systems.\n"
                "\n"
                "Use it to automate everything you can do in the Sympheny web application: "
                "create projects and analyses, model energy hubs, demands, supply "
                "technologies and networks, run optimizations, and integrate the platform "
                "into your own tools and workflows.\n"
                "\n"
                "## API areas\n"
                "\n"
                "- **Platform** (`/sympheny-app`) - manage projects, analyses, scenarios, "
                "hubs, energy carriers, demands, technologies and networks.\n"
                "- **Account** (`/backoffice`) - obtain access tokens and inspect your "
                "user profile.\n"
                "- **Solver** (`/sense-api`) - submit solver jobs, track their progress, "
                "and manage your job quota.\n"
                "\n"
                "## Authentication\n"
                "\n"
                "Request a JWT access token with your Sympheny credentials via "
                "`POST /backoffice/auth/ext/token`, then send it with every request in "
                "the `Authorization: Bearer <token>` header.\n"
                "\n"
                "## Client library\n"
                "\n"
                "A Python client is available as "
                "[sympheny-toolbox](https://github.com/urban-sympheny/sympheny-toolbox)."
            ),
            "version": "1.0.0",
            "contact": {
                "name": "Sympheny",
                "url": "https://www.sympheny.com",
            },
        },
        "servers": [{"url": SERVER_URL}],
        "paths": {},
        "components": {"schemas": {}, "securitySchemes": {}},
        "tags": [],
    }

    labels = {id(webapp): "Webapp", id(api_services): "ApiServices", id(backoffice): "Backoffice", id(sense): "Sense"}
    for spec in (webapp, api_services, backoffice, sense):
        for path in spec["paths"]:
            if path in merged["paths"]:
                raise SystemExit(f"path collision: {path}")
        merge_schemas(merged, spec, labels[id(spec)])
        merged["paths"].update(spec["paths"])

    # single bearer scheme for all backends (webapp's bearerAuth is equivalent;
    # APIKeyHeader is internal-only and never referenced by kept operations)
    merged["components"]["securitySchemes"] = {"HTTPBearer": backoffice["components"]["securitySchemes"]["HTTPBearer"]}

    # --- tags ----------------------------------------------------------------
    tag_descriptions = {tag["name"]: tag.get("description") for spec in (webapp, api_services, backoffice, sense) for tag in spec.get("tags", [])}
    merged["x-tagGroups"] = []
    for group_name, spec in (
        ("Platform", webapp),
        ("Services", api_services),
        ("Account", backoffice),
        ("Solver", sense),
    ):
        names = sorted(used_tags(spec))
        if not names:
            continue
        merged["x-tagGroups"].append({"name": group_name, "tags": names})
        for name in names:
            tag: dict[str, Any] = {"name": name}
            if tag_descriptions.get(name):
                tag["description"] = tag_descriptions[name]
            merged["tags"].append(tag)

    # --- validate: every $ref must resolve ------------------------------------
    refs: set[str] = set()
    collect_refs(merged, refs)
    available = {f"#/components/schemas/{name}" for name in merged["components"]["schemas"]}
    dangling = refs - available
    if dangling:
        raise SystemExit(f"dangling $refs: {sorted(dangling)}")

    sort_output(merged)
    OUTPUT.write_text(json.dumps(merged, indent=2) + "\n")
    ops = sum(1 for item in merged["paths"].values() for method in item if method in HTTP_METHODS)
    print(f"wrote {OUTPUT}: {len(merged['paths'])} paths, {ops} operations, {len(merged['components']['schemas'])} schemas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
