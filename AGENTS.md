# AGENTS.md

Rules for AI coding agents working in this repository. These are binding unless the user explicitly overrides them in chat.

## Git

- **Never push to the remote.** The maintainer reviews and pushes manually.
- Only create local commits if explicitly asked.
- Do not create branches or tags unless explicitly asked.

## Dependencies

- Prefer the Python standard library. Add a third-party dependency only if it gives a clear, real benefit over the stdlib equivalent — ask before adding, don't assume.
- No dependency may be added but left unused. If a library stops being used, remove it from `pyproject.toml`.
- Manage dependencies with `uv` (`uv add`, `uv remove`, `uv sync`) so `uv.lock` stays consistent.

## Code style & structure

- Python `>=3.11`, `src/` layout, package `sympheny_toolbox`.
- Keep things minimal: no speculative abstractions, no unused tooling, no dead code.
- All code must be fully type-annotated (mypy runs with `disallow_untyped_defs`).
- Linting and formatting are governed by the ruff config in `pyproject.toml` (line length 150). Do not change lint/type-check config to silence findings — fix the code instead.

## Generated code (never edit by hand)

- `src/sympheny_toolbox/models.py` is generated from `docs/sympheny_openapi.json` — regenerate with `uv run python scripts/generate_models.py`.
- `src/sympheny_toolbox/_sync/` is generated from `src/sympheny_toolbox/_async/` — regenerate with `uv run python scripts/generate_sync.py`.
- To change client behavior, edit `src/sympheny_toolbox/_async/` (the source of truth) and regenerate. Keep `_async/` unasync-safe: no `asyncio` imports, the substring "Async" only as a class-name prefix, no "async"/"asynchronous" wording in docstrings except the word "asynchronous" (which is mapped to "synchronous").
- `./scripts/check.sh` fails if `_sync/` is out of date.

## Verification (required after finishing any code change)

Run and pass:

```sh
./scripts/check.sh
```

It runs the `_sync/` drift check, `uv run ruff format .`, `uv run ruff check .`, `uv run mypy .`, and the test suite under `coverage` (`uv run coverage run -m pytest -q` + `uv run coverage report`).
CI (`.github/workflows/ci.yml`, also called by the publish workflow) runs the same script with `--ci`, which fails on formatting drift instead of reformatting.

## Versioning

- Maintain semantic versioning (MAJOR.MINOR.PATCH) in `pyproject.toml`:
  - MAJOR — breaking API changes
  - MINOR — new, backward-compatible features
  - PATCH — bug fixes
- A `v*` tag push triggers a publish to PyPI (the workflow checks that the tag matches the `pyproject.toml` version and that `./scripts/check.sh --ci` passes) — never tag.

## Docs & tests

- Update documentation whenever behavior or interfaces change.
- Update tests whenever behavior or interfaces change. Tests live under `tests/` and run against a mock API (`httpx.MockTransport`); they must never hit the real Sympheny API.
