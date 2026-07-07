<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/solver.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Solver jobs

Operations on solver jobs. Available on the client as `client.solver_jobs`.

## solver_jobs.submit { #method-solver_jobs-submit }

```python
async def submit(jobs: list[PostSolverJobExt]) -> list[SolverJob]
```

Submit one or more solver jobs for execution.

REST operation: [`POST /sense-api/ext/solver/jobs`](../../api/reference/solver-jobs.md#operation-post_solver_jobs_sense_api_ext_solver_jobs_post)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jobs` | list of [`PostSolverJobExt`](models/solver.md#model-PostSolverJobExt) | yes | Jobs to submit. |

**Returns:** list of [`SolverJob`](models/solver.md#model-SolverJob)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        submitted = await client.solver_jobs.submit(jobs)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        submitted = client.solver_jobs.submit(jobs)
    ```

## solver_jobs.list_for_scenarios { #method-solver_jobs-list_for_scenarios }

```python
async def list_for_scenarios(
    scenario_guids: list[str],
    *,
    limit: int = 200,
    status: JobStatus | None = None,
) -> list[SolverJob]
```

List solver jobs for the given scenarios, optionally filtered by status.

REST operation: [`POST /sense-api/ext/solver/jobs/get-scenarios`](../../api/reference/solver-jobs.md#operation-post_get_scenario_jobs_sense_api_ext_solver_jobs_get_scenarios_post)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guids` | list of `str` | yes | GUIDs of the scenarios to list jobs for. |
| `limit` | `int` | no | Maximum number of jobs to return. Defaults to `200`. |
| `status` | [`JobStatus`](models/solver.md#model-JobStatus), optional | no | Return only jobs with this status (filtered client-side). |

**Returns:** list of [`SolverJob`](models/solver.md#model-SolverJob)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        jobs = await client.solver_jobs.list_for_scenarios(scenario_guids)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        jobs = client.solver_jobs.list_for_scenarios(scenario_guids)
    ```

## solver_jobs.usage { #method-solver_jobs-usage }

```python
async def usage() -> GetUsageExt
```

Get solver usage of the current subscription and user.

REST operation: [`GET /sense-api/ext/solver/jobs/usage`](../../api/reference/solver-jobs.md#operation-get_solver_jobs_usage_sense_api_ext_solver_jobs_usage_get)

**Returns:** [`GetUsageExt`](models/solver.md#model-GetUsageExt)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        usage = await client.solver_jobs.usage()
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        usage = client.solver_jobs.usage()
    ```

## solver_jobs.get { #method-solver_jobs-get }

```python
async def get(job_id: str | UUID) -> GetSolverJobExt
```

Get a solver job by id.

REST operation: [`GET /sense-api/ext/solver/jobs/{id}`](../../api/reference/solver-jobs.md#operation-get_solver_job_sense_api_ext_solver_jobs__id__get)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `job_id` | `str` or `UUID` | yes | Solver job id. |

**Returns:** [`GetSolverJobExt`](models/solver.md#model-GetSolverJobExt)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        job = await client.solver_jobs.get(job_id)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        job = client.solver_jobs.get(job_id)
    ```

## solver_jobs.delete { #method-solver_jobs-delete }

```python
async def delete(job_id: str | UUID) -> str
```

Delete a solver job.

REST operation: [`DELETE /sense-api/ext/solver/jobs/{id}`](../../api/reference/solver-jobs.md#operation-delete_solver_job_sense_api_ext_solver_jobs__id__delete)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `job_id` | `str` or `UUID` | yes | Solver job id. |

**Returns:** `str`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        result = await client.solver_jobs.delete(job_id)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        result = client.solver_jobs.delete(job_id)
    ```

## solver_jobs.stop { #method-solver_jobs-stop }

```python
async def stop(job_id: str | UUID) -> str
```

Stop a running solver job.

REST operation: [`PUT /sense-api/ext/solver/jobs/{id}/stop`](../../api/reference/solver-jobs.md#operation-stop_job_sense_api_ext_solver_jobs__id__stop_put)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `job_id` | `str` or `UUID` | yes | Solver job id. |

**Returns:** `str`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        result = await client.solver_jobs.stop(job_id)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        result = client.solver_jobs.stop(job_id)
    ```
