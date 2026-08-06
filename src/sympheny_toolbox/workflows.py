"""High-level Sympheny workflows built on top of the synchronous client.

These helpers combine multiple API calls into common automation flows (lookups by
name, execution with polling, result download, ...). They operate on a
[Sympheny][sympheny_toolbox._sync.client.Sympheny] client instance and are synchronous only.
"""

from __future__ import annotations

import io
import logging
import time
import zipfile
from typing import TYPE_CHECKING, Any, TypeVar
from urllib.parse import quote, urlencode

import httpx

from sympheny_toolbox import excel
from sympheny_toolbox.errors import SymphenyError
from sympheny_toolbox.models import (
    AnalysisResponseDto,
    GetSolverJobExt,
    JobStatus,
    ObjectiveFunction,
    PostSolverJobExt,
    ProjectDetailResponseDto,
    ScenarioResponseDto,
    TemporalResolution,
)


if TYPE_CHECKING:
    from collections.abc import Callable
    from uuid import UUID

    from sympheny_toolbox import Sympheny

logger = logging.getLogger(__name__)

T = TypeVar("T")

INPUT_FILE_SHEETS = [
    "Stages",
    "Hubs",
    "Energy Carriers",
    "Imports",
    "Exports",
    "On-site Resources",
    "Demands",
    "Conversion Techs",
    "Conversion Tech Modes",
    "Storage Techs",
    "Network Techs",
    "Network Links",
]

_DOWNLOAD_TIMEOUT_SEC = 60.0
_DOWNLOAD_RETRIES = 3
_DOWNLOAD_RETRY_BACKOFF_SEC = 1.0


def _download(url: str) -> bytes:
    for attempt in range(_DOWNLOAD_RETRIES):
        try:
            response = httpx.get(url, timeout=_DOWNLOAD_TIMEOUT_SEC)
            response.raise_for_status()
            return response.content
        except httpx.HTTPError:
            if attempt == _DOWNLOAD_RETRIES - 1:
                raise
            time.sleep(_DOWNLOAD_RETRY_BACKOFF_SEC)
    raise AssertionError("unreachable")  # pragma: no cover


def _app_domain(client: Sympheny) -> str:
    return "app.dev.sympheny.com" if client.is_dev else "app.sympheny.com"


# -- lookups by name ---------------------------------------------------------


def find_project(client: Sympheny, project_name: str) -> ProjectDetailResponseDto | None:
    """Find a project by name and return its details, or ``None`` if not found."""
    for project in client.projects.list():
        if project.project_name == project_name and project.project_guid is not None:
            return client.projects.get(project.project_guid)
    return None


def find_analysis(client: Sympheny, analysis_name: str, project_guid: str) -> AnalysisResponseDto | None:
    """Find an analysis by name within a project, or ``None`` if not found."""
    return next((a for a in client.analyses.list(project_guid) if a.analysis_name == analysis_name), None)


def find_scenario(client: Sympheny, scenario_name: str, analysis_guid: str) -> ScenarioResponseDto | None:
    """Find a scenario by name within an analysis, or ``None`` if not found."""
    return next((s for s in client.scenarios.list(analysis_guid) if s.scenario_name == scenario_name), None)


def scenario_url(client: Sympheny, scenario_guid: str) -> str:
    """Return the Sympheny web app URL of a scenario."""
    scenario = client.scenarios.get(scenario_guid)
    return f"https://{_app_domain(client)}/projects/{scenario.project_guid}/analysis/{scenario.analysis_guid}/scenario/{scenario_guid}"


def dashboard_url(client: Sympheny, scenario_guid: str) -> str | None:
    """Return the results-dashboard URL of the first finished job of a scenario, or ``None``."""
    scenario = client.scenarios.get(scenario_guid)
    jobs = client.solver_jobs.list_for_scenarios([scenario_guid])
    done_jobs = [job for job in jobs if job.status is not None and job.status.value == "DONE"]
    if not done_jobs:
        return None

    url = f"https://{_app_domain(client)}/projects/{scenario.project_guid}/analysis/{scenario.analysis_guid}/execution/{done_jobs[0].id}/solution/1/general"
    hubs = client.hubs.list(scenario_guid)
    stages = client.stages.list(scenario_guid)
    if hubs and stages and hubs[0].hub_name and stages[0].name:
        url += "?" + urlencode({"hub": hubs[0].hub_name, "stage": stages[0].name}, quote_via=quote)
    return url


# -- execution ----------------------------------------------------------------


def build_solver_job_request(
    scenario_guid: str,
    *,
    scenario_name: str | None = None,
    job_name: str = "sympheny-toolbox job",
    objective1: ObjectiveFunction = ObjectiveFunction.min_life_cycle_cost,
    objective2: ObjectiveFunction | None = ObjectiveFunction.min_co2_emissions,
    temporal_resolution: TemporalResolution = TemporalResolution.low,
    points: int = 2,
    time_limit: int = 60,
    mip_gap: float = 1.0,
) -> PostSolverJobExt:
    """Build a solver-job request for a scenario.

    ``time_limit`` is the solver's processing budget in **minutes** (queue time excluded). Pass the
    resulting request(s) to [execute_scenarios][sympheny_toolbox.workflows.execute_scenarios].
    """
    # Built via model_validate with alias keys: type checkers disagree on the synthesized
    # __init__ parameter names of aliased fields (mypy plugin: field names; pyright/ty: aliases).
    return PostSolverJobExt.model_validate(
        {
            "name": job_name,
            "objective1": objective1,
            "objective2": objective2,
            "scenarioGuid": scenario_guid,
            "scenarioName": scenario_name,
            "temporalResolution": temporal_resolution,
            "points": points,
            "timeLimit": time_limit,
            "mipGap": mip_gap,
        }
    )


def execute_scenarios(
    client: Sympheny,
    requests: list[PostSolverJobExt],
    *,
    wait: bool = True,
    poll_interval_sec: float = 10.0,
) -> list[GetSolverJobExt]:
    """Submit solver jobs in a single request and, by default, wait until they all terminate.

    ``time_limit`` on each request is the solver's processing budget in **minutes** (queue time
    excluded); the server terminates a job once it is exceeded. When waiting, this helper does not
    impose its own wall-clock timeout, so jobs may sit queued for as long as needed.

    With ``wait=False`` the jobs are only submitted and the freshly queued jobs are returned,
    without polling. Returns the jobs in the same order as ``requests``. Raises
    [SymphenyError][sympheny_toolbox.errors.SymphenyError] if any scenario is infeasible.
    """
    submitted = client.solver_jobs.submit(requests)
    job_ids = [job.id for job in submitted]
    if not wait:
        logger.info("Submitted %d solver job(s) (not waiting for results)", len(job_ids))
        return [client.solver_jobs.get(job_id) for job_id in job_ids]

    results: list[GetSolverJobExt] = []
    for job_id in job_ids:
        job = _wait_for_termination(client, job_id, poll_interval_sec)
        if job.infeasibility_info:
            raise SymphenyError(f"Execution failed, scenario is infeasible: {job.infeasibility_info}")
        logger.info("Execution finished with status %s", job.status)
        results.append(job)
    return results


def _wait_for_termination(client: Sympheny, job_id: str | UUID, poll_interval_sec: float) -> GetSolverJobExt:
    last_status: JobStatus | None = None

    def fetch_terminated_job() -> GetSolverJobExt | None:
        nonlocal last_status
        job = client.solver_jobs.get(job_id)
        if job.status != last_status:
            logger.info("Solver job %s status: %s", job_id, job.status)
            last_status = job.status
        return job if job.terminated else None

    return wait_until(fetch_terminated_job, wait_sec=poll_interval_sec, timeout_sec=None)


def execute_scenario(
    client: Sympheny,
    scenario_guid: str,
    *,
    job_name: str = "sympheny-toolbox job",
    objective1: ObjectiveFunction = ObjectiveFunction.min_life_cycle_cost,
    objective2: ObjectiveFunction | None = ObjectiveFunction.min_co2_emissions,
    temporal_resolution: TemporalResolution = TemporalResolution.low,
    points: int = 2,
    time_limit: int = 60,
    mip_gap: float = 1.0,
    poll_interval_sec: float = 10.0,
) -> GetSolverJobExt:
    """Submit a solver job for a single scenario and wait until it terminates.

    Convenience wrapper over [build_solver_job_request][sympheny_toolbox.workflows.build_solver_job_request]
    + [execute_scenarios][sympheny_toolbox.workflows.execute_scenarios] for the common single-scenario
    case. Returns the terminated job; raises [SymphenyError][sympheny_toolbox.errors.SymphenyError] if
    the scenario is infeasible.
    """
    scenario = client.scenarios.get(scenario_guid)
    request = build_solver_job_request(
        scenario_guid,
        scenario_name=scenario.scenario_name,
        job_name=job_name,
        objective1=objective1,
        objective2=objective2,
        temporal_resolution=temporal_resolution,
        points=points,
        time_limit=time_limit,
        mip_gap=mip_gap,
    )
    return execute_scenarios(client, [request], poll_interval_sec=poll_interval_sec)[0]


def get_input_file_dict(client: Sympheny, job_id: str | UUID) -> dict[str, list[dict[str, Any]]]:
    """Download the input Excel file of a solver job as ``{sheet: [row dicts]}``."""
    job = client.solver_jobs.get(job_id)
    if job.input_file is None:
        raise SymphenyError(f"Solver job {job_id} has no input file")
    return excel.read_records(_download(str(job.input_file.root)), INPUT_FILE_SHEETS)


def get_output_file_dict(client: Sympheny, job_id: str | UUID, solution_num: int) -> dict[str, Any]:
    """Download the result zip of a solver job and read one solution's Excel file.

    Returns the ``Cost & CO2`` sheet as records plus every ``Mode *`` profile sheet.
    """
    job = client.solver_jobs.get(job_id)
    if job.output_file is None:
        raise SymphenyError(f"Solver job {job_id} has no output file")

    with zipfile.ZipFile(io.BytesIO(_download(str(job.output_file.root)))) as archive:
        target = next((n for n in archive.namelist() if n.startswith(f"Solution {solution_num}") and n.endswith(".xlsx")), None)
        if target is None:
            raise SymphenyError(f"No Excel file for solution {solution_num} in the result zip of job {job_id}")
        content = archive.read(target)

    result: dict[str, Any] = excel.read_records(content, ["Cost & CO2"])
    mode_sheets = [name for name in excel.sheet_names(content) if name.startswith("Mode ")]
    result.update(excel.read_profile_sheets(content, mode_sheets))
    return result


# -- polling -----------------------------------------------------------------------


def wait_until(fetch: Callable[[], T | None], *, wait_sec: float = 5.0, timeout_sec: float | None = 500.0) -> T:
    """Poll ``fetch`` until it returns a non-``None`` result.

    Raises [TimeoutError][] if ``timeout_sec`` elapses first. Pass ``timeout_sec=None``
    to poll indefinitely (no deadline).
    """
    deadline = None if timeout_sec is None else time.monotonic() + timeout_sec
    while True:
        result = fetch()
        if result is not None:
            return result
        if deadline is not None and time.monotonic() >= deadline:
            raise TimeoutError(f"Background job did not complete within {timeout_sec} seconds")
        logger.debug("Not done yet, sleeping %s sec", wait_sec)
        time.sleep(wait_sec)
