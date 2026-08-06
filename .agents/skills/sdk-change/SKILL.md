---
name: sdk-change
description: >
  How to change the Python SDK and drive its regeneration pipeline. Use this
  skill for ANY task that touches src/sympheny_toolbox/ or specs/ — adding or
  changing a client method, adding a resource group, refreshing the OpenAPI spec
  and the generated models, regenerating the sync client, or anything that moves
  the client's public surface — even if the user doesn't name the pipeline
  (e.g. "add an endpoint for X", "the spec changed", "the sync client is stale",
  "fix the return type of scenarios.copy").
---

# SDK change skill

The client is layered, and most of the layers are generated. Editing the wrong
layer is the standard way to lose work here: the next regeneration overwrites
it, or `./scripts/check.sh` fails on drift.

## Layering map

| Layer | Path | Kind |
|---|---|---|
| Merged OpenAPI spec | `specs/sympheny_openapi.json` | **generated** (maintainer-only, from private exports) |
| Pydantic models | `src/sympheny_toolbox/models.py` | **generated** from the spec |
| Async client | `src/sympheny_toolbox/_async/` | hand-written, **source of truth** |
| Sync client | `src/sympheny_toolbox/_sync/` | **generated** from `_async/` |
| Helpers | `workflows.py`, `excel.py`, `utils.py`, `errors.py`, `_envelope.py` | hand-written |
| SDK reference pages | `docs/sdk/reference/` | **generated**, drift-checked |

Never hand-edit a generated layer. To change what it contains, change its source
and regenerate.

## Task: edit client behavior

1. **Edit `_async/` only.** One file per resource class (flat layout:
   `_async/hubs.py` holds `AsyncHubs`); `_sync/` is derived and is deleted and
   rewritten wholesale on every regeneration.
2. **Keep `_async/` unasync-safe.** `scripts/generate_sync.py` is a token
   transform, not a parser, so the async source must obey:
   - no `asyncio` imports and no `asyncio`-only constructs;
   - the substring `Async` appears only as a class-name prefix (`AsyncHubs`,
     `httpx.AsyncClient`, `AsyncTransport`) — never inside prose, variable
     names, or string literals, because `Async(\w+)` is stripped everywhere;
   - no "async"/"asynchronous" wording in docstrings, except the bare word
     `asynchronous`, which is mapped to `synchronous`.
3. **Embed the REST call in every public method docstring**, as a one-line
   summary ending in a code-span `` `METHOD /path` ``:

   ```python
   async def list(self, scenario_guid: str) -> list[HubResponseDto]:
       """List the hubs of a scenario. ``GET /sympheny-app/scenarios/{scenarioGuid}/hubs``"""
   ```

   `scripts/check_sdk_docs_drift.py` parses this; a missing or malformed call
   fails the check. Use the spec's path template, not the f-string.
4. **A new resource group** needs its own `_async/<resource>.py`, an import and
   an attribute assignment in `_async/client.py`, a test in
   `tests/test_resources.py`, and a `docs/sdk/reference/<resource>.md` page.
5. **Regenerate the sync client:** `uv run python scripts/generate_sync.py`
   (`--check` is what CI runs; `./scripts/check.sh` fails if `_sync/` is stale).

## Task: refresh the spec and models (maintainer-only)

The upstream exports are internal, git-ignored artifacts — a fresh clone cannot
run this. In order:

1. `uv run python scripts/fetch_webapp_openapi.py --creds creds.properties` —
   writes `specs/webapp_openapi_latest.json` and prints the operation/schema
   diff. It overwrites nothing: review the diff, then copy it over
   `specs/webapp_openapi.json` by hand.
2. `uv run python scripts/merge_openapi.py` — merges the webapp, backoffice, and
   sense exports into `specs/sympheny_openapi.json` and applies the nullability
   contract (a property absent from its schema's `required` may be null).
3. `uv run python scripts/generate_models.py` — regenerates `models.py`.
4. Reconcile `_async/` with the new models (changed request/response DTOs,
   new or removed operations), then regenerate `_sync/`.
5. `uv run python scripts/generate_api_reference.py` — regenerates the REST API
   reference; then the SDK reference per `.agents/skills/docs/SKILL.md` →
   `regen-sdk-reference`.

## After any public-surface change

- `uv run python scripts/check_sdk_docs_drift.py` must pass; pass `--write-map`
  when the `operationId` → `resource.method` mapping changed.
- Update the SDK reference pages via the docs skill (they are agent-written, not
  script-generated).
- Update `tests/` — tests run against `httpx.MockTransport` and must never reach
  the real API.
- Update `README.md` if the change is user-visible.
- Add a `CHANGELOG.md` entry and bump `pyproject.toml` per the versioning rules
  in `AGENTS.md`; releasing is `.agents/skills/release/SKILL.md`.

## Verification (end every task with this)

1. `./scripts/check.sh` — must pass (it covers `_sync/` drift, ruff format, ruff
   check, mypy, and the test suite under coverage).
2. If docs changed, the docs skill's Verification section as well.
3. `git diff --stat` matches expectations: no churn in generated files you did
   not intend to regenerate.
