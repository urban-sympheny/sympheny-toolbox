# Changelog

All notable changes to `sympheny-toolbox` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[2.1.0]: https://github.com/urban-sympheny/sympheny-toolbox/releases/tag/v2.1.0
