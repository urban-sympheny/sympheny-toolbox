"""Operations on conversion technologies of the Sympheny platform API (``conversion-technology-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ConversionTechnologyDetailResponseDtoV2,
    ConversionTechnologyListResponseDtoV2,
    ConversionTechnologyRequestDtoPUT,
    ConversionTechnologyRequestDtoV2,
    ConversionTechnologyResponseDtoV2,
    ResponseDtoConversionTechnologyDetailResponseDtoV2,
    ResponseDtoConversionTechnologyListResponseDtoV2,
    ResponseDtoConversionTechnologyResponseDtoV2,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncConversionTechnologies:
    """Operations on conversion technologies (``conversion-technology-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: ConversionTechnologyRequestDtoV2) -> ConversionTechnologyResponseDtoV2:
        """Create a conversion technology in a scenario. ``POST /sympheny-app/v2_2/scenarios/{scenarioGuid}/conversion-technologies``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_2/scenarios/{scenario_guid}/conversion-technologies", json=dump(request))
        envelope = ResponseDtoConversionTechnologyResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> ConversionTechnologyListResponseDtoV2:
        """List the conversion technologies of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/conversion-technologies``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/conversion-technologies")
        envelope = ResponseDtoConversionTechnologyListResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, technology_guid: str) -> ConversionTechnologyDetailResponseDtoV2:
        """Get conversion technology details. ``GET /sympheny-app/v2/scenarios/conversion-technologies/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/conversion-technologies/{technology_guid}")
        envelope = ResponseDtoConversionTechnologyDetailResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, technology_guid: str, request: ConversionTechnologyRequestDtoPUT) -> ConversionTechnologyResponseDtoV2:
        """Update a conversion technology. ``PUT /sympheny-app/v2_1/scenarios/conversion-technologies/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_1/scenarios/conversion-technologies/{technology_guid}", json=dump(request))
        envelope = ResponseDtoConversionTechnologyResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, technology_guid: str) -> None:
        """Delete a conversion technology. ``DELETE /sympheny-app/v2/scenarios/conversion-technologies/{guid}``"""
        await self._t.request_json("DELETE", f"/sympheny-app/v2/scenarios/conversion-technologies/{technology_guid}")
