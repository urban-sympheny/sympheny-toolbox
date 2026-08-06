"""Operations on hubs of the Sympheny platform API (``hub-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    HubRequestDto,
    HubRequestDtoPUT,
    HubResponseDto,
    ResponseDtoHubResponseDto,
    ResponseDtoListFHubResponseDto,
    ResponseDtoListHubResponseDto,
)


if TYPE_CHECKING:
    import builtins

    from sympheny_toolbox._async._transport import AsyncTransport


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

    async def update(self, hub_guid: str, request: HubRequestDtoPUT) -> HubResponseDto:
        """Update a hub. ``PUT /sympheny-app/v2/scenarios/hubs/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/hubs/{hub_guid}", json=dump(request))
        envelope = ResponseDtoHubResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, hub_guid: str) -> builtins.list[HubResponseDto]:
        """Delete a hub; returns the remaining hubs. ``DELETE /sympheny-app/scenarios/hubs/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/hubs/{hub_guid}")
        envelope = ResponseDtoListHubResponseDto.model_validate(raw)
        return unwrap(envelope.data)
