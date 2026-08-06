"""Operations on energy demands of the Sympheny platform API (``energy-demand-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    EnergyDemandDetailResponseDtoV2,
    EnergyDemandListResponseDto,
    EnergyDemandRequestDtoPUT,
    EnergyDemandRequestDtoV2,
    EnergyDemandResponseDtoV2,
    ResponseDtoEnergyDemandDetailResponseDtoV2,
    ResponseDtoEnergyDemandListResponseDto,
    ResponseDtoEnergyDemandResponseDtoV2,
    ResponseDtoListEnergyDemandResponseDtoV2,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncEnergyDemands:
    """Operations on energy demands (``energy-demand-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: EnergyDemandRequestDtoV2) -> EnergyDemandResponseDtoV2:
        """Create a new energy demand in a scenario. ``POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/energy-demands``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_1/scenarios/{scenario_guid}/energy-demands", json=dump(request))
        envelope = ResponseDtoEnergyDemandResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> list[EnergyDemandResponseDtoV2]:
        """List the energy demands of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/energy-demands``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/energy-demands")
        envelope = ResponseDtoListEnergyDemandResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, demand_guid: str, *, scenario_variant_guid: str | None = None) -> EnergyDemandDetailResponseDtoV2:
        """Get energy demand details. ``GET /sympheny-app/v2/energy-demands/{guid}``"""
        params: dict[str, str] = {}
        if scenario_variant_guid is not None:
            params["scenarioVariantGuid"] = scenario_variant_guid
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/energy-demands/{demand_guid}", params=params or None)
        envelope = ResponseDtoEnergyDemandDetailResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, scenario_guid: str, demand_guid: str, request: EnergyDemandRequestDtoPUT) -> EnergyDemandResponseDtoV2:
        """Update an energy demand. ``PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/energy-demands/{demand-guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_2/scenarios/{scenario_guid}/energy-demands/{demand_guid}", json=dump(request))
        envelope = ResponseDtoEnergyDemandResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, demand_guid: str) -> EnergyDemandListResponseDto:
        """Delete an energy demand; returns the remaining demands. ``DELETE /sympheny-app/scenarios/energy-demands/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/energy-demands/{demand_guid}")
        envelope = ResponseDtoEnergyDemandListResponseDto.model_validate(raw)
        return unwrap(envelope.data)
