"""Operations on intra-hub network links of the Sympheny platform API (``intra-hub-network-link-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    IntraHubNetworkLinkListResponseDto,
    IntraHubNetworkLinkRequestDto,
    IntraHubNetworkLinkRequestDtoPUT,
    IntraHubNetworkLinkResponseDto,
    ResponseDtoIntraHubNetworkLinkListResponseDto,
    ResponseDtoIntraHubNetworkLinkResponseDto,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncIntraHubNetworkLinks:
    """Operations on intra-hub network links (``intra-hub-network-link-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: IntraHubNetworkLinkRequestDto) -> IntraHubNetworkLinkResponseDto:
        """Create an intra-hub network link in a scenario. ``POST /sympheny-app/v2/scenarios/{scenarioGuid}/intra-hub-network-links``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2/scenarios/{scenario_guid}/intra-hub-network-links", json=dump(request))
        envelope = ResponseDtoIntraHubNetworkLinkResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> IntraHubNetworkLinkListResponseDto:
        """List the intra-hub network links of a scenario. ``GET /sympheny-app/scenarios/{scenarioGuid}/intra-hub-network-links``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/{scenario_guid}/intra-hub-network-links")
        envelope = ResponseDtoIntraHubNetworkLinkListResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, link_guid: str) -> IntraHubNetworkLinkResponseDto:
        """Get intra-hub network link details. ``GET /sympheny-app/scenarios/intra-hub-network-links/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/intra-hub-network-links/{link_guid}")
        envelope = ResponseDtoIntraHubNetworkLinkResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, link_guid: str, request: IntraHubNetworkLinkRequestDtoPUT) -> IntraHubNetworkLinkResponseDto:
        """Update an intra-hub network link. ``PUT /sympheny-app/v2/scenarios/intra-hub-network-links/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/intra-hub-network-links/{link_guid}", json=dump(request))
        envelope = ResponseDtoIntraHubNetworkLinkResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, link_guid: str) -> IntraHubNetworkLinkListResponseDto:
        """Delete an intra-hub network link; returns the remaining links. ``DELETE /sympheny-app/scenarios/intra-hub-network-links/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/intra-hub-network-links/{link_guid}")
        envelope = ResponseDtoIntraHubNetworkLinkListResponseDto.model_validate(raw)
        return unwrap(envelope.data)
