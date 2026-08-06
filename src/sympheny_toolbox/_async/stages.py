"""Operations on stages of the Sympheny platform API (``stage-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ResponseDtoListStageResponseDto,
    ResponseDtoStageResponseDto,
    StageCore,
    StageRequestDto,
    StageResponseDto,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


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

    async def update(self, scenario_guid: str, stage_guid: str, request: StageCore) -> StageResponseDto:
        """Update a stage. ``PUT /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/scenarios/{scenario_guid}/stages/{stage_guid}", json=dump(request))
        envelope = ResponseDtoStageResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str, stage_guid: str) -> None:
        """Delete a stage. ``DELETE /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}``"""
        await self._t.request_json("DELETE", f"/sympheny-app/scenarios/{scenario_guid}/stages/{stage_guid}")
