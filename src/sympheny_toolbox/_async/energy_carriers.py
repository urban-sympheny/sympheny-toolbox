"""Operations on energy carriers of the Sympheny platform API (``energy-carrier-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    EnergyCarrierRequestDtoPUT,
    EnergyCarrierRequestDtoV2,
    EnergyCarrierResponseDto,
    EnergyCarriersListResponseDto,
    ResponseDtoEnergyCarrierResponseDto,
    ResponseDtoEnergyCarriersListResponseDto,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncEnergyCarriers:
    """Operations on energy carriers (``energy-carrier-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: EnergyCarrierRequestDtoV2) -> EnergyCarrierResponseDto:
        """Create a new energy carrier in a scenario. ``POST /sympheny-app/v2/scenarios/{scenarioGuid}/carriers``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2/scenarios/{scenario_guid}/carriers", json=dump(request))
        envelope = ResponseDtoEnergyCarrierResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> EnergyCarriersListResponseDto:
        """List the energy carriers of a scenario. ``GET /sympheny-app/scenarios/{scenarioGuid}/carriers``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/{scenario_guid}/carriers")
        envelope = ResponseDtoEnergyCarriersListResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, carrier_guid: str) -> EnergyCarrierResponseDto:
        """Get energy carrier details. ``GET /sympheny-app/carriers/{carrierGuid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/carriers/{carrier_guid}")
        envelope = ResponseDtoEnergyCarrierResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, carrier_guid: str, request: EnergyCarrierRequestDtoPUT) -> EnergyCarrierResponseDto:
        """Update an energy carrier. ``PUT /sympheny-app/v2/carriers/{carrierGuid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/carriers/{carrier_guid}", json=dump(request))
        envelope = ResponseDtoEnergyCarrierResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, carrier_guid: str) -> EnergyCarriersListResponseDto:
        """Delete an energy carrier; returns the remaining carriers. ``DELETE /sympheny-app/scenarios/carriers/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/carriers/{carrier_guid}")
        envelope = ResponseDtoEnergyCarriersListResponseDto.model_validate(raw)
        return unwrap(envelope.data)
