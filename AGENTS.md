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

## Verification (required after finishing any code change)

Run and pass:

```sh
./scripts/check.sh
```

It runs `uv run ruff format .`, `uv run ruff check .`, and `uv run mypy .`.
Once a test suite exists under `tests/`, add `uv run pytest` to the script.

## Versioning

- Maintain semantic versioning (MAJOR.MINOR.PATCH) in `pyproject.toml`:
  - MAJOR — breaking API changes
  - MINOR — new, backward-compatible features
  - PATCH — bug fixes
- A `v*` tag push triggers a publish to PyPI — never tag.

## Docs & tests

- Update documentation whenever behavior or interfaces change.
- Update tests whenever behavior or interfaces change (once the test suite exists).
