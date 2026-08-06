# AGENTS.md

Rules for AI coding agents working in this repository. These are binding.

## Rule exceptions

When the maintainer asks for something that conflicts with these rules (or with a skill's rules),
don't silently comply and don't refuse. Ask which they want: **change the rule** — do the work and
update this file or the skill in the same change, so the rules stay true — or a **one-time
exception**, done as asked with a brief comment at the site marking it as maintainer-sanctioned.
Rules and reality must never drift apart silently.

## Skills

Process detail lives in `.agents/skills/`; read the relevant skill before starting.

- `docs` — anything under `docs/` or `zensical.toml`: writing guides, regenerating the references, nav, style.
- `sdk-change` — anything under `src/sympheny_toolbox/` or `specs/`: the layering and regeneration pipeline.
- `release` — cutting a version: changelog close-out, version bump, hand-off.

## Git

- **Never push to the remote.** The maintainer reviews and pushes manually.
- Only create local commits if explicitly asked.
- Do not create branches or tags unless explicitly asked.

## Dependencies

- Prefer the Python standard library. Add a third-party dependency only if it gives a clear, real benefit over the stdlib equivalent — ask before adding, don't assume.
- No dependency may be added but left unused. If a library stops being used, remove it from `pyproject.toml`.
- Manage dependencies with `uv` (`uv add`, `uv remove`, `uv sync`) so `uv.lock` stays consistent.

## Library documentation lookups

- For questions about any third-party library, framework, or tool (httpx, pydantic, Zensical, pytest, …), prefer the **context7 MCP server** over memory or web search — training data is often stale. Resolve the library ID first, then query with one focused question per call. Zensical resolves to `/zensical/docs`; for docs work the `docs` skill takes precedence.
- Finding a feature in upstream docs is not permission to use it — repo rules (dependency policy, docs whitelist) still govern.

## Code style & structure

- Python `>=3.11`, `src/` layout, package `sympheny_toolbox`.
- Keep things minimal: no speculative abstractions, no unused tooling, no dead code.
- All code must be fully type-annotated (mypy runs with `disallow_untyped_defs`).
- Linting and formatting are governed by the ruff config in `pyproject.toml` (line length 150). Do not change lint/type-check config to silence findings — fix the code instead.

## Generated — never edit by hand

Change the source and regenerate; process details in the `sdk-change` and `docs` skills.

- `specs/sympheny_openapi.json` — merged from private upstream exports (maintainer-only).
- `src/sympheny_toolbox/models.py` — generated from the spec.
- `src/sympheny_toolbox/_sync/` — generated from `_async/`, the hand-written source of truth.
- `docs/api/reference/` and `docs/sdk/reference/` — generated, drift-checked.

## Verification (required after finishing any code change)

Run and pass:

```sh
./scripts/check.sh
```

It runs the `_sync/` drift check, `uv run ruff format .`, `uv run ruff check .`, `uv run mypy .`, and the test suite under `coverage`.
CI (`.github/workflows/ci.yml`, also called by the publish workflow) runs the same script with `--ci`, which fails on formatting drift instead of reformatting.

## Versioning

- Maintain semantic versioning (MAJOR.MINOR.PATCH) in `pyproject.toml`: MAJOR — breaking API changes; MINOR — new, backward-compatible features; PATCH — bug fixes.
- Record every notable change in `CHANGELOG.md` under the target version (Keep a Changelog format: `Added` / `Changed` / `Fixed` / `Removed` / `Docs`). Bump `pyproject.toml` and update the changelog in the same change.
- A `v*` tag push triggers a publish to PyPI — never tag, never push.

## Docs & tests

- Update documentation whenever behavior or interfaces change — this includes `README.md` and `CHANGELOG.md`.
- Update tests whenever behavior or interfaces change. Tests live under `tests/` and run against a mock API (`httpx.MockTransport`); they must never hit the real Sympheny API.
