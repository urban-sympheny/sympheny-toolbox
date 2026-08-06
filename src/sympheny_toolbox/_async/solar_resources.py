"""Operations on solar on-site resources of the Sympheny platform API (``solar-on-site-resource-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ResponseDtoListSolarOnSiteResourceResponseDtoV2,
    ResponseDtoSolarOnSiteResourceListResponseDto,
    ResponseDtoSolarOnSiteResourceResponseDtoV2,
    SolarOnSiteResourceListResponseDto,
    SolarOnSiteResourceRequestDtoPUT,
    SolarOnSiteResourceRequestDtoV2,
    SolarOnSiteResourceResponseDtoV2,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncSolarResources:
    """Operations on solar on-site resources (``solar-on-site-resource-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: SolarOnSiteResourceRequestDtoV2) -> SolarOnSiteResourceResponseDtoV2:
        """Create a new solar on-site resource in a scenario. ``POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/solar-on-site-resource``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_1/scenarios/{scenario_guid}/solar-on-site-resource", json=dump(request))
        envelope = ResponseDtoSolarOnSiteResourceResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> list[SolarOnSiteResourceResponseDtoV2]:
        """List the solar on-site resources of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/solar-on-site-resource``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/solar-on-site-resource")
        envelope = ResponseDtoListSolarOnSiteResourceResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, resource_guid: str) -> SolarOnSiteResourceResponseDtoV2:
        """Get solar on-site resource details. ``GET /sympheny-app/v2/scenarios/solar-on-site-resource/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/solar-on-site-resource/{resource_guid}")
        envelope = ResponseDtoSolarOnSiteResourceResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, resource_guid: str, request: SolarOnSiteResourceRequestDtoPUT) -> SolarOnSiteResourceResponseDtoV2:
        """Update a solar on-site resource. ``PUT /sympheny-app/v2_2/scenarios/solar-on-site-resource/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_2/scenarios/solar-on-site-resource/{resource_guid}", json=dump(request))
        envelope = ResponseDtoSolarOnSiteResourceResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, resource_guid: str) -> SolarOnSiteResourceListResponseDto:
        """Delete a solar on-site resource; returns the remaining resources. ``DELETE /sympheny-app/scenarios/solar-on-site-resource/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/solar-on-site-resource/{resource_guid}")
        envelope = ResponseDtoSolarOnSiteResourceListResponseDto.model_validate(raw)
        return unwrap(envelope.data)
