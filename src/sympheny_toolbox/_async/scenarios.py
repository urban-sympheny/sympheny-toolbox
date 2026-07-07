"""Scenario, stage, and hub endpoints of the Sympheny platform API."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    HubRequestDto,
    HubResponseDto,
    ResponseDtoHubResponseDto,
    ResponseDtoListFHubResponseDto,
    ResponseDtoListFScenarioResponseDto,
    ResponseDtoListHubResponseDto,
    ResponseDtoListStageResponseDto,
    ResponseDtoScenarioResponseDto,
    ResponseDtoStageResponseDto,
    ResponseDtoStatus,
    ScenarioRequestDto,
    ScenarioResponseDto,
    StageRequestDto,
    StageResponseDto,
    Status,
)


if TYPE_CHECKING:
    import builtins

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

        Broken as of this writing (to be fixed server-side): the ``name`` argument is only applied when
        ``analysis_destination_guid`` is omitted (the copy stays in the source's analysis). When a
        destination *is* given, ``name`` is ignored and the copy takes the source's name *without*
        deduplicating, so copying the same source into one analysis twice fails the
        ``scenario_name + analysis_id`` unique constraint. To place a renamed copy in another analysis:
        copy into it without a name (the server assigns a unique "... (Copy)" name), then copy that in
        place with the wanted name.
        """
        params: dict[str, str] = {}
        if analysis_destination_guid is not None:
            params["analysisDestinationGuid"] = analysis_destination_guid
        if name is not None:
            params["name"] = name
        raw = await self._t.request_json("PUT", f"/sympheny-app/scenarios/copy/{scenario_guid}", params=params or None)
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)


class AsyncStages:
    """Operations on stages (``stage-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def list(self, scenario_guid: str) -> list[StageResponseDto]:
        """List the stages of a scenario. ``GET /sympheny-app/scenarios/{scenarioGuid}/stages``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/{scenario_guid}/stages")
        envelope = ResponseDtoListStageResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def create(self, scenario_guid: str, request: StageRequestDto) -> StageResponseDto:
        """Create a new stage in a scenario. ``POST /sympheny-app/scenarios/{scenarioGuid}/stages``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/scenarios/{scenario_guid}/stages", json=dump(request))
        envelope = ResponseDtoStageResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, stage_guid: str) -> StageResponseDto:
        """Get stage details. ``GET /sympheny-app/scenarios/stages/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/stages/{stage_guid}")
        envelope = ResponseDtoStageResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, scenario_guid: str, stage_guid: str, request: StageResponseDto) -> StageResponseDto:
        """Update a stage. ``PUT /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/scenarios/{scenario_guid}/stages/{stage_guid}", json=dump(request))
        envelope = ResponseDtoStageResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str, stage_guid: str) -> None:
        """Delete a stage. ``DELETE /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}``"""
        await self._t.request_json("DELETE", f"/sympheny-app/scenarios/{scenario_guid}/stages/{stage_guid}")


class AsyncHubs:
    """Operations on hubs (``hub-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def list(self, scenario_guid: str) -> list[HubResponseDto]:
        """List the hubs of a scenario. ``GET /sympheny-app/scenarios/{scenarioGuid}/hubs``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/{scenario_guid}/hubs")
        envelope = ResponseDtoListFHubResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def create(self, scenario_guid: str, request: HubRequestDto) -> HubResponseDto:
        """Create a new hub in a scenario. ``POST /sympheny-app/scenarios/{scenarioGuid}/hubs``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/scenarios/{scenario_guid}/hubs", json=dump(request))
        envelope = ResponseDtoHubResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, hub_guid: str) -> HubResponseDto:
        """Get hub details. ``GET /sympheny-app/scenarios/hubs/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/hubs/{hub_guid}")
        envelope = ResponseDtoHubResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, hub_guid: str, request: HubResponseDto) -> HubResponseDto:
        """Update a hub. ``PUT /sympheny-app/v2/scenarios/hubs/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/hubs/{hub_guid}", json=dump(request))
        envelope = ResponseDtoHubResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, hub_guid: str) -> builtins.list[HubResponseDto]:
        """Delete a hub; returns the remaining hubs. ``DELETE /sympheny-app/scenarios/hubs/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/hubs/{hub_guid}")
        envelope = ResponseDtoListHubResponseDto.model_validate(raw)
        return unwrap(envelope.data)
