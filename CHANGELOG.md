# Changelog

All notable changes to `sympheny-toolbox` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- The published OpenAPI spec now includes a first api-services endpoint,
  `POST /api-services/gis/buildings`, which returns the buildings within an area as GeoJSON. It
  adds generated models (`BuildingsRequest`, `BuildingFeatureCollection`, `BuildingFeature`,
  `BuildingProperties`, `Address`, `Geometry`, and the `BuildingTypeEnum`, `FeatureEnum`,
  `FeatureCollectionEnum` and `FeatureGeoTypeEnum` enums) and a
  [Buildings](https://docs.sympheny.com/api/reference/buildings/) REST API reference page.
- The published spec picks up seven new webapp endpoints from the latest export, with their
  generated models and REST API reference entries:
  - energy demand database: `GET /sympheny-app/database-energy-demand-table` and
    `POST /sympheny-app/database-energy-demand-profile/{demandType}/calculate` (new
    [Energy demand database](https://docs.sympheny.com/api/reference/energy-demand-database/) page);
  - specs input file: `PUT /sympheny-app/v2/specs` starts generating the specs file (new
    [Specs](https://docs.sympheny.com/api/reference/specs/) page), and
    `GET /sympheny-app/scenario/{scenarioGuid}/specs-input-file-url` is polled for its URL;
  - scenario from Excel: `GET /sympheny-app/db-update/s3-presigned-url` returns an upload URL
    (new [Uploads](https://docs.sympheny.com/api/reference/uploads/) page); after the file is
    uploaded there, `POST /sympheny-app/v2/analysis/{guid}/scenario/excel` creates a scenario from
    it, or `PUT /sympheny-app/v2/scenarios/{scenarioGuid}/excel` replaces one.

### Changed
- Maintainer tooling (no change to the published spec or the SDK): `scripts/fetch_webapp_openapi.py`
  is now `scripts/fetch_openapi.py`. It fetches the webapp and the api-services
  (`/api-services/api-docs`) exports (`--source` picks one) and diffs each against the copy on disk.
  The backoffice and sense exports stay local files until they get a docs endpoint.
- `scripts/merge_openapi.py` now takes the endpoints to publish from the committed
  `specs/openapi_filters.toml`: include/exclude patterns per source (`METHOD /path` globs, `tag:`,
  `op:`), with a warning for patterns that match nothing. This replaces the hardcoded backoffice and
  sense selections. api-services is merged as a new source, as an allowlist
  (its paths already start with `/api-services`; its caller tags such as `Web App FE` are dropped):
  nothing is published until its `include` names it. The non-required-means-nullable contract
  still applies to the webapp export only.
- `scripts/merge_openapi.py` now sorts the merged spec's paths, and the methods within each, so a
  reordered upstream export no longer churns `specs/sympheny_openapi.json`. This change reorders
  the committed spec (and its `docs/api/openapi.json` copy) once, with identical content. Component
  schemas keep their order on purpose: sorting them would renumber the generated enum models
  (`Version`, `Version1`, …) and rename public SDK classes.

### Docs
- Removed the beta announcement banner and the `overrides/main.html` theme override it lived in
  (with `custom_dir` and the `announce.dismiss` theme feature): the legacy documentation at
  support.app.sympheny.com is being retired and redirected to
  [docs.sympheny.com](https://docs.sympheny.com), so the banner's pointer to it no longer holds.
- Added the quick-start tutorial video to
  [Quick start](https://docs.sympheny.com/web-app/getting-started/quick-start/), with an English
  caption track served from the site (`docs/web-app/getting-started/quick-start-tutorial.en.vtt`);
  browsers reject a cross-origin caption track, so it ships with the docs rather than with the
  video on S3.
- Quick start now lazy-loads its screenshots (`{ loading=lazy }` on all but the first two of 52
  images, 11.3 MB in total), so the page no longer fetches every screenshot up front.
- Documentation prose is now British English with the `-ise` convention (`optimise`, `organisation`,
  `colour`, `centre`, `modelling`, `analyse`, `licence`), applied across 47 hand-written pages. UI
  strings (**Database Center**, **Organization Database**, the **Optimize** sizing option),
  code identifiers and enum values (`organizationId`, `colorHexCode`, `SPORTS_CENTER`), the
  generated reference pages, and filenames keep their source spelling. The rule and its four
  exemptions are recorded in `AGENTS.md` and the `docs` skill.

## [3.0.1] - 2026-08-07

### Changed
- CI workflow (`.github/workflows/ci.yml`) permissions are scoped to `contents: read`, and runs are
  grouped by ref with in-progress pull-request runs cancelled on new pushes.

## [3.0.0] - 2026-08-06

The v3 release: the SDK now wraps exactly the endpoints of the official OpenAPI export, regenerated
from the current webapp spec, and the documentation moves to a full site at
[docs.sympheny.com](https://docs.sympheny.com). Changes below are relative to 2.1.0.

### Removed
- **Breaking:** `client.unofficial` and every endpoint it exposed. The SDK now wraps only
  endpoints present in the official OpenAPI export; the missing ones (scenario-Excel upload,
  specs generation) have been requested from the backend team.
- **Breaking:** the workflows built on those endpoints — `create_scenario_from_excel`,
  `create_variants_from_excel`, `create_variants_from_dict`, `get_variants_dict`,
  `generate_input_file`, `create_enymap_scenario`, `get_demand_profile` — and their constants
  (`VARIANTS_SHEET`, `PROFILES_SHEET`, `ENYMAP_*`).
- **Breaking:** the Excel helpers that only served those workflows: `excel.build_variants_workbook`,
  `excel.read_profile_input_sheet`, and `excel.PROFILE_LENGTH`.
- `KNOWN_ISSUES.md` (added in 2.1.0): every tracked API issue is fixed upstream (verified against
  the API on 2026-08-06), and the corresponding client-side workarounds are gone from the SDK.
- The manual `renameScenario`/`copyScenario` path patching in `scripts/merge_openapi.py`: both
  operations are present in the upstream webapp export.

### Changed
- **Breaking:** the public spec and models are regenerated from the current webapp OpenAPI export,
  in which every body-carrying PUT endpoint has a dedicated request DTO (no server-owned audit
  timestamps or other response-only fields). Every `update()` method now takes the matching model —
  for example `Hubs.update` takes `HubRequestDtoPUT` (was `HubResponseDto`), `Stages.update` takes
  `StageCore`, and the remaining updates take their respective `*RequestDtoPUT` DTOs.
- **Breaking:** HTTP 403 responses now raise the new `PermissionDeniedError` (the authenticated
  user may not perform the action) instead of `AuthenticationError`, which is now raised only for
  HTTP 401 (missing/invalid/expired token). Both remain `APIError` subclasses; code catching
  `AuthenticationError` for 403s must switch to `PermissionDeniedError`.
- Response fields the API can legitimately return as null (for example
  `NetworkLinkResponseDtoV2.network_loss` and `EnergyCarrierResponseDto.color_hex_code`) are now
  optional in the generated models, so strictly validated reads no longer fail on scenarios with
  unset values. Cost/CO2/capacity numerics document the backend's 5-decimal limit
  (`multipleOf: 1e-05`) in the spec.
- `Scenarios.copy` now documents that `name` is honoured with and without
  `analysis_destination_guid`, matching the fixed backend behavior.
- Moved the OpenAPI specs (`sympheny_openapi.json` and the git-ignored upstream exports) from
  `docs/` to `specs/` — `docs/` now holds only documentation-site content.
- Internal client modules are flattened to one file per resource (for example `_async/energy.py`
  becomes `energy_carriers.py`, `impex.py`, `profiles.py`, `energy_demands.py`, and
  `solar_resources.py`). Purely a code-layout change — the resource groups on the client and every
  public import are unchanged.
- Agent tooling: the repo's process rules are split into skills under `.agents/skills/`
  (`docs`, `sdk-change`, `release`), with `AGENTS.md` reduced to the binding rules and an index.

### Added
- `scripts/fetch_webapp_openapi.py` (maintainer-only): downloads the current webapp OpenAPI export
  and prints the operations and schemas that changed against the one on disk.

### Docs
- Added the documentation site (Zensical, `docs/` + `zensical.toml`) at
  [docs.sympheny.com](https://docs.sympheny.com), with four surfaces: Web app, REST API, Python
  SDK, and Use with AI. Built strict (`--clean --strict`, broken links fail) as a PR check and
  deployed to GitHub Pages on push to `main` (`.github/workflows/docs.yml`). A `Documentation` URL
  was added to the PyPI metadata.
- Migrated the entire Sympheny Help Center (Confluence) into the Web app tab: all 76 pages
  accounted for, rewritten to the docs style guide — 169 images optimized, the 18 screencasts the
  export had dropped plus all spreadsheet/data attachments re-hosted on S3, every dead V2/Confluence
  link purged, quickstart completed, glossary rebuilt as a linked index, outdated tutorials
  deliberately dropped. The section is organized as Getting started, a flat Step-by-step guide
  (project and analysis pages, the eight scenario steps, Execution, Results dashboard), Concepts,
  Parameters, Advanced workflows, and Support.
- Added the generated REST API reference (`scripts/generate_api_reference.py`, one page per tag
  from `specs/sympheny_openapi.json`) and the generated SDK reference (one page per resource group
  plus grouped model pages, from the async client source) — cross-linked both ways via
  `docs/_data/sdk_map.yml`, with stale-generation and drift checks
  (`scripts/check_sdk_docs_drift.py`) run on every PR. The sync client is deliberately not
  documented separately; every example carries linked Sync/Async tabs.
- Hand-wrote the REST API overview and authentication guide, the SDK index (install, quickstart,
  error hierarchy, sync-vs-async explainer), and the end-to-end SDK workflow guides.
- Added the AI surface: `llms.txt`/`llms-full.txt` generated into the built site
  (`scripts/generate_llms_txt.py`), an MCP setup page (placeholder until the server ships), the
  Scalar API explorer (`docs/api/explorer.html`, its own nav entry under REST API), a dismissible
  beta banner pointing to the legacy docs, cookie-consent config, and footer Support/Privacy links.
- Branded the site with the Sympheny palette and wordmark (system/light/dark schemes), added the
  icon-card landing page, deduplicated the sidebar via `navigation.indexes`, and tagged every
  hand-written page with a small controlled search-tag vocabulary.
- Condensed `README.md` to install, quick start, and pointers into the documentation site.

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

[3.0.1]: https://github.com/urban-sympheny/sympheny-toolbox/releases/tag/v3.0.1
[3.0.0]: https://github.com/urban-sympheny/sympheny-toolbox/releases/tag/v3.0.0
[2.1.0]: https://github.com/urban-sympheny/sympheny-toolbox/releases/tag/v2.1.0
