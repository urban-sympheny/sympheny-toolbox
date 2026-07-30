---
tags:
  - sdk
  - workflow
---

# Create scenario from Excel

Turn a filled-in scenario Excel workbook into a Sympheny scenario you can execute. This
is the fastest way to create a fully-specified scenario in one call instead of building
it stage by stage.

## Prerequisites

- An **analysis GUID** to create the scenario in. List your projects with
  [`client.projects.list()`](../reference/projects.md#method-projects-list) and their
  analyses with
  [`client.analyses.list(project_guid)`](../reference/analyses.md#method-analyses-list),
  or copy the GUID from the analysis URL in the
  [web app](../../web-app/step-by-step-guide/analyses.md).
- A scenario **Excel workbook** with the sheets the importer expects (`Stages`, `Hubs`,
  `Energy Carriers`, `Demands`, `Conversion Techs`, …). Export one from an existing
  scenario in the web app to use as a template.

## Steps

Uploading happens in three calls: ask for a presigned upload URL, PUT the file to it,
then create the scenario from that URL.

=== "Async"

    ```python
    import asyncio
    from pathlib import Path

    from sympheny_toolbox import AsyncSympheny


    async def main() -> None:
        analysis_guid = "your-analysis-guid"
        content = Path("scenario.xlsx").read_bytes()

        async with AsyncSympheny("you@example.com", "password") as client:
            upload_url = await client.unofficial.get_upload_url()
            await client.unofficial.upload_to_presigned_url(upload_url, content)
            scenario_guid = await client.unofficial.create_scenario_from_excel_url(
                upload_url, "Scenario from Excel", analysis_guid
            )
            print("created scenario", scenario_guid)


    asyncio.run(main())
    ```

=== "Sync"

    ```python
    from pathlib import Path

    from sympheny_toolbox import Sympheny

    analysis_guid = "your-analysis-guid"
    content = Path("scenario.xlsx").read_bytes()

    with Sympheny("you@example.com", "password") as client:
        upload_url = client.unofficial.get_upload_url()
        client.unofficial.upload_to_presigned_url(upload_url, content)
        scenario_guid = client.unofficial.create_scenario_from_excel_url(
            upload_url, "Scenario from Excel", analysis_guid
        )
        print("created scenario", scenario_guid)
    ```

`create_scenario_from_excel_url` returns the new scenario's GUID. Pass it straight to
[Run a solver job](run-solver-job.md).

!!! note "Unofficial endpoints"
    [`get_upload_url`](../reference/unofficial.md#method-unofficial-get_upload_url),
    [`upload_to_presigned_url`](../reference/unofficial.md#method-unofficial-upload_to_presigned_url),
    and
    [`create_scenario_from_excel_url`](../reference/unofficial.md#method-unofficial-create_scenario_from_excel_url)
    wrap endpoints that are **not part of the published REST spec**. They power the web
    app's Excel import and are stable in practice, but may change without a version bump.

## Shortcut (sync client only)

The `workflows` module collapses the three calls into one. It reads the file, uploads it,
and creates the scenario:

```python
from sympheny_toolbox import Sympheny, workflows

with Sympheny("you@example.com", "password") as client:
    scenario_guid = workflows.create_scenario_from_excel(
        client, "scenario.xlsx", "Scenario from Excel", analysis_guid
    )
```

This helper is built on the synchronous client and has no async twin; on the async client,
use the three calls above.

## What to read next

- [Run a solver job](run-solver-job.md): optimize the scenario you just created.
- [Scenarios reference](../reference/scenarios.md): inspect, rename, copy, or delete the
  scenario.
- [Step-by-step guide](../../web-app/step-by-step-guide/index.md): what each
  workbook sheet corresponds to in the scenario editor.
