#!/usr/bin/env bash
# Run all repo verification checks (see AGENTS.md).
# Pass --ci to fail on formatting drift instead of reformatting in place.
set -euo pipefail
cd "$(dirname "$0")/.."

format_args=()
[[ "${1:-}" == "--ci" ]] && format_args=(--check)

uv run python scripts/generate_sync.py --check
uv run ruff format "${format_args[@]+"${format_args[@]}"}" .
uv run ruff check .
uv run mypy .
uv run coverage run -m pytest -q
uv run coverage report
