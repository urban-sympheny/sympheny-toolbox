# Handoff: Agent Instructions Setup + API Client Migration

Self-contained context export for continuing this work in a fresh session.
Read together with `docs/toolbox_setup_plan.md` (the original task definition —
its working process and global rules apply to everything below).

---

## 1. Repo state

- Package **`sympheny-toolbox` v1.2.0** — lightweight Python wrapper for the Sympheny SaaS API.
  Published to PyPI. Repo: `urban-sympheny/sympheny-toolbox`.
- Layout: `src/sympheny_toolbox/` (~690 LOC): `sympheny.py` (main `Sympheny` class,
  requests-based, sync only), `execution.py`, `execution_results.py`, `enymap.py`,
  `utils.py`, `utils_demand.py`, `utils_variant.py`.
- Runtime deps: `jproperties`, `openpyxl`, `pandas`, `requests`.
- Dev tooling (already configured in `pyproject.toml`): **uv** (build backend `uv_build`),
  **ruff** (target py311, line-length 150, rules E/W/F/B/I/UP/S/C4/C90/SIM/TC/RUF/PT),
  **mypy**, **pytest** + pytest-asyncio. Python `>=3.11,<4`.
- CI: publish-to-PyPI on `v*` tag push (uv build/publish). No lint/test CI.
- No AGENTS.md / CLAUDE.md / .agents / .claude exist yet.

## 2. Work already completed (previous sessions)

### Merged OpenAPI spec
- `scripts/merge_openapi.py` (stdlib-only, rerunnable) merges three backend specs from `docs/`:
  - `webapp_openapi.json` (3.0.1, upgraded to 3.1 during merge; ALL endpoints kept;
    every non-required field made nullable; paths prefixed `/sympheny-app`)
  - `backoffice_openapi.json` (only `POST /backoffice/auth/ext/token` — with `security: []` —
    and `GET /backoffice/ext/users/profile`)
  - `sense_openapi.json` (only the 6 "External Solver Jobs" endpoints under `/sense-api`)
- Output: **`docs/sympheny_openapi.json`** — OpenAPI 3.1.0, 73 paths, 85 operations,
  156 schemas. Validated with openapi-spec-validator.
- Single server `https://eu-north-1-api.sympheny.com`; single security scheme `HTTPBearer`
  (http/bearer/JWT — webapp's `bearerAuth` folded in; internal-only `APIKeyHeader` removed).
- Unused schemas pruned via transitive $ref walk; `x-tagGroups`: Platform (`/sympheny-app`),
  Account (`/backoffice`), Solver (`/sense-api`).
- Public-facing `info` description covers API areas, auth flow, link to this package.
- Manual addition: `PUT /scenarios/copy/{scenarioGuid}` (copyScenario) was hand-copied into
  `webapp_openapi.json` from `docs/legacy_webapp.json` (Swagger 2.0 legacy export) because the
  current webapp export lacks it. Noted in the merge script docstring.
- Dev base URL also exists: `https://eu-north-1-api.dev.sympheny.com` (used by old client).

### Known gap: old-client endpoints NOT in the merged spec (~16)
The current client calls these, but they are absent from `docs/sympheny_openapi.json`
(missing from the webapp export; some exist in `docs/legacy_webapp.json`):

| Method | Path | Used in |
|---|---|---|
| DELETE | `/sympheny-app/master-scenario/{id}/scenario-variants` | sympheny.py |
| GET | `/sympheny-app/master-scenario/{id}/scenario-variants` | sympheny.py |
| POST | `/sympheny-app/master-scenario/` | sympheny.py |
| GET | `/sympheny-app/master-scenario/{id}/scenario-variants-excel` | sympheny.py |
| PUT | `/sympheny-app/scenario-variants-excel` | sympheny.py |
| GET | `/sympheny-app/analysis/{id}` | sympheny.py (spec has only DELETE) |
| GET | `/sympheny-app/db-update/s3-presigned-url` | sympheny.py |
| POST | `/sympheny-app/v2/analysis/{id}/scenario/excel` | sympheny.py |
| PUT | `/sympheny-app/scenarios/{id}/close-diagram` | sympheny.py |
| PUT | `/sympheny-app/v2/specs` | sympheny.py |
| PUT | `/sympheny-app/v2/scenarios/{id}/specs` | enymap.py |
| POST | `/sympheny-app/analysis/{id}/scenario-enymap` | enymap.py |
| POST | `/sympheny-app/scenario-enymap/{id}/create-gis-hub` | enymap.py |
| POST | `/sympheny-app/scenario-enymap/{id}/create-demand-solar` | enymap.py |
| GET | `/sympheny-app/database-energy-demands/{id}/profile` | utils_demand.py |
| GET/POST | `/api-services/gis/background`, `/api-services/demand/hub_demand` | enymap.py, utils_demand.py — a 4th backend (`api-services`), no spec available |

These map to Phase 2 item 3 in the task doc: keep them, clearly marked as unofficial.

### Auth flow (as implemented in old client)
`POST {base}/backoffice/auth/ext/token` with `{"email", "password"}` →
`access_token` (JWT) → `Authorization: Bearer <token>` on all calls.
Credentials loaded from a `.properties` file via `jproperties` (`utils.load_creds_basic`).

## 3. User decisions (confirmed in chat — binding)

1. AGENTS.md **includes tooling conventions** (uv, ruff, mypy) as rules, plus two extra rules:
   - **No library may be added but left unused** (dependency hygiene).
   - **Agents must run ruff and mypy after finishing work** to verify.
2. No extra org-specific rules beyond `docs/toolbox_setup_plan.md` globals.
3. Phase 2 migration is a **clean break in 2.0.0** — old modules removed/replaced outright,
   no deprecation shims.

## 4. Phase plan and status

Work through phases in order; **pause for user review between phases**; before each phase ask
clarifying questions; before writing Phase 2 code, present the proposal and wait for confirmation.

### Phase 1 — Agent instruction files (NEXT, not started)
1. `AGENTS.md` at repo root — research current agents.md conventions first. Content: the
   global rules from `docs/toolbox_setup_plan.md` + repo conventions (uv, ruff, mypy,
   src layout) + the two extra rules from §3. Rules only — no objectives/background.
2. `CLAUDE.md` stub pointing to AGENTS.md (no duplication).
3. `.agents/skills/` + symlink `.claude/skills -> .agents/skills` — only if skills are
   actually added; otherwise skip.
4. Evaluate MCP servers (e.g. Context7); add config only if genuinely useful, else just report.
5. Recommendation (with reasoning) on whether to add `docs/adr/` — user hasn't decided.

### Phase 2 — API client from `docs/sympheny_openapi.json` (after Phase 1 review)
- First: written proposal + file layout, wait for confirmation. Evaluate:
  - codegen (openapi-python-client, datamodel-code-generator) vs hand-written — pick least bloat.
    Working hypothesis: generate Pydantic models (dev-time codegen), hand-write a thin client.
  - **httpx** for sync+async in one surface (vs stdlib urllib) — justify.
  - **Pydantic** vs stdlib dataclasses — justify.
  - **Polars** — only if a real data need exists (current pandas usage is Excel/variant helpers);
    almost certainly not needed.
- Then implement: models → sync+async client core (auth via token endpoint, error handling,
  MCP-friendly surface) → unofficial endpoints (from §2 table) segregated and clearly marked →
  port/remove high-level helpers → update README/docs → **bump version to 2.0.0**.
- Audience note (do NOT put in AGENTS.md): MCP server embedding is priority #1; direct
  customer use is #2 — keep public surface clean/stable to avoid another breaking bump.

### Phase 3 — Tests
Deliberately deferred. Only flag as follow-up once the client is stable. Do not build now.

## 5. Todo IDs (for SQL tracking, if resumed with this tool)
Phase 1: `agents-md`, `claude-md-stub`, `skills-symlink`, `mcp-evaluation`, `adr-recommendation`.
Phase 2: `client-proposal` → `client-models` → `client-core` → `client-unofficial` →
`client-migration` (deps in that order). Phase 3: `flag-tests`.
