"""High-level Sympheny workflows built on top of the synchronous client.

These helpers combine multiple API calls into common automation flows (scenario
creation from Excel, execution with polling, result download, ...). They operate
on a :class:`~sympheny_toolbox.Sympheny` client instance and are synchronous only.
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
    from pathlib import Path
    from uuid import UUID

    from sympheny_toolbox import Sympheny

logger = logging.getLogger(__name__)

T = TypeVar("T")

VARIANTS_SHEET = "Variants"
PROFILES_SHEET = "Profiles"

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

ENYMAP_TECH_OPTIONS = ["PV", "HEAT_PUMP", "GAS_BOILER", "CHILLER", "BATTERY", "HOT_WATER_STORAGE"]
ENYMAP_DEMAND_OPTIONS = ["HOT_WATER", "SPACE_HEATING", "ELECTRICITY", "COOLING"]
ENYMAP_IMPORT_OPTIONS = ["ELECTRICITY"]
ENYMAP_EXPORT_OPTIONS = ["HEAT_AMBIENT", "COOLING"]

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


# -- scenario creation from Excel ---------------------------------------------


def create_scenario_from_excel(client: Sympheny, excel_path: str | Path, scenario_name: str, analysis_guid: str) -> str:
    """Upload a scenario Excel file and create a scenario from it; returns the scenario GUID."""
    upload_url = client.unofficial.get_upload_url()
    with open(excel_path, "rb") as file:
        client.unofficial.upload_to_presigned_url(upload_url, file.read())
    return client.unofficial.create_scenario_from_excel_url(upload_url, scenario_name, analysis_guid)


def create_variants_from_excel(client: Sympheny, excel_path: str | Path, master_scenario_guid: str) -> Any:
    """Upload a variants Excel file and (re)create the scenario variants of a master scenario."""
    upload_url = client.unofficial.get_upload_url()
    with open(excel_path, "rb") as file:
        client.unofficial.upload_to_presigned_url(upload_url, file.read())
    return client.unofficial.create_variants_from_excel_url(upload_url, master_scenario_guid)


def create_variants_from_dict(client: Sympheny, variants: dict[str, Any] | list[dict[str, Any]], master_scenario_guid: str) -> Any:
    """Create scenario variants from in-memory data instead of an Excel file.

    ``variants`` is either a plain list of variant records, or a dict with keys
    ``"Variants"`` (list of records) and ``"Profiles"`` (mapping of profile name
    to 8760 hourly values).
    """
    if isinstance(variants, dict):
        content = excel.build_variants_workbook(variants[VARIANTS_SHEET], variants.get(PROFILES_SHEET) or None)
    else:
        content = excel.build_variants_workbook(variants)
    upload_url = client.unofficial.get_upload_url()
    client.unofficial.upload_to_presigned_url(upload_url, content)
    return client.unofficial.create_variants_from_excel_url(upload_url, master_scenario_guid)


def get_variants_dict(client: Sympheny, master_scenario_guid: str) -> dict[str, Any]:
    """Download the variants Excel of a master scenario as ``{"Variants": [...], "Profiles": {...}}``."""
    content = _download(client.unofficial.get_variants_excel_url(master_scenario_guid))
    variants = excel.read_records(content, [VARIANTS_SHEET])[VARIANTS_SHEET]
    profiles: dict[str, list[float]] = {}
    if PROFILES_SHEET in excel.sheet_names(content):
        profiles = excel.read_profile_input_sheet(content, PROFILES_SHEET)
    return {VARIANTS_SHEET: variants, PROFILES_SHEET: profiles}


# -- execution ----------------------------------------------------------------


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
    """Submit a solver job for a scenario and wait until it terminates.

    ``time_limit`` is the solver's processing budget in **minutes** (queue time excluded);
    the server terminates the job once it is exceeded. This helper does not impose its own
    wall-clock timeout, so a job may sit queued for as long as needed; it polls until the
    server terminates the job.

    Returns the terminated job. Raises :class:`~sympheny_toolbox.errors.SymphenyError`
    if the scenario is infeasible.
    """
    scenario = client.scenarios.get(scenario_guid)
    # Built via model_validate with alias keys: type checkers disagree on the synthesized
    # __init__ parameter names of aliased fields (mypy plugin: field names; pyright/ty: aliases).
    job_request = PostSolverJobExt.model_validate(
        {
            "name": job_name,
            "objective1": objective1,
            "objective2": objective2,
            "scenarioGuid": scenario_guid,
            "scenarioName": scenario.scenario_name,
            "temporalResolution": temporal_resolution,
            "points": points,
            "timeLimit": time_limit,
            "mipGap": mip_gap,
        }
    )
    response = client.solver_jobs.submit([job_request])
    job_id = response[0].id

    last_status: JobStatus | None = None

    def fetch_terminated_job() -> GetSolverJobExt | None:
        nonlocal last_status
        job = client.solver_jobs.get(job_id)
        if job.status != last_status:
            logger.info("Solver job status: %s", job.status)
            last_status = job.status
        if not job.terminated:
            return None
        return job

    job = wait_until(fetch_terminated_job, wait_sec=poll_interval_sec, timeout_sec=None)
    if job.infeasibility_info:
        raise SymphenyError(f"Execution failed, scenario is infeasible: {job.infeasibility_info}")
    logger.info("Execution finished with status %s", job.status)
    return job


def generate_input_file(client: Sympheny, scenario_guid: str, *, poll_interval_sec: float = 5.0, timeout_sec: float = 100.0) -> str:
    """Trigger input-file generation for a scenario and return the file URL once available."""
    client.unofficial.generate_specs([scenario_guid])
    scenario = client.scenarios.get(scenario_guid)

    def fetch_input_filepath() -> str | None:
        analysis = client.unofficial.get_analysis(str(scenario.analysis_guid))
        results = analysis["results"]["scenarios"]
        result = next((s for s in results if s["scenarioName"] == scenario.scenario_name), None)
        return result["inputFilepath"] if result and result["inputFilepath"] else None

    return wait_until(fetch_input_filepath, wait_sec=poll_interval_sec, timeout_sec=timeout_sec)


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


# -- enymap ---------------------------------------------------------------------


def create_enymap_scenario(
    client: Sympheny,
    scenario_name: str,
    analysis_guid: str,
    techs: list[str],
    demands: list[str],
    imports: list[str],
    exports: list[str],
    polygon: list[Any],
    *,
    poll_interval_sec: float = 5.0,
    timeout_sec: float = 500.0,
) -> str:
    """Create an enymap scenario with GIS hub, demands, and solar resources; returns the scenario GUID."""
    for values, options in [
        (techs, ENYMAP_TECH_OPTIONS),
        (demands, ENYMAP_DEMAND_OPTIONS),
        (imports, ENYMAP_IMPORT_OPTIONS),
        (exports, ENYMAP_EXPORT_OPTIONS),
    ]:
        _validate_choices(values, options)

    payload = {
        "scenarioName": scenario_name,
        "length": 4,
        "interestRate": 8.4,
        "exchangeCurrency": "CHF",
        "exchangeRate": 1.6,
        "scope": "REGIONAL_NATIONAL",
        "technologies": techs,
        "demands": demands,
        "imports": imports,
        "exports": exports,
    }
    scenario_guid = str(client.unofficial.create_scenario_enymap(analysis_guid, payload)["scenarioGuid"])

    client.unofficial.create_gis_hub(scenario_guid, polygon)

    def gis_hub_ready() -> bool | None:
        jobs = client.unofficial.gis_background_jobs()
        return True if jobs and jobs[0]["is_done"] else None

    wait_until(gis_hub_ready, wait_sec=poll_interval_sec, timeout_sec=timeout_sec)
    client.unofficial.create_demand_solar(scenario_guid)
    client.unofficial.generate_scenario_specs(scenario_guid)
    return scenario_guid


def _validate_choices(values: list[str], options: list[str]) -> None:
    if len(set(values)) != len(values):
        raise ValueError(f"Duplicate values in: {values}")
    invalid = set(values) - set(options)
    if invalid:
        raise ValueError(f"Invalid values found: {invalid}. Acceptable values are: {options}")


# -- demand profiles --------------------------------------------------------------


def get_demand_profile(client: Sympheny, demand_type: str, building_type: str, construction_end: int, building_area_m2: float) -> list[float]:
    """Estimate a building's hourly demand profile (8760 values) from the Sympheny demand database."""
    estimates = client.unofficial.hub_demand(
        demand_type,
        building_type,
        [{"construction_end": construction_end, "building_ground_area": building_area_m2, "nbr_floor": 1}],
    )
    total_demand = estimates[0]["totalAnnualDemand"]
    demand_guid = estimates[0]["energyDemandMetadataGuid"]
    profile = client.unofficial.get_database_demand_profile(demand_guid)
    return [entry["demandValue"] * total_demand for entry in profile]


# -- polling -----------------------------------------------------------------------


def wait_until(fetch: Callable[[], T | None], *, wait_sec: float = 5.0, timeout_sec: float | None = 500.0) -> T:
    """Poll ``fetch`` until it returns a non-``None`` result.

    Raises :class:`TimeoutError` if ``timeout_sec`` elapses first. Pass ``timeout_sec=None``
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
