"""Operations on scenarios of the Sympheny platform API (``scenario-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ResponseDtoListFScenarioResponseDto,
    ResponseDtoScenarioResponseDto,
    ResponseDtoStatus,
    ScenarioRequestDto,
    ScenarioResponseDto,
    Status,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncScenarios:
    """Operations on scenarios (``scenario-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def list(self, analysis_guid: str) -> list[ScenarioResponseDto]:
        """List the scenarios of an analysis. ``GET /sympheny-app/analysis/{guid}/scenario``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/analysis/{analysis_guid}/scenario")
        envelope = ResponseDtoListFScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def create(self, analysis_guid: str, request: ScenarioRequestDto) -> ScenarioResponseDto:
        """Create a new scenario in an analysis. ``POST /sympheny-app/analysis/{guid}/scenario``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/analysis/{analysis_guid}/scenario", json=dump(request))
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, scenario_guid: str) -> ScenarioResponseDto:
        """Get scenario details. ``GET /sympheny-app/scenario/{scenarioGuid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenario/{scenario_guid}")
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def rename(self, scenario_guid: str, request: ScenarioRequestDto) -> ScenarioResponseDto:
        """Rename a scenario in place. ``PUT /sympheny-app/scenarios/{scenarioGuid}``

        Unlike [copy][sympheny_toolbox._async.scenarios.AsyncScenarios.copy], this sets the scenario's
        name directly, so it works within the scenario's current analysis without creating a duplicate.
        """
        raw = await self._t.request_json("PUT", f"/sympheny-app/scenarios/{scenario_guid}", json=dump(request))
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str) -> Status:
        """Delete a scenario. ``DELETE /sympheny-app/scenario/{scenarioGuid}``

        The API returns no ``data`` payload for this endpoint even on success, so a missing payload is
        treated as an empty [Status][sympheny_toolbox.models.Status] rather than an error.
        """
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenario/{scenario_guid}")
        envelope = ResponseDtoStatus.model_validate(raw)
        return envelope.data if envelope.data is not None else Status()

    async def copy(self, scenario_guid: str, *, analysis_destination_guid: str | None = None, name: str | None = None) -> ScenarioResponseDto:
        """Copy a scenario, optionally into another analysis. ``PUT /sympheny-app/scenarios/copy/{scenarioGuid}``

        With no ``analysis_destination_guid`` the copy stays in the source's analysis; ``name`` sets
        the copy's name in either case.
        """
        params: dict[str, str] = {}
        if analysis_destination_guid is not None:
            params["analysisDestinationGuid"] = analysis_destination_guid
        if name is not None:
            params["name"] = name
        raw = await self._t.request_json("PUT", f"/sympheny-app/scenarios/copy/{scenario_guid}", params=params or None)
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)
