# Changelog

All notable changes to `sympheny-toolbox` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0b1] - 2026-07-10

First beta of v3: the documentation site, plus one breaking error-handling change in the client.

### Changed
- **Breaking:** HTTP 403 responses now raise the new `PermissionDeniedError` (the authenticated
  user may not perform the action) instead of `AuthenticationError`, which is now raised only for
  HTTP 401 (missing/invalid/expired token). Both remain `APIError` subclasses; code catching
  `AuthenticationError` for 403s must switch to `PermissionDeniedError`.
- Moved the OpenAPI specs (`sympheny_openapi.json` and the git-ignored upstream exports) from
  `docs/` to `specs/`, and `KNOWN_ISSUES.md` from `docs/` to the repo root — `docs/` now holds only
  documentation-site content.

### Docs
- Added the documentation site (Zensical, `docs/` + `zensical.toml`), with four surfaces: Web
  Application, REST API, Python SDK, and Use with AI. Built strict (`--clean --strict`, broken
  links fail) as a PR check and deployed to GitHub Pages on push to `main`
  (`.github/workflows/docs.yml`).
- Migrated the entire Sympheny Help Center (Confluence) into the Web Application tab: all 76 pages
  accounted for, rewritten to the docs style guide — 169 images optimized, the 18 screencasts the
  export had dropped plus all spreadsheet/data attachments re-hosted on S3, every dead V2/Confluence
  link purged, quickstart completed, glossary rebuilt as a linked index, outdated tutorials
  deliberately dropped. Full page-by-page account in `migration-report.md`.
- Added the generated REST API reference (`scripts/generate_api_reference.py`: 19 pages, 87
  operations from `specs/sympheny_openapi.json`, plus a served spec copy for the Scalar-based API
  explorer) and the generated SDK reference (19 resource pages, 104 methods, grouped model pages,
  from the async client source) — cross-linked both ways via `docs/_data/sdk_map.yml`, with
  stale-generation and drift checks (`check_sdk_docs_drift.py`) run on every PR. The sync client is
  deliberately not documented separately; every example carries linked Sync/Async tabs.
- Hand-wrote the REST API overview and authentication guide, the SDK index (install, quickstart,
  error hierarchy, sync-vs-async explainer), and three end-to-end SDK workflow guides (scenario
  from Excel, run and poll a solver job, download results).
- Branded the site with the Sympheny palette and wordmark (system/light/dark schemes), added the
  icon-card landing page, deduplicated the sidebar via `navigation.indexes`, and tagged every
  hand-written page with a small controlled search-tag vocabulary.
- Added the AI surface: `llms.txt`/`llms-full.txt` generated into the built site
  (`scripts/generate_llms_txt.py`), an MCP setup page (placeholder until the server ships), the
  Scalar API explorer (`docs/api/explorer.html`, not in nav, no third-party proxy), a dismissible
  beta banner pointing to the legacy docs, cookie-consent config (no analytics wired yet), and
  footer Support/Privacy links.

## [2.1.0] - 2026-07-04

### Added
- `Scenarios.rename(scenario_guid, request)` — rename a scenario in place
  (`PUT /sympheny-app/scenarios/{scenarioGuid}`), and the `renameScenario` operation is now included in
  `docs/sympheny_openapi.json` (it was missing from the upstream export).
- `workflows.build_solver_job_request(...)` — build a `PostSolverJobExt` for a scenario.
- `workflows.execute_scenarios(client, requests, *, wait=True)` — submit multiple solver jobs in a
  single request; with `wait=False` it submits without polling.

### Fixed
- `Scenarios.delete` and `Analyses.delete` no longer raise when the API returns a `data: null` payload
  on a successful delete; a missing payload is treated as an empty `Status`.

### Changed
- `workflows.execute_scenario` is now a thin single-scenario wrapper over `execute_scenarios` (same
  behavior and signature); the solver-job request is built once in `build_solver_job_request`.

### Docs
- Added `docs/KNOWN_ISSUES.md`, a living record of known API behaviors and the client-side workarounds.
- Clarified that the upstream OpenAPI exports are internal and git-ignored — only the merged
  `docs/sympheny_openapi.json` is public.

## [2.0.0]

- Rewritten as a typed API client generated from the OpenAPI spec, with parallel async/sync clients.

[3.0.0b1]: https://github.com/urban-sympheny/sympheny-toolbox/releases/tag/v3.0.0b1
[2.1.0]: https://github.com/urban-sympheny/sympheny-toolbox/releases/tag/v2.1.0
