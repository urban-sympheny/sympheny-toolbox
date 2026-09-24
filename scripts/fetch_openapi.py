#!/usr/bin/env python3
"""Download the current backend OpenAPI exports and report how they differ from the ones on disk.

Maintainer-only: the exports are internal Sympheny artifacts, so all of these files are git-ignored.

    uv run python scripts/fetch_openapi.py --creds creds.properties
    uv run python scripts/fetch_openapi.py --creds creds.properties --source api-services

For each source (default: all of them), writes ``specs/<source>_openapi_latest.json`` and prints the
operations and schemas that changed against ``specs/<source>_openapi.json``. Nothing is overwritten —
compare, then replace by hand and rerun ``scripts/merge_openapi.py`` followed by
``scripts/generate_models.py``.

The backoffice and sense exports have no docs endpoint yet; they stay local files in ``specs/``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from sympheny_toolbox import Sympheny
from sympheny_toolbox.utils import load_creds_basic


SPECS = Path(__file__).resolve().parents[1] / "specs"

# source -> (docs endpoint, query params, file on disk, freshly fetched file)
SOURCES: dict[str, tuple[str, dict[str, str], Path, Path]] = {
    "webapp": ("/sympheny-app/v3/api-docs", {"select": "essential"}, SPECS / "webapp_openapi.json", SPECS / "webapp_openapi_latest.json"),
    "api-services": ("/api-services/api-docs", {}, SPECS / "api_services_openapi.json", SPECS / "api_services_openapi_latest.json"),
}


def operations(spec: dict[str, Any]) -> dict[str, Any]:
    """Every operation of a spec, keyed ``"GET /path"``."""
    return {f"{method.upper()} {path}": operation for path, methods in spec["paths"].items() for method, operation in methods.items()}


def schemas(spec: dict[str, Any]) -> dict[str, Any]:
    return dict(spec.get("components", {}).get("schemas", {}))


def changed(current: dict[str, Any], latest: dict[str, Any]) -> set[str]:
    """Names present in both, whose definition is not identical."""
    return {name for name in current.keys() & latest.keys() if json.dumps(current[name], sort_keys=True) != json.dumps(latest[name], sort_keys=True)}


def show(label: str, names: set[str]) -> None:
    print(f"  {label}: {len(names)}")
    for name in sorted(names):
        print(f"    {name}")


def compare(current: dict[str, Any], latest: dict[str, Any], current_name: str, latest_name: str) -> None:
    print(f"\nDifferences ({current_name} -> {latest_name}):")
    for label, old, new in (("operations", operations(current), operations(latest)), ("schemas", schemas(current), schemas(latest))):
        show(f"{label} added", new.keys() - old.keys())
        show(f"{label} removed", old.keys() - new.keys())
        show(f"{label} changed", changed(old, new))


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch the latest backend OpenAPI exports and diff them against the ones on disk.")
    parser.add_argument("--creds", type=Path, default=Path("creds.properties"), help="Path to a .properties file (username=/password=)")
    parser.add_argument("--source", choices=sorted(SOURCES), action="append", help="Source to fetch; repeatable (default: all)")
    args = parser.parse_args()

    username, password = load_creds_basic(args.creds)
    with Sympheny(username, password) as client:
        for name in args.source or SOURCES:
            api_docs, params, current_path, latest_path = SOURCES[name]
            print(f"\n[{name}] Fetching {client._transport.base_url}{api_docs}")
            latest = client._transport.request_json("GET", api_docs, params=params or None)

            latest_path.write_text(json.dumps(latest, indent=2) + "\n")
            print(f"Saved {latest_path} ({len(latest['paths'])} paths, {len(schemas(latest))} schemas)")

            if not current_path.exists():
                print(f"{current_path} does not exist yet — nothing to compare against.")
                continue
            compare(json.loads(current_path.read_text()), latest, current_path.name, latest_path.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
