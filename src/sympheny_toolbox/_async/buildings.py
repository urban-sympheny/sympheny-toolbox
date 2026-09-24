"""Building lookups of the Sympheny services API (``GIS Buildings``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump
from sympheny_toolbox.models import BuildingFeatureCollection, BuildingsRequest


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport
    from sympheny_toolbox.models import Geometry


class AsyncBuildings:
    """Building lookups (``GIS Buildings``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def in_area(self, aoi: Geometry) -> BuildingFeatureCollection:
        """Find the buildings within an area, as GeoJSON features. ``POST /api-services/gis/buildings``"""
        raw = await self._t.request_json("POST", "/api-services/gis/buildings", json=dump(BuildingsRequest(aoi=aoi)))
        return BuildingFeatureCollection.model_validate(raw)
