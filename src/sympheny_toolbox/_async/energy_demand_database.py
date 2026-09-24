"""Operations on the energy demand database of the Sympheny platform API (``database-energy-demand-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import ResponseDtoListBigDecimal, ResponseDtoListEnergyDemandDBResponse


if TYPE_CHECKING:
    import builtins

    from sympheny_toolbox._async._transport import AsyncTransport
    from sympheny_toolbox.models import DemandType, EnergyDemandDBRequest, EnergyDemandDBResponse


class AsyncEnergyDemandDatabase:
    """Operations on the energy demand database (``database-energy-demand-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def list(self) -> list[EnergyDemandDBResponse]:
        """List the specific energy demands of the database. ``GET /sympheny-app/database-energy-demand-table``"""
        raw = await self._t.request_json("GET", "/sympheny-app/database-energy-demand-table")
        envelope = ResponseDtoListEnergyDemandDBResponse.model_validate(raw)
        return unwrap(envelope.data)

    async def calculate(self, demand_type: DemandType, requests: builtins.list[EnergyDemandDBRequest]) -> builtins.list[float]:
        """Calculate a demand profile from the database. ``POST /sympheny-app/database-energy-demand-profile/{demandType}/calculate``

        Each request needs ``area_m2`` or ``annual_kwh``.
        """
        raw = await self._t.request_json(
            "POST", f"/sympheny-app/database-energy-demand-profile/{demand_type.value}/calculate", json=[dump(request) for request in requests]
        )
        envelope = ResponseDtoListBigDecimal.model_validate(raw)
        return unwrap(envelope.data)
