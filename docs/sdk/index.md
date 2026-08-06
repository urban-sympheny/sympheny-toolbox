---
tags:
  - sdk
  - getting-started
---

# Python SDK

`sympheny-toolbox` is the official Python client for the Sympheny API. It exposes every
documented REST endpoint as a typed method, validates requests and responses with
Pydantic models, and handles authentication (login, token caching, refresh) for you.

## Install

```sh
pip install sympheny-toolbox
```

Requires Python 3.11 or newer.

## One API, sync and async

Every method exists on both `Sympheny` and `AsyncSympheny` with identical signatures.
The sync client is generated from the async source, so the two can never diverge.
These docs describe the async client once; every code example has a **Sync** / **Async**
tab, and your choice persists across all pages.

## Quickstart

Authenticate with your Sympheny account credentials, then reach the endpoints through
resource groups on the client (`client.projects`, `client.scenarios`, …):

=== "Async"

    ```python
    import asyncio

    from sympheny_toolbox import AsyncSympheny


    async def main() -> None:
        async with AsyncSympheny("you@example.com", "password") as client:
            projects = await client.projects.list()
            for project in projects:
                print(project.project_name, project.project_guid)


    asyncio.run(main())
    ```

=== "Sync"

    ```python
    from sympheny_toolbox import Sympheny

    with Sympheny("you@example.com", "password") as client:
        projects = client.projects.list()
        for project in projects:
            print(project.project_name, project.project_guid)
    ```

The client is a context manager; it closes its HTTP connection pool on exit. Outside a
`with` block, call `aclose()` (async) or `close()` (sync) yourself.

### Client options

| Argument | Default | Description |
| --- | --- | --- |
| `username` | required | Sympheny account email address. |
| `password` | required | Sympheny account password. |
| `is_dev` | `False` | Use the development environment instead of production. |
| `base_url` | production URL | Override the API base URL entirely (takes precedence over `is_dev`). |
| `timeout` | `30.0` | Request timeout in seconds. |

### Errors

Failed requests raise typed exceptions from `sympheny_toolbox.errors`, all subclasses of
`SymphenyError`: `AuthenticationError` (401), `PermissionDeniedError` (403),
`NotFoundError` (404), `APIError` (any other unsuccessful status, with `status_code` and
`body` attributes), and `UnexpectedResponseError` (the response lacked the expected
payload).

## Where to go next

- [Workflows](workflows/index.md): end-to-end guides for running a solver job and
  downloading the results.
- [SDK reference](reference/projects.md): one page per resource group, one section per
  method, each cross-linked to the REST operation it wraps.
- [Model reference](reference/models/common.md): the Pydantic request/response models,
  grouped by resource.
- [REST API reference](../api/index.md): the underlying HTTP API, if you need to call
  it directly.
