[![CI](https://github.com/urban-sympheny/sympheny-toolbox/actions/workflows/ci.yml/badge.svg)](https://github.com/urban-sympheny/sympheny-toolbox/actions/workflows/ci.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/sympheny-toolbox.svg?cacheSeconds=300)](https://pypi.org/project/sympheny-toolbox)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sympheny-toolbox.svg?cacheSeconds=300)](https://pypi.org/project/sympheny-toolbox)

# Sympheny Toolbox

The official typed Python client for the [Sympheny](https://www.sympheny.com) SaaS API: every documented endpoint as a typed method, synchronous **and** asynchronous, with authentication handled for you.

## Documentation

Full documentation lives at **<https://docs.sympheny.com/>**:

- SDK guide and reference: <https://docs.sympheny.com/sdk/>
- REST API reference: <https://docs.sympheny.com/api/>

## Install

```bash
pip install sympheny-toolbox
```

Requires **Python 3.11+**.

## Quick start

```python
from sympheny_toolbox import Sympheny

client = Sympheny("you@example.com", "your-password")

for project in client.projects.list():
    print(project.project_name)
```

The same API is available asynchronously via `AsyncSympheny`:

```python
from sympheny_toolbox import AsyncSympheny

async with AsyncSympheny("you@example.com", "your-password") as client:
    projects = await client.projects.list()
```

Endpoints are grouped on the client the way the documented API groups them (`client.projects`, `client.analyses`, `client.scenarios`, `client.hubs`, `client.solver_jobs`, and so on); see the [SDK reference](https://docs.sympheny.com/sdk/reference/projects/). Requests and responses use Pydantic models generated from the OpenAPI spec (`sympheny_toolbox.models`). Higher-level helpers that combine several calls, such as running a solver job and downloading its results, live in `sympheny_toolbox.workflows` and are documented under [Workflows](https://docs.sympheny.com/sdk/workflows/).

Failed requests raise `sympheny_toolbox.errors.SymphenyError` subclasses: `AuthenticationError` (401), `PermissionDeniedError` (403), `NotFoundError` (404), `APIError` (any other unsuccessful status), and `UnexpectedResponseError`.

## Development

The client is layered: the merged OpenAPI spec in `specs/` generates `models.py`, the hand-written asynchronous client in `_async/` is the source of truth, and the synchronous client in `_sync/` is generated from it by an unasync-style transform. Regenerate it with `uv run python scripts/generate_sync.py` after changing anything under `_async/`.

Run every check (drift check, ruff, mypy, tests under coverage) with `./scripts/check.sh`. Tests live under [`tests/`](tests/) and run against a mock API (`httpx.MockTransport`), so they need no credentials and never reach the real Sympheny API.

To release: bump the version in `pyproject.toml`, add the matching [`CHANGELOG.md`](CHANGELOG.md) entry, and push a `vX.Y.Z` tag. The [publish workflow](.github/workflows/publish.yml) checks that the tag matches the project version, runs all checks, and publishes to PyPI.
