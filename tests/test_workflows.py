"""Tests for the high-level workflows (submit + poll, lookups, result files)."""

from __future__ import annotations

import io
import json
import zipfile
from typing import TYPE_CHECKING, Any

import pytest
from openpyxl import Workbook

from sympheny_toolbox import workflows
from sympheny_toolbox.errors import SymphenyError
from sympheny_toolbox.models import JobStatus

from .test_resources import JOB_ID, SOLVER_JOB


if TYPE_CHECKING:
    from sympheny_toolbox import Sympheny

    from .conftest import MockAPI

SCENARIO_BODY = {
    "data": {
        "scenarioGuid": "scn-1",
        "scenarioName": "Test scenario",
        "projectGuid": "prj-1",
        "analysisGuid": "ana-1",
    }
}
RUNNING_JOB = {key: value for key, value in SOLVER_JOB.items() if key != "terminated"} | {"status": "RUNNING", "statusMsg": "Running"}


# -- execution -----------------------------------------------------------------


def test_execute_scenario_submits_and_polls_until_terminated(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/scenario/scn-1", SCENARIO_BODY)
    api.add("POST", "/sense-api/ext/solver/jobs", [RUNNING_JOB])
    api.add("GET", f"/sense-api/ext/solver/jobs/{JOB_ID}", RUNNING_JOB)  # first poll: still running
    api.add("GET", f"/sense-api/ext/solver/jobs/{JOB_ID}", SOLVER_JOB)  # second poll: terminated

    job = workflows.execute_scenario(client, "scn-1", job_name="my job", poll_interval_sec=0.0)

    assert job.status is JobStatus.done
    assert _submit_body(api) == [
        {
            "name": "my job",
            "objective1": "MIN_LIFE_CYCLE_COST",
            "objective2": "MIN_CO2_EMISSIONS",
            "scenarioGuid": "scn-1",
            "scenarioName": "Test scenario",
            "temporalResolution": "LOW",
            "points": 2,
            "timeLimit": 60,
            "mipGap": 1.0,
        }
    ]


def test_build_solver_job_request_uses_aliases_and_defaults() -> None:
    request = workflows.build_solver_job_request("scn-9", scenario_name="Nine", job_name="job", points=5)

    assert request.model_dump(by_alias=True, exclude_none=True) == {
        "name": "job",
        "objective1": "MIN_LIFE_CYCLE_COST",
        "objective2": "MIN_CO2_EMISSIONS",
        "scenarioGuid": "scn-9",
        "scenarioName": "Nine",
        "temporalResolution": "LOW",
        "points": 5,
        "timeLimit": 60,
        "mipGap": 1.0,
    }


def test_execute_scenarios_submits_batch_in_one_post_without_waiting(client: Sympheny, api: MockAPI) -> None:
    job_b = SOLVER_JOB | {"id": "11111111-1111-4111-8111-111111111111", "scenarioGuid": "scn-2"}
    api.add("POST", "/sense-api/ext/solver/jobs", [RUNNING_JOB, job_b])  # one submit returns both jobs
    api.add("GET", f"/sense-api/ext/solver/jobs/{JOB_ID}", RUNNING_JOB)
    api.add("GET", f"/sense-api/ext/solver/jobs/{job_b['id']}", job_b)

    requests = [workflows.build_solver_job_request("scn-1", scenario_name="One"), workflows.build_solver_job_request("scn-2", scenario_name="Two")]
    jobs = workflows.execute_scenarios(client, requests, wait=False)

    assert [job.scenario_guid for job in jobs] == ["scn-1", "scn-2"]
    assert sum(1 for r in api.requests if r.url.path == "/sense-api/ext/solver/jobs") == 1  # single batch POST
    assert len(_submit_body(api)) == 2


def _submit_body(api: MockAPI) -> Any:
    request = next(request for request in api.requests if request.url.path == "/sense-api/ext/solver/jobs")
    return json.loads(request.content)


def test_execute_scenario_raises_on_infeasibility(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/scenario/scn-1", SCENARIO_BODY)
    api.add("POST", "/sense-api/ext/solver/jobs", [RUNNING_JOB])
    api.add("GET", f"/sense-api/ext/solver/jobs/{JOB_ID}", SOLVER_JOB | {"status": "FAILED", "infeasibilityInfo": "Demand cannot be met"})

    with pytest.raises(SymphenyError, match="infeasible"):
        workflows.execute_scenario(client, "scn-1", poll_interval_sec=0.0)


# -- polling -------------------------------------------------------------------


def test_wait_until_returns_first_non_none_result() -> None:
    results = iter([None, None, "done"])

    assert workflows.wait_until(lambda: next(results), wait_sec=0.0, timeout_sec=10.0) == "done"


def test_wait_until_times_out() -> None:
    with pytest.raises(TimeoutError, match="did not complete"):
        workflows.wait_until(lambda: None, wait_sec=0.0, timeout_sec=0.0)


# -- lookups -------------------------------------------------------------------


def test_find_project_returns_details_of_match(client: Sympheny, api: MockAPI) -> None:
    api.add(
        "GET",
        "/sympheny-app/projects",
        {"data": {"projects": [{"projectName": "Other", "projectGuid": "prj-0"}, {"projectName": "Mine", "projectGuid": "prj-1"}]}},
    )
    api.add("GET", "/sympheny-app/projects/prj-1", {"data": {"projectName": "Mine", "projectGuid": "prj-1"}})

    project = workflows.find_project(client, "Mine")

    assert project is not None
    assert project.project_guid == "prj-1"


def test_find_project_returns_none_when_absent(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/projects", {"data": {"projects": [{"projectName": "Other", "projectGuid": "prj-0"}]}})

    assert workflows.find_project(client, "Mine") is None


def test_find_scenario_by_name(client: Sympheny, api: MockAPI) -> None:
    api.add(
        "GET",
        "/sympheny-app/analysis/ana-1/scenario",
        {"data": [{"scenarioGuid": "scn-1", "scenarioName": "Base"}, {"scenarioGuid": "scn-2", "scenarioName": "Variant"}]},
    )

    scenario = workflows.find_scenario(client, "Variant", "ana-1")

    assert scenario is not None
    assert scenario.scenario_guid == "scn-2"


def test_scenario_url(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/scenario/scn-1", SCENARIO_BODY)

    url = workflows.scenario_url(client, "scn-1")

    assert url == "https://app.sympheny.com/projects/prj-1/analysis/ana-1/scenario/scn-1"


def test_dashboard_url_of_first_done_job(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/scenario/scn-1", SCENARIO_BODY)
    api.add("POST", "/sense-api/ext/solver/jobs/get-scenarios", [SOLVER_JOB])
    api.add(
        "GET",
        "/sympheny-app/scenarios/scn-1/hubs",
        {"data": [{"hubGuid": "hub-1", "hubName": "Hub 1", "created": "2026-01-01T00:00:00Z", "updated": "2026-01-01T00:00:00Z"}]},
    )
    api.add("GET", "/sympheny-app/scenarios/scn-1/stages", {"data": [{"name": "Stage 1", "length": 20, "index": 0}]})

    url = workflows.dashboard_url(client, "scn-1")

    assert url == (f"https://app.sympheny.com/projects/prj-1/analysis/ana-1/execution/{JOB_ID}/solution/1/general?hub=Hub%201&stage=Stage%201")


def test_dashboard_url_returns_none_without_done_job(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", "/sympheny-app/scenario/scn-1", SCENARIO_BODY)
    api.add("POST", "/sense-api/ext/solver/jobs/get-scenarios", [RUNNING_JOB])

    assert workflows.dashboard_url(client, "scn-1") is None


# -- result files --------------------------------------------------------------


def _solution_zip() -> bytes:
    workbook = Workbook()
    cost_sheet = workbook.active
    assert cost_sheet is not None
    cost_sheet.title = "Cost & CO2"
    cost_sheet.append(["Metric", "Value"])
    cost_sheet.append(["Total cost", 1000.0])

    mode_sheet = workbook.create_sheet("Mode 1")
    mode_sheet.append(["Result profiles", None])
    mode_sheet.append(["Time step", "Gas boiler"])
    mode_sheet.append([1, 5.0])

    excel_buffer = io.BytesIO()
    workbook.save(excel_buffer)

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as archive:
        archive.writestr("Solution 1 - result.xlsx", excel_buffer.getvalue())
    return zip_buffer.getvalue()


def test_get_output_file_dict(client: Sympheny, api: MockAPI, monkeypatch: pytest.MonkeyPatch) -> None:
    api.add("GET", f"/sense-api/ext/solver/jobs/{JOB_ID}", SOLVER_JOB | {"outputFile": "https://files.test/output.zip"})
    monkeypatch.setattr(workflows, "_download", lambda url: _solution_zip())

    result = workflows.get_output_file_dict(client, JOB_ID, 1)

    assert result["Cost & CO2"] == [{"Metric": "Total cost", "Value": 1000.0}]
    assert result["Mode 1"] == {"Gas boiler": [5.0]}


def test_get_output_file_dict_raises_without_output_file(client: Sympheny, api: MockAPI) -> None:
    api.add("GET", f"/sense-api/ext/solver/jobs/{JOB_ID}", SOLVER_JOB)

    with pytest.raises(SymphenyError, match="no output file"):
        workflows.get_output_file_dict(client, JOB_ID, 1)


def test_get_output_file_dict_raises_when_solution_missing(client: Sympheny, api: MockAPI, monkeypatch: pytest.MonkeyPatch) -> None:
    api.add("GET", f"/sense-api/ext/solver/jobs/{JOB_ID}", SOLVER_JOB | {"outputFile": "https://files.test/output.zip"})
    monkeypatch.setattr(workflows, "_download", lambda url: _solution_zip())

    with pytest.raises(SymphenyError, match="No Excel file for solution 9"):
        workflows.get_output_file_dict(client, JOB_ID, 9)
