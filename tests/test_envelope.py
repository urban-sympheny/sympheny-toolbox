"""Tests for envelope unwrapping and request-model serialization."""

from __future__ import annotations

import pytest

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.errors import UnexpectedResponseError
from sympheny_toolbox.models import PostSolverJobExt, ScenarioResponseDto, Status


def test_unwrap_returns_payload() -> None:
    scenario = ScenarioResponseDto(scenario_guid="scn-1")
    assert unwrap(scenario) is scenario


def test_unwrap_raises_on_missing_data() -> None:
    with pytest.raises(UnexpectedResponseError, match="'data' payload"):
        unwrap(None)


def test_dump_uses_camel_case_aliases_and_drops_none() -> None:
    job = PostSolverJobExt.model_validate(
        {
            "name": "job",
            "objective1": "MIN_LIFE_CYCLE_COST",
            "scenarioGuid": "scn-1",
            "temporalResolution": "LOW",
            "points": 2,
            "timeLimit": 3,
            "mipGap": 1.0,
        }
    )

    payload = dump(job)

    assert payload["scenarioGuid"] == "scn-1"
    assert payload["temporalResolution"] == "LOW"
    assert payload["timeLimit"] == 3
    assert "scenario_guid" not in payload
    assert "objective2" not in payload  # None values are excluded
    assert "scenarioName" not in payload


def test_dump_is_json_compatible() -> None:
    payload = dump(Status(code="200", desc="OK"))
    assert payload == {"code": "200", "desc": "OK"}
