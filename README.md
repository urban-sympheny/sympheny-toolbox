[![CI](https://github.com/urban-sympheny/sympheny-toolbox/actions/workflows/ci.yml/badge.svg)](https://github.com/urban-sympheny/sympheny-toolbox/actions/workflows/ci.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/sympheny-toolbox.svg?cacheSeconds=300)](https://pypi.org/project/sympheny-toolbox)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sympheny-toolbox.svg?cacheSeconds=300)](https://pypi.org/project/sympheny-toolbox)

# Sympheny Toolbox

A typed Python client for the [Sympheny](https://www.sympheny.com) SaaS API — full coverage of the documented API with synchronous **and** asynchronous support, plus high-level helpers to automate common workflows (create scenarios, run optimizations, manage variants, and more).

## Install

```bash
pip install sympheny-toolbox
```

Requires **Python 3.11+**.

## Quick start

```python
from sympheny_toolbox import Sympheny

client = Sympheny("you@example.com", "your-password")  # is_dev=True for the dev environment

for project in client.projects.list():
    print(project.project_name)
```

The same API is available asynchronously via `AsyncSympheny`:

```python
from sympheny_toolbox import AsyncSympheny

async with AsyncSympheny("you@example.com", "your-password") as client:
    projects = await client.projects.list()
```

Credentials can also be loaded from a Java-style `.properties` file (`username=...` / `password=...`):

```python
from sympheny_toolbox.utils import load_creds_basic

username, password = load_creds_basic("creds.properties")
```

> **Tip:** Don't commit credential files — use a secrets manager or `.gitignore`.

## Client structure

Every documented endpoint of the Sympheny API ([`specs/sympheny_openapi.json`](specs/sympheny_openapi.json)) is available as a typed method on a resource group:

| Resource group | Endpoints |
|---|---|
| `client.projects`, `client.analyses` | Projects and analyses |
| `client.scenarios`, `client.stages`, `client.hubs` | Scenario structure |
| `client.energy_carriers`, `client.energy_demands`, `client.impex`, `client.profiles`, `client.solar_resources` | Energy data |
| `client.conversion_technologies`, `client.storage_technologies`, `client.technology_packages` | Technologies |
| `client.network_technologies`, `client.network_links`, `client.intra_hub_network_links` | Networks |
| `client.solver_jobs` | Solver job submission, status, and usage |
| `client.users` | Account profile |
| `client.unofficial` | ⚠️ Endpoints **not part of the documented API** — may change without notice |

Requests and responses use Pydantic models generated from the OpenAPI spec (`sympheny_toolbox.models`). Errors are raised as `sympheny_toolbox.errors.SymphenyError` subclasses (`APIError`, `AuthenticationError`, `PermissionDeniedError`, `NotFoundError`).

Some backend endpoints have quirks the client works around (or that you need to work around yourself); these are documented in [`KNOWN_ISSUES.md`](KNOWN_ISSUES.md).

```python
from sympheny_toolbox import Sympheny, models

client = Sympheny("you@example.com", "your-password")

project = client.projects.create(models.ProjectRequestDto(project_name="My Project", version=models.Version.v2))
analysis = client.analyses.create(project.project_guid, models.AnalysisRequestDto(analysis_name="My Analysis"))
```

Only V2 projects are supported — `client.projects.create` raises `ValueError` for any other version.

## Workflows

Higher-level automation flows that combine multiple API calls live in `sympheny_toolbox.workflows` (synchronous client only):

```python
from sympheny_toolbox import Sympheny, workflows

client = Sympheny("you@example.com", "your-password")

# Find things by name
project = workflows.find_project(client, "My Project")
analysis = workflows.find_analysis(client, "My Analysis", str(project.project_guid))
scenario = workflows.find_scenario(client, "Base", str(analysis.analysis_guid))

# Create a scenario from an Excel file
scenario_guid = workflows.create_scenario_from_excel(client, "scenario.xlsx", "demo", str(analysis.analysis_guid))
print(workflows.scenario_url(client, scenario_guid))

# Create scenario variants (from a file or from in-memory data)
workflows.create_variants_from_excel(client, "variants.xlsx", scenario_guid)

# Execute and fetch results
job = workflows.execute_scenario(client, scenario_guid)
results = workflows.get_output_file_dict(client, job.id, solution_num=1)
print(workflows.dashboard_url(client, scenario_guid))

# Or submit several scenarios in a single request, without waiting for results
requests = [workflows.build_solver_job_request(guid) for guid in (scenario_guid,)]
workflows.execute_scenarios(client, requests, wait=False)
```

Rename a scenario in place with `client.scenarios.rename(scenario_guid, models.ScenarioRequestDto(scenario_name="..."))`.

### EnyMap scenarios

```python
scenario_guid = workflows.create_enymap_scenario(
    client,
    scenario_name="enymap_demo",
    analysis_guid=analysis_guid,
    techs=["PV", "HEAT_PUMP"],
    demands=["ELECTRICITY", "SPACE_HEATING"],
    imports=["ELECTRICITY"],
    exports=["HEAT_AMBIENT"],
    polygon=[[lon, lat], ...],
)
```

| Parameter | Options |
|-----------|---------|
| `techs` | `PV`, `HEAT_PUMP`, `GAS_BOILER`, `CHILLER`, `BATTERY`, `HOT_WATER_STORAGE` |
| `demands` | `HOT_WATER`, `SPACE_HEATING`, `ELECTRICITY`, `COOLING` |
| `imports` | `ELECTRICITY` |
| `exports` | `HEAT_AMBIENT`, `COOLING` |

## Migrating from 1.x

Version 2.0.0 is a complete rewrite and a breaking change:

- The `Sympheny` class is now imported from the package root: `from sympheny_toolbox import Sympheny`.
- Endpoint calls moved to resource groups (`client.projects.list()` instead of `s.list_projects()`), return typed Pydantic models instead of dicts, and an async client (`AsyncSympheny`) was added.
- The old high-level methods (`find_project`, `create_scenario_from_excel`, `execute_scenario`, ...) moved to `sympheny_toolbox.workflows` as functions taking the client as first argument.
- Undocumented endpoints are now clearly separated under `client.unofficial`.
- Dependencies were slimmed down to `httpx`, `pydantic`, and `openpyxl` (`requests`, `pandas`, `polars`, and `jproperties` were dropped).

## Development

The client is layered as follows:

- `specs/sympheny_openapi.json` — the public API spec, **merged** by `scripts/merge_openapi.py` from git-ignored upstream Sympheny exports (maintainer-only; a fresh clone lacks the private inputs).
- `sympheny_toolbox/models.py` — Pydantic models, **generated** from `specs/sympheny_openapi.json` via `scripts/generate_models.py`.
- `sympheny_toolbox/_async/` — the hand-written asynchronous client (source of truth).
- `sympheny_toolbox/_sync/` — the synchronous client, **generated** from `_async/` via `scripts/generate_sync.py` (unasync-style transform).
- `sympheny_toolbox/workflows.py`, `excel.py`, `utils.py` — hand-written helpers.

After changing anything under `_async/`, regenerate with `uv run python scripts/generate_sync.py`. Run all checks (drift check, ruff, mypy, pytest) with `./scripts/check.sh`.

Tests live under [`tests/`](tests/) and run against a mock API (`httpx.MockTransport`) — they never hit the real Sympheny API, so no credentials are needed to run them.

### Releasing

Bump the version in `pyproject.toml` (semantic versioning), add a matching entry to [`CHANGELOG.md`](CHANGELOG.md), then push a matching `vX.Y.Z` tag. The [publish workflow](.github/workflows/publish.yml) verifies that the tag matches the project version, runs all checks, and publishes to PyPI.
