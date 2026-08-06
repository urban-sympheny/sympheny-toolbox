"""Operations on network links of the Sympheny platform API (``network-link-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    NetworkLinkListResponseDto,
    NetworkLinkRequestDtoPUT,
    NetworkLinkRequestDtoV2,
    NetworkLinkResponseDtoV2,
    ResponseDtoListNetworkLinkResponseDtoV2,
    ResponseDtoNetworkLinkListResponseDto,
    ResponseDtoNetworkLinkResponseDtoV2,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncNetworkLinks:
    """Operations on network links (``network-link-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: NetworkLinkRequestDtoV2) -> NetworkLinkResponseDtoV2:
        """Create a network link in a scenario. ``POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/network-links``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_1/scenarios/{scenario_guid}/network-links", json=dump(request))
        envelope = ResponseDtoNetworkLinkResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> list[NetworkLinkResponseDtoV2]:
        """List the network links of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/network-links``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/network-links")
        envelope = ResponseDtoListNetworkLinkResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, link_guid: str) -> NetworkLinkResponseDtoV2:
        """Get network link details. ``GET /sympheny-app/v2/network-links/{network-link-guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/network-links/{link_guid}")
        envelope = ResponseDtoNetworkLinkResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, scenario_guid: str, link_guid: str, request: NetworkLinkRequestDtoPUT) -> NetworkLinkResponseDtoV2:
        """Update a network link. ``PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/network-links/{network-link-guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_2/scenarios/{scenario_guid}/network-links/{link_guid}", json=dump(request))
        envelope = ResponseDtoNetworkLinkResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str, link_guid: str) -> NetworkLinkListResponseDto:
        """Delete a network link; returns the remaining links. ``DELETE /sympheny-app/scenarios/{scenarioGuid}/network-links/{network-link-guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/{scenario_guid}/network-links/{link_guid}")
        envelope = ResponseDtoNetworkLinkListResponseDto.model_validate(raw)
        return unwrap(envelope.data)
