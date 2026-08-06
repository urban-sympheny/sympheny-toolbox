#!/usr/bin/env python3
"""Download the current webapp OpenAPI export and report how it differs from the one on disk.

Maintainer-only: the export is an internal Sympheny artifact, so both files are git-ignored.

    uv run python scripts/fetch_webapp_openapi.py --creds creds.properties

Writes ``specs/webapp_openapi_latest.json`` and prints the operations and schemas that changed
against ``specs/webapp_openapi.json``. Nothing is overwritten — compare, then replace by hand and
rerun ``scripts/merge_openapi.py`` followed by ``scripts/generate_models.py``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from sympheny_toolbox import Sympheny
from sympheny_toolbox.utils import load_creds_basic


SPECS = Path(__file__).resolve().parents[1] / "specs"
CURRENT = SPECS / "webapp_openapi.json"
LATEST = SPECS / "webapp_openapi_latest.json"
API_DOCS = "/sympheny-app/v3/api-docs"


def operations(spec: dict[str, Any]) -> dict[str, Any]:
    """Every operation of a spec, keyed ``"GET /path"``."""
    return {f"{method.upper()} {path}": operation for path, methods in spec["paths"].items() for method, operation in methods.items()}


def schemas(spec: dict[str, Any]) -> dict[str, Any]:
    return dict(spec["components"]["schemas"])


def changed(current: dict[str, Any], latest: dict[str, Any]) -> set[str]:
    """Names present in both, whose definition is not identical."""
    return {name for name in current.keys() & latest.keys() if json.dumps(current[name], sort_keys=True) != json.dumps(latest[name], sort_keys=True)}


def show(label: str, names: set[str]) -> None:
    print(f"  {label}: {len(names)}")
    for name in sorted(names):
        print(f"    {name}")


def compare(current: dict[str, Any], latest: dict[str, Any]) -> None:
    print(f"\nDifferences ({CURRENT.name} -> {LATEST.name}):")
    for label, old, new in (("operations", operations(current), operations(latest)), ("schemas", schemas(current), schemas(latest))):
        show(f"{label} added", new.keys() - old.keys())
        show(f"{label} removed", old.keys() - new.keys())
        show(f"{label} changed", changed(old, new))


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch the latest webapp OpenAPI export and diff it against the one on disk.")
    parser.add_argument("--creds", type=Path, default=Path("creds.properties"), help="Path to a .properties file (username=/password=)")
    args = parser.parse_args()

    username, password = load_creds_basic(args.creds)
    with Sympheny(username, password) as client:
        print(f"Fetching {client._transport.base_url}{API_DOCS}?select=essential")
        latest = client._transport.request_json("GET", API_DOCS, params={"select": "essential"})

    LATEST.write_text(json.dumps(latest, indent=2) + "\n")
    print(f"Saved {LATEST} ({len(latest['paths'])} paths, {len(latest['components']['schemas'])} schemas)")

    if not CURRENT.exists():
        print(f"{CURRENT} does not exist yet — nothing to compare against.")
        return 0
    compare(json.loads(CURRENT.read_text()), latest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
