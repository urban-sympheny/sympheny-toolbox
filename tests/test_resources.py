"""Tests for typed resource endpoints: paths, request serialization, envelope handling."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from sympheny_toolbox.errors import UnexpectedResponseError
from sympheny_toolbox.models import GetScenarioGuidsPage, JobStatus, ProjectRequestDto, ScenarioRequestDto, Status, Version


if TYPE_CHECKING:
    from sympheny_toolbox import Sympheny

    from .conftest import MockAPI


JOB_ID = "0b7e894e-15e6-4c9f-a692-3c9ac60566ba"

SOLVER_JOB = {
    "status": "DONE",
    "statusMsg": "Done",
    "terminated": "2026-01-01T01:00:00Z",
    "name": "test job",
    "objective1": "MIN_LIFE_CYCLE_COST",
    "objective2": "MIN_CO2_EMISSIONS",
    "scenarioGuid": "scn-1",
    "scenarioName": "Test scenario",
    "temporalResolution": "LOW",
    "points": 2,
    "timeLimit": 3,
    "mipGap": 1.0,
    "accountGuid": "acc-1",
    "organizationId": "6a5f0e8e-9c1d-4f0a-8c9a-111111111111",
    "subscriptionId": "6a5f0e8e-9c1d-4f0a-8c9a-222222222222",
    "id": JOB_ID,
    "created": "2026-01-01T00:00:00Z",
}


def test_projects_list_unwraps_nested_envelope(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/projects", {"data": {"projects": [{"projectName": "P1", "projectGuid": "prj-1"}]}, "status": {"code": "200"}})

    projects = client.projects.list()

    assert api.last_request.method == "GET"
    assert [project.project_name for project in projects] == ["P1"]


def test_projects_list_returns_empty_list_when_projects_missing(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/projects", {"data": {}, "status": {"code": "200"}})

    assert client.projects.list() == []


def test_missing_data_payload_raises_unexpected_response(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/projects", {"status": {"code": "200"}})

    with pytest.raises(UnexpectedResponseError):
        client.projects.list()


def test_analyses_list_unwraps_paged_envelope(client: Sympheny, api: MockAPI) -> None:
    api.add(
        "GET",
        "/sympheny-app/projects/prj-1/analyses",
        {"data": [{"analysisGuid": "ana-1", "analysisName": "A1"}], "totalElements": 1, "hasNext": False},
    )

    analyses = client.analyses.list("prj-1")

    assert [analysis.analysis_guid for analysis in analyses] == ["ana-1"]


def test_analyses_delete_tolerates_missing_data_payload(client: Sympheny, api: MockAPI) -> None:
    # The live API returns `data: null` for this endpoint even on a successful delete.
    api.add("DELETE", "/sympheny-app/analysis/ana-1", {"data": None})

    status = client.analyses.delete("ana-1")

    assert status == Status()


def test_scenarios_copy_sends_query_params(client: Sympheny, api: MockAPI) -> None:
    api.add("PUT", "/sympheny-app/scenarios/copy/scn-1", {"data": {"scenarioGuid": "scn-2", "scenarioName": "Copy"}})

    copy = client.scenarios.copy("scn-1", analysis_destination_guid="ana-2", name="Copy")

    assert copy.scenario_guid == "scn-2"
    params = dict(api.last_request.url.params)
    assert params == {"analysisDestinationGuid": "ana-2", "name": "Copy"}


def test_scenarios_rename_sends_body(client: Sympheny, api: MockAPI) -> None:
    api.add("PUT", "/sympheny-app/scenarios/scn-1", {"data": {"scenarioGuid": "scn-1", "scenarioName": "New"}})

    renamed = client.scenarios.rename("scn-1", ScenarioRequestDto(scenario_name="New"))

    assert renamed.scenario_name == "New"
    assert api.last_json == {"scenarioName": "New"}


def test_scenarios_delete_tolerates_missing_data_payload(client: Sympheny, api: MockAPI) -> None:
    # The live API returns `data: null` for this endpoint even on a successful delete.
    api.add("DELETE", "/sympheny-app/scenario/scn-1", {"data": None})

    assert client.scenarios.delete("scn-1") == Status()


def test_solver_jobs_list_for_scenarios_sends_aliased_body(client: Sympheny, api: MockAPI) -> None:
    api.add("POST", "/sense-api/ext/solver/jobs/get-scenarios", [SOLVER_JOB])

    jobs = client.solver_jobs.list_for_scenarios(["scn-1"], limit=50)

    assert api.last_json == {"scenarioGuids": ["scn-1"], "limit": 50}
    assert jobs[0].status is JobStatus.done
    assert jobs[0].scenario_guid == "scn-1"


def test_solver_jobs_list_for_scenarios_filters_by_status(client: Sympheny, api: MockAPI) -> None:
    running_job = SOLVER_JOB | {"status": "RUNNING", "statusMsg": "Running", "terminated": None}
    api.add("POST", "/sense-api/ext/solver/jobs/get-scenarios", [SOLVER_JOB, running_job])

    jobs = client.solver_jobs.list_for_scenarios(["scn-1"], status=JobStatus.done)

    assert [job.status for job in jobs] == [JobStatus.done]


def test_projects_create_rejects_non_v2(client: Sympheny, api: MockAPI) -> None:
    with pytest.raises(ValueError, match="V2"):
        client.projects.create(ProjectRequestDto(project_name="P1", version=Version.v1))


def test_energy_carriers_list_parses_models(client: Sympheny, api: MockAPI) -> None:
    carrier = {
        "energyCarrierGuid": "ec-1",
        "typeKey": "ELECTRICITY",
        "typeDisplayName": "Electricity",
        "subtypeKey": "GRID",
        "subtypeDisplayName": "Grid",
        "energyCarrierName": "Electricity",
        "colorHexCode": "#ffcc00",
        "customOutputEfficiencyActivated": False,
        "customInputEfficiencyActivated": False,
        "created": "2026-01-01T00:00:00Z",
    }
    api.add("GET", "/sympheny-app/scenarios/scn-1/carriers", {"data": {"energyCarriers": [carrier]}})

    result = client.energy_carriers.list("scn-1")

    assert api.last_request.method == "GET"
    assert result.energy_carriers is not None
    assert result.energy_carriers[0].energy_carrier_guid == "ec-1"
    assert result.energy_carriers[0].energy_carrier_name == "Electricity"


def test_solver_jobs_get_parses_file_urls(client: Sympheny, api: MockAPI) -> None:
    api.add(
        "GET",
        f"/sense-api/ext/solver/jobs/{JOB_ID}",
        SOLVER_JOB | {"inputFile": "https://files.test/input.xlsx", "outputFile": "https://files.test/output.zip"},
    )

    job = client.solver_jobs.get(JOB_ID)

    assert job.input_file is not None
    assert str(job.input_file.root) == "https://files.test/input.xlsx"
    assert job.output_file is not None
    assert str(job.output_file.root) == "https://files.test/output.zip"


def test_get_scenario_guids_page_default_limit() -> None:
    request = GetScenarioGuidsPage.model_validate({"scenarioGuids": ["scn-1"]})
    assert request.limit == 200
