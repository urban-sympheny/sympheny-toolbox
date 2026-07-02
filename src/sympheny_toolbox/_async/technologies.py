"""Technology and network endpoints of the Sympheny platform API."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ConversionTechnologyDetailResponseDtoV2,
    ConversionTechnologyListResponseDtoV2,
    ConversionTechnologyRequestDtoV2,
    ConversionTechnologyResponseDtoV2,
    IntraHubNetworkLinkListResponseDto,
    IntraHubNetworkLinkRequestDto,
    IntraHubNetworkLinkResponseDto,
    NetworkLinkListResponseDto,
    NetworkLinkRequestDtoV2,
    NetworkLinkResponseDtoV2,
    NetworkTechnologyListResponseDto,
    NetworkTechnologyListResponseDtoV2,
    NetworkTechnologyRequestDtoV2,
    NetworkTechnologyResponseDtoV2,
    ResponseDtoConversionTechnologyDetailResponseDtoV2,
    ResponseDtoConversionTechnologyListResponseDtoV2,
    ResponseDtoConversionTechnologyResponseDtoV2,
    ResponseDtoIntraHubNetworkLinkListResponseDto,
    ResponseDtoIntraHubNetworkLinkResponseDto,
    ResponseDtoListNetworkLinkResponseDtoV2,
    ResponseDtoNetworkLinkListResponseDto,
    ResponseDtoNetworkLinkResponseDtoV2,
    ResponseDtoNetworkTechnologyListResponseDto,
    ResponseDtoNetworkTechnologyListResponseDtoV2,
    ResponseDtoNetworkTechnologyResponseDtoV2,
    ResponseDtoStorageTechnologyDetailResponseDtoV2,
    ResponseDtoStorageTechnologyListResponseDto,
    ResponseDtoStorageTechnologyListResponseDtoV2,
    ResponseDtoStorageTechnologyResponseDtoV2,
    ResponseDtoTechnologyPackageListResponseDto,
    ResponseDtoTechnologyPackageListResponseDtoV2,
    ResponseDtoTechnologyPackageResponseDtoV2,
    StorageTechnologyDetailResponseDtoV2,
    StorageTechnologyListResponseDto,
    StorageTechnologyListResponseDtoV2,
    StorageTechnologyRequestDtoV2,
    StorageTechnologyResponseDtoV2,
    TechnologyPackageListResponseDto,
    TechnologyPackageListResponseDtoV2,
    TechnologyPackageRequestDtoV2,
    TechnologyPackageResponseDtoV2,
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

    async def update(self, technology_guid: str, request: ConversionTechnologyDetailResponseDtoV2) -> ConversionTechnologyResponseDtoV2:
        """Update a conversion technology. ``PUT /sympheny-app/v2_1/scenarios/conversion-technologies/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_1/scenarios/conversion-technologies/{technology_guid}", json=dump(request))
        envelope = ResponseDtoConversionTechnologyResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, technology_guid: str) -> None:
        """Delete a conversion technology. ``DELETE /sympheny-app/v2/scenarios/conversion-technologies/{guid}``"""
        await self._t.request_json("DELETE", f"/sympheny-app/v2/scenarios/conversion-technologies/{technology_guid}")


class AsyncStorageTechnologies:
    """Operations on storage technologies (``storage-technology-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: StorageTechnologyRequestDtoV2) -> StorageTechnologyResponseDtoV2:
        """Create a storage technology in a scenario. ``POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/storage-technologies``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_1/scenarios/{scenario_guid}/storage-technologies", json=dump(request))
        envelope = ResponseDtoStorageTechnologyResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> StorageTechnologyListResponseDtoV2:
        """List the storage technologies of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/storage-technologies``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/storage-technologies")
        envelope = ResponseDtoStorageTechnologyListResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, technology_guid: str) -> StorageTechnologyDetailResponseDtoV2:
        """Get storage technology details. ``GET /sympheny-app/v2/scenarios/storage-technologies/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/storage-technologies/{technology_guid}")
        envelope = ResponseDtoStorageTechnologyDetailResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, technology_guid: str, request: StorageTechnologyDetailResponseDtoV2) -> StorageTechnologyDetailResponseDtoV2:
        """Update a storage technology. ``PUT /sympheny-app/v2_2/scenarios/storage-technologies/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_2/scenarios/storage-technologies/{technology_guid}", json=dump(request))
        envelope = ResponseDtoStorageTechnologyDetailResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, technology_guid: str) -> StorageTechnologyListResponseDto:
        """Delete a storage technology; returns the remaining storage technologies. ``DELETE /sympheny-app/scenarios/storage-technologies/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/storage-technologies/{technology_guid}")
        envelope = ResponseDtoStorageTechnologyListResponseDto.model_validate(raw)
        return unwrap(envelope.data)


class AsyncTechnologyPackages:
    """Operations on technology packages (``technology-package-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: TechnologyPackageRequestDtoV2) -> TechnologyPackageResponseDtoV2:
        """Create a technology package in a scenario. ``POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_1/scenarios/{scenario_guid}/technology-packages", json=dump(request))
        envelope = ResponseDtoTechnologyPackageResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> TechnologyPackageListResponseDtoV2:
        """List the technology packages of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/technology-packages")
        envelope = ResponseDtoTechnologyPackageListResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, scenario_guid: str, package_guid: str) -> TechnologyPackageResponseDtoV2:
        """Get technology package details. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/technology-packages/{package_guid}")
        envelope = ResponseDtoTechnologyPackageResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, scenario_guid: str, package_guid: str, request: TechnologyPackageResponseDtoV2) -> TechnologyPackageResponseDtoV2:
        """Update a technology package. ``PUT /sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages/{guid}``"""
        raw = await self._t.request_json(
            "PUT", f"/sympheny-app/v2_1/scenarios/{scenario_guid}/technology-packages/{package_guid}", json=dump(request)
        )
        envelope = ResponseDtoTechnologyPackageResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str, package_guid: str, *, delete_techs: bool | None = None) -> TechnologyPackageListResponseDto:
        """Delete a technology package. ``DELETE /sympheny-app/scenarios/{scenarioGuid}/technology-packages/{guid}``"""
        params: dict[str, bool] = {}
        if delete_techs is not None:
            params["deleteTechs"] = delete_techs
        raw = await self._t.request_json(
            "DELETE", f"/sympheny-app/scenarios/{scenario_guid}/technology-packages/{package_guid}", params=params or None
        )
        envelope = ResponseDtoTechnologyPackageListResponseDto.model_validate(raw)
        return unwrap(envelope.data)


class AsyncNetworkTechnologies:
    """Operations on network technologies (``network-technology-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def create(self, scenario_guid: str, request: NetworkTechnologyRequestDtoV2) -> NetworkTechnologyResponseDtoV2:
        """Create a network technology in a scenario. ``POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/network-technologies``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/v2_1/scenarios/{scenario_guid}/network-technologies", json=dump(request))
        envelope = ResponseDtoNetworkTechnologyResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def list(self, scenario_guid: str) -> NetworkTechnologyListResponseDtoV2:
        """List the network technologies of a scenario. ``GET /sympheny-app/v2/scenarios/{scenarioGuid}/network-technologies``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/{scenario_guid}/network-technologies")
        envelope = ResponseDtoNetworkTechnologyListResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, technology_guid: str) -> NetworkTechnologyResponseDtoV2:
        """Get network technology details. ``GET /sympheny-app/v2/scenarios/network-technologies/{guid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/v2/scenarios/network-technologies/{technology_guid}")
        envelope = ResponseDtoNetworkTechnologyResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def update(self, technology_guid: str, request: NetworkTechnologyResponseDtoV2) -> NetworkTechnologyResponseDtoV2:
        """Update a network technology. ``PUT /sympheny-app/v2_1/scenarios/network-technologies/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_1/scenarios/network-technologies/{technology_guid}", json=dump(request))
        envelope = ResponseDtoNetworkTechnologyResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, technology_guid: str) -> NetworkTechnologyListResponseDto:
        """Delete a network technology; returns the remaining network technologies. ``DELETE /sympheny-app/scenarios/network-technologies/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/network-technologies/{technology_guid}")
        envelope = ResponseDtoNetworkTechnologyListResponseDto.model_validate(raw)
        return unwrap(envelope.data)


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

    async def update(self, scenario_guid: str, link_guid: str, request: NetworkLinkResponseDtoV2) -> NetworkLinkResponseDtoV2:
        """Update a network link. ``PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/network-links/{network-link-guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2_2/scenarios/{scenario_guid}/network-links/{link_guid}", json=dump(request))
        envelope = ResponseDtoNetworkLinkResponseDtoV2.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str, link_guid: str) -> NetworkLinkListResponseDto:
        """Delete a network link; returns the remaining links. ``DELETE /sympheny-app/scenarios/{scenarioGuid}/network-links/{network-link-guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/{scenario_guid}/network-links/{link_guid}")
        envelope = ResponseDtoNetworkLinkListResponseDto.model_validate(raw)
        return unwrap(envelope.data)


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

    async def update(self, link_guid: str, request: IntraHubNetworkLinkResponseDto) -> IntraHubNetworkLinkResponseDto:
        """Update an intra-hub network link. ``PUT /sympheny-app/v2/scenarios/intra-hub-network-links/{guid}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/intra-hub-network-links/{link_guid}", json=dump(request))
        envelope = ResponseDtoIntraHubNetworkLinkResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, link_guid: str) -> IntraHubNetworkLinkListResponseDto:
        """Delete an intra-hub network link; returns the remaining links. ``DELETE /sympheny-app/scenarios/intra-hub-network-links/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenarios/intra-hub-network-links/{link_guid}")
        envelope = ResponseDtoIntraHubNetworkLinkListResponseDto.model_validate(raw)
        return unwrap(envelope.data)
