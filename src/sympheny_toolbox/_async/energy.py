"""Energy carrier, import/export, profile, energy demand, and solar resource endpoints of the Sympheny platform API."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    EnergyCarrierRequestDtoV2,
    EnergyCarrierResponseDto,
    EnergyCarriersListResponseDto,
    EnergyDemandDetailResponseDtoV2,
    EnergyDemandListResponseDto,
    EnergyDemandRequestDtoV2,
    EnergyDemandResponseDtoV2,
    ImportExportRequestDtoV2,
    ImportExportResponseDtoV2,
    ProfileDetailsResponseDto,
    ProfileJsonRequestDto,
    ProfileResponseDto,
    ResponseDtoEnergyCarrierResponseDto,
    ResponseDtoEnergyCarriersListResponseDto,
    ResponseDtoEnergyDemandDetailResponseDtoV2,
    ResponseDtoEnergyDemandListResponseDto,
    ResponseDtoEnergyDemandResponseDtoV2,
    ResponseDtoImportExportResponseDtoV2,
    ResponseDtoListEnergyDemandResponseDtoV2,
    ResponseDtoListImportExportResponseDtoV2,
    ResponseDtoListProfileResponseDto,
    ResponseDtoListSolarOnSiteResourceResponseDtoV2,
    ResponseDtoProfileDetailsResponseDto,
    ResponseDtoProfileResponseDto,
    ResponseDtoSolarOnSiteResourceListResponseDto,
    ResponseDtoSolarOnSiteResourceResponseDtoV2,
    ResponseDtoStatus,
    SolarOnSiteResourceListResponseDto,
    SolarOnSiteResourceRequestDtoV2,
    SolarOnSiteResourceResponseDtoV2,
    Status,
    Type1,
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

    async def update(self, carrier_guid: str, request: EnergyCarrierResponseDto) -> EnergyCarrierResponseDto:
        """Update an energy carrier. ``PUT /sympheny-app/v2/carriers/{carrierGuid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/carriers/{carrier_guid}", json=dump(request))
        envelope = ResponseDtoEnergyCarrierResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, carrier_guid: str) -> EnergyCarriersListResponseDto:
        """Delete an energy carrier; returns the remaining carriers. ``DELETE /sympheny-app/scenarios/carriers/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/carriers/{carrier_guid}")
        envelope = ResponseDtoEnergyCarriersListResponseDto.model_validate(raw)
        return unwrap(envelope.data)


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

    async def update(self, impex_guid: str, request: ImportExportResponseDtoV2) -> ImportExportResponseDtoV2:
        """Update an import/export. ``PUT /sympheny-app/v2_1/scenarios/impex/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_1/scenarios/impex/{impex_guid}", json=dump(request))
        envelope = ResponseDtoImportExportResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, impex_type: Type1, impex_guid: str) -> Status:
        """Delete an import/export. ``DELETE /sympheny-app/impex/{type}/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/impex/{impex_type.value}/{impex_guid}")
        envelope = ResponseDtoStatus.model_validate(raw)
        return unwrap(envelope.data)


class AsyncProfiles:
    """Operations on profiles (``profile-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: ProfileJsonRequestDto) -> ProfileResponseDto:
        """Create a new profile in a scenario. ``POST /sympheny-app/scenarios/{scenarioGuid}/profiles-json``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/scenarios/{scenario_guid}/profiles-json", json=dump(request))
        envelope = ResponseDtoProfileResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> list[ProfileResponseDto]:
        """List the profiles of a scenario. ``GET /sympheny-app/scenarios/{scenarioGuid}/profiles``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/{scenario_guid}/profiles")
        envelope = ResponseDtoListProfileResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, scenario_guid: str, profile_id: int) -> ProfileDetailsResponseDto:
        """Get profile details. ``GET /sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenarios/{scenario_guid}/profiles/{profile_id}")
        envelope = ResponseDtoProfileDetailsResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, scenario_guid: str, profile_id: int, request: ProfileDetailsResponseDto) -> ProfileDetailsResponseDto:
        """Update a profile. ``PUT /sympheny-app/v2/scenarios/{scenarioGuid}/profiles-json/{profileId}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/{scenario_guid}/profiles-json/{profile_id}", json=dump(request))
        envelope = ResponseDtoProfileDetailsResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str, profile_id: int) -> None:
        """Delete a profile. ``DELETE /sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}``"""
        await self._t.request_json("DELETE", f"/sympheny-app/scenarios/{scenario_guid}/profiles/{profile_id}")


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

    async def update(self, scenario_guid: str, demand_guid: str, request: EnergyDemandResponseDtoV2) -> EnergyDemandResponseDtoV2:
        """Update an energy demand. ``PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/energy-demands/{demand-guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_2/scenarios/{scenario_guid}/energy-demands/{demand_guid}", json=dump(request))
        envelope = ResponseDtoEnergyDemandResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, demand_guid: str) -> EnergyDemandListResponseDto:
        """Delete an energy demand; returns the remaining demands. ``DELETE /sympheny-app/scenarios/energy-demands/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/energy-demands/{demand_guid}")
        envelope = ResponseDtoEnergyDemandListResponseDto.model_validate(raw)
        return unwrap(envelope.data)


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

    async def update(self, resource_guid: str, request: SolarOnSiteResourceResponseDtoV2) -> SolarOnSiteResourceResponseDtoV2:
        """Update a solar on-site resource. ``PUT /sympheny-app/v2_2/scenarios/solar-on-site-resource/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_2/scenarios/solar-on-site-resource/{resource_guid}", json=dump(request))
        envelope = ResponseDtoSolarOnSiteResourceResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, resource_guid: str) -> SolarOnSiteResourceListResponseDto:
        """Delete a solar on-site resource; returns the remaining resources. ``DELETE /sympheny-app/scenarios/solar-on-site-resource/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/solar-on-site-resource/{resource_guid}")
        envelope = ResponseDtoSolarOnSiteResourceListResponseDto.model_validate(raw)
        return unwrap(envelope.data)
