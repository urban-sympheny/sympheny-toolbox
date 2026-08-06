"""Operations on energy imports and exports of the Sympheny platform API (``impex-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ImportExportRequestDtoPUT,
    ImportExportRequestDtoV2,
    ImportExportResponseDtoV2,
    ResponseDtoImportExportResponseDtoV2,
    ResponseDtoListImportExportResponseDtoV2,
    ResponseDtoStatus,
    Status,
    Type1,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncImpex:
    """Operations on energy imports and exports (``impex-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: ImportExportRequestDtoV2) -> ImportExportResponseDtoV2:
        """Create a new import/export in a scenario. ``POST /sympheny-app/v2_1/scenario/{scenarioGuid}/impex``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_1/scenario/{scenario_guid}/impex", json=dump(request))
        envelope = ResponseDtoImportExportResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> list[ImportExportResponseDtoV2]:
        """List the imports/exports of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/impexes``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/impexes")
        envelope = ResponseDtoListImportExportResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, impex_type: Type1, impex_guid: str, *, scenario_variant_guid: str | None = None) -> ImportExportResponseDtoV2:
        """Get import/export details. ``GET /sympheny-app/v2/impex/{type}/{guid}``"""
        params: dict[str, str] = {}
        if scenario_variant_guid is not None:
            params["scenarioVariantGuid"] = scenario_variant_guid
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/impex/{impex_type.value}/{impex_guid}", params=params or None)
        envelope = ResponseDtoImportExportResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, impex_guid: str, request: ImportExportRequestDtoPUT) -> ImportExportResponseDtoV2:
        """Update an import/export. ``PUT /sympheny-app/v2_1/scenarios/impex/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_1/scenarios/impex/{impex_guid}", json=dump(request))
        envelope = ResponseDtoImportExportResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, impex_type: Type1, impex_guid: str) -> Status:
        """Delete an import/export. ``DELETE /sympheny-app/impex/{type}/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/impex/{impex_type.value}/{impex_guid}")
        envelope = ResponseDtoStatus.model_validate(raw)
        return unwrap(envelope.data)
