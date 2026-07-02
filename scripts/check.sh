#!/usr/bin/env bash
# Run all repo verification checks (see AGENTS.md).
set -euo pipefail
cd "$(dirname "$0")/.."

uv run ruff format .
uv run ruff check .
uv run mypy .
