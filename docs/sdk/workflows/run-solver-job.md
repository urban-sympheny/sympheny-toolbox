---
tags:
  - sdk
  - workflow
---

# Run solver job

Submit a scenario to the Sympheny solver and wait for the optimization to finish. This
mirrors clicking **Execute** in the [web app](../../web-app/step-by-step-guide/execution.md),
but scripted end to end.

## Prerequisites

- A **scenario GUID** that is ready for execution, for example the one returned by
  [Create a scenario from Excel](create-scenario-from-excel.md), or an existing scenario's GUID.
- Solver quota on your subscription. Check it with
  [`client.solver_jobs.usage()`](../reference/solver_jobs.md#method-solver_jobs-usage).

## Build the request

A solver job is described by a
[`PostSolverJobExt`](../reference/models/solver.md#model-PostSolverJobExt). The request is
plain data, so you build it the same way whichever client you use:

```python
from sympheny_toolbox.models import ObjectiveFunction, PostSolverJobExt, TemporalResolution

request = PostSolverJobExt(
    name="Battery evaluation",
    objective1=ObjectiveFunction.min_life_cycle_cost,
    objective2=ObjectiveFunction.min_co2_emissions,
    scenario_guid="your-scenario-guid",
    temporal_resolution=TemporalResolution.low,
    points=2,
    time_limit=30,
    mip_gap=1.0,
)
```

- **`objective1` / `objective2`**: the optimization objectives (see
  [`ObjectiveFunction`](../reference/models/solver.md#model-ObjectiveFunction)). With two
  objectives the solver returns a Pareto front of `points` solutions.
- **`temporal_resolution`**: how aggressively the 8760-hour year is
  [clustered](../../web-app/concepts/clustered-profiles.md) before solving
  (`LOW`/`MEDIUM`/`HIGH`/`FULL`); lower is faster, coarser.
- **`mip_gap`**: the optimality gap, in percent, at which the solver stops.

!!! warning "`time_limit` is in minutes"
    `time_limit` is the solver's processing budget in **minutes** (queue time excluded),
    not seconds. The server terminates a job once it is exceeded.

## Submit and poll

Submit the request, then poll the job until it reaches a terminal status. `DONE` means the
optimization succeeded; `STOPPED`, `FAILED`, and `INVALID` are terminal failures.

=== "Async"

    ```python
    import asyncio

    from sympheny_toolbox import AsyncSympheny
    from sympheny_toolbox.models import JobStatus

    TERMINAL = {JobStatus.done, JobStatus.stopped, JobStatus.failed, JobStatus.invalid}


    async def main() -> None:
        async with AsyncSympheny("you@example.com", "password") as client:
            submitted = await client.solver_jobs.submit([request])
            job_id = submitted[0].id

            while True:
                job = await client.solver_jobs.get(job_id)
                print(job.status)
                if job.status in TERMINAL:
                    break
                await asyncio.sleep(10)

            if job.status is not JobStatus.done:
                raise RuntimeError(f"Job did not finish cleanly ({job.status}): {job.infeasibility_info}")
            print("finished job", job_id)


    asyncio.run(main())
    ```

=== "Sync"

    ```python
    import time

    from sympheny_toolbox import Sympheny
    from sympheny_toolbox.models import JobStatus

    TERMINAL = {JobStatus.done, JobStatus.stopped, JobStatus.failed, JobStatus.invalid}

    with Sympheny("you@example.com", "password") as client:
        submitted = client.solver_jobs.submit([request])
        job_id = submitted[0].id

        while True:
            job = client.solver_jobs.get(job_id)
            print(job.status)
            if job.status in TERMINAL:
                break
            time.sleep(10)

        if job.status is not JobStatus.done:
            raise RuntimeError(f"Job did not finish cleanly ({job.status}): {job.infeasibility_info}")
        print("finished job", job_id)
    ```

[`submit`](../reference/solver_jobs.md#method-solver_jobs-submit) takes a **list** of
requests and returns one [`SolverJob`](../reference/models/solver.md#model-SolverJob) per
request, so you can batch several scenarios in a single call and poll each `id`.

## Shortcut (sync client only)

`workflows.execute_scenario` builds the request, submits it, and polls to termination in
one call, raising if the scenario is infeasible:

```python
from sympheny_toolbox import Sympheny, workflows

with Sympheny("you@example.com", "password") as client:
    job = workflows.execute_scenario(client, "your-scenario-guid", time_limit=30)
    print(job.status)  # JobStatus.done
```

Use `workflows.execute_scenarios` to submit many at once. Both are built on the
synchronous client; on the async client, use the submit-and-poll loop above.

## What to read next

- [Download the results](download-results.md): read the result file of the finished job.
- [Solver jobs reference](../reference/solver_jobs.md): every method on
  `client.solver_jobs`, including `list_for_scenarios`, `stop`, and `delete`.
- [`POST /sense-api/ext/solver/jobs`](../../api/reference/solver-jobs.md#operation-post_solver_jobs_sense_api_ext_solver_jobs_post):
  the underlying REST operation.
