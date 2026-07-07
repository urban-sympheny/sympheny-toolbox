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

## Library documentation lookups

- For questions about any third-party library, framework, or tool (httpx, pydantic, Zensical, pytest, …), prefer the **context7 MCP server** over memory or web search — training data is often stale. Resolve the library ID first, then query with one focused question per call.
- Zensical resolves to `/zensical/docs`; for docs work the rules in `.agents/skills/docs/SKILL.md` ("Looking up Zensical behavior") take precedence.
- Finding a feature in upstream docs is not permission to use it — repo rules (dependency policy, docs whitelist) still govern.

## Code style & structure

- Python `>=3.11`, `src/` layout, package `sympheny_toolbox`.
- Keep things minimal: no speculative abstractions, no unused tooling, no dead code.
- All code must be fully type-annotated (mypy runs with `disallow_untyped_defs`).
- Linting and formatting are governed by the ruff config in `pyproject.toml` (line length 150). Do not change lint/type-check config to silence findings — fix the code instead.

## Generated code (never edit by hand)

- `specs/sympheny_openapi.json` (the public, committed spec) is merged by `scripts/merge_openapi.py` from git-ignored upstream Sympheny exports (`specs/webapp_openapi.json`, `backoffice_openapi.json`, `sense_openapi.json`, plus `renameScenario`/`copyScenario` re-added from `webapp_legacy_openapi.json`). Regenerating it is a maintainer-only step — a fresh clone lacks the private inputs. Do not hand-edit the merged file.
- `src/sympheny_toolbox/models.py` is generated from `specs/sympheny_openapi.json` — regenerate with `uv run python scripts/generate_models.py`.
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
- Record every notable change in `CHANGELOG.md` under the target version (Keep a Changelog format: `Added` / `Changed` / `Fixed` / `Docs`). Bump `pyproject.toml` and update the changelog in the same change.
- A `v*` tag push triggers a publish to PyPI (the workflow checks that the tag matches the `pyproject.toml` version and that `./scripts/check.sh --ci` passes) — never tag.

## Docs & tests

- Update documentation whenever behavior or interfaces change — this includes `README.md`, `CHANGELOG.md`, and, when a change adds or resolves an API quirk or its client-side workaround, `KNOWN_ISSUES.md` (mark the entry `Open` or `Fixed in SDK` and update its `Last updated` date).
- Update tests whenever behavior or interfaces change. Tests live under `tests/` and run against a mock API (`httpx.MockTransport`); they must never hit the real Sympheny API.
