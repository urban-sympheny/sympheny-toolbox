---
tags:
  - sdk
  - workflow
---

# Download results

Fetch the result file of a finished solver job, or link straight to its results dashboard
in the [web app](../../web-app/step-by-step-guide/results-dashboard.md).

## Prerequisites

- The **job id** of a finished job, the one returned by
  [Run a solver job](run-solver-job.md). If you only have a scenario GUID, list its jobs
  with
  [`client.solver_jobs.list_for_scenarios([scenario_guid])`](../reference/solver_jobs.md#method-solver_jobs-list_for_scenarios).

## Get the result file URL

A finished job carries an `output_file`: a presigned URL to a zip of result workbooks,
one Excel file per Pareto solution. It is only populated once the job's status is `DONE`.

=== "Async"

    ```python
    import asyncio

    from sympheny_toolbox import AsyncSympheny
    from sympheny_toolbox.models import JobStatus


    async def main() -> None:
        job_id = "your-job-id"
        async with AsyncSympheny("you@example.com", "password") as client:
            job = await client.solver_jobs.get(job_id)
            if job.status is not JobStatus.done or job.output_file is None:
                raise RuntimeError(f"No results available (status {job.status})")
            print(str(job.output_file.root))  # presigned URL to the results zip


    asyncio.run(main())
    ```

=== "Sync"

    ```python
    from sympheny_toolbox import Sympheny
    from sympheny_toolbox.models import JobStatus

    job_id = "your-job-id"
    with Sympheny("you@example.com", "password") as client:
        job = client.solver_jobs.get(job_id)
        if job.status is not JobStatus.done or job.output_file is None:
            raise RuntimeError(f"No results available (status {job.status})")
        print(str(job.output_file.root))  # presigned URL to the results zip
    ```

With the URL in hand you can download the zip with any HTTP client and open the workbooks
yourself, or use the helper below to parse them for you.

## Read a solution (sync client only)

`workflows.get_output_file_dict` downloads the zip, opens one solution's workbook, and
returns its `Cost & CO2` summary plus every `Mode *` profile sheet as plain Python data:

```python
from sympheny_toolbox import Sympheny, workflows

with Sympheny("you@example.com", "password") as client:
    result = workflows.get_output_file_dict(client, "your-job-id", solution_num=1)
    print(result["Cost & CO2"])
```

## Link to the dashboard instead

To send someone to the interactive results dashboard rather than the raw file,
`workflows.dashboard_url` returns the web-app URL of a scenario's first finished job:

```python
from sympheny_toolbox import Sympheny, workflows

with Sympheny("you@example.com", "password") as client:
    print(workflows.dashboard_url(client, "your-scenario-guid"))
```

Both helpers are built on the synchronous client and have no async twin.

## What to read next

- [Results dashboard](../../web-app/step-by-step-guide/results-dashboard.md): how to read a results
  dashboard in the web app.
- [Solver jobs reference](../reference/solver_jobs.md): the full
  [`GetSolverJobExt`](../reference/models/solver.md#model-GetSolverJobExt) a job returns.
- [`GET /sense-api/ext/solver/jobs/{id}`](../../api/reference/solver-jobs.md#operation-get_solver_job_sense_api_ext_solver_jobs__id__get):
  the underlying REST operation.
