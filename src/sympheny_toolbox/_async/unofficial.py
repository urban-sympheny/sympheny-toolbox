"""UNOFFICIAL Sympheny API endpoints.

Every method in this module calls an endpoint that is **not part of the official
documented Sympheny API** (``specs/sympheny_openapi.json``). These endpoints may
change or disappear without notice. They return raw JSON payloads (``dict``/``list``)
instead of typed models.

As the official OpenAPI spec grows, some of these endpoints may be migrated onto the
typed resource classes (e.g. ``client.projects``) and removed from ``client.unofficial``
without notice. Prefer an official, typed equivalent whenever one exists.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncUnofficial:
    """Endpoints outside the official documented Sympheny API. May change without notice."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    # -- analysis ---------------------------------------------------------

    async def get_analysis(self, analysis_guid: str) -> dict[str, Any]:
        """UNOFFICIAL — Get analysis details incl. scenarios and results. ``GET /sympheny-app/analysis/{guid}``

        Prefer ``client.analyses.get`` unless you need the ``results`` payload
        (scenarios / input-file paths), which the official endpoint does not return.
        """
        raw = await self._t.request_json("GET", f"/sympheny-app/analysis/{analysis_guid}")
        return dict(raw["data"])

    # -- scenario variants (master scenario) ------------------------------

    async def create_master_scenario(self, payload: dict[str, Any]) -> dict[str, Any]:
        """UNOFFICIAL — Create a master scenario. ``POST /sympheny-app/master-scenario/``"""
        raw = await self._t.request_json("POST", "/sympheny-app/master-scenario/", json=payload)
        return dict(raw["data"])

    async def list_variants(self, master_scenario_guid: str) -> list[dict[str, Any]]:
        """UNOFFICIAL — List scenario variants of a master scenario. ``GET /sympheny-app/master-scenario/{guid}/scenario-variants``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/master-scenario/{master_scenario_guid}/scenario-variants")
        return list(raw["data"])

    async def delete_all_variants(self, master_scenario_guid: str) -> None:
        """UNOFFICIAL — Delete all scenario variants of a master scenario. ``DELETE /sympheny-app/master-scenario/{guid}/scenario-variants``"""
        await self._t.request_json("DELETE", f"/sympheny-app/master-scenario/{master_scenario_guid}/scenario-variants")

    async def get_variants_excel_url(self, master_scenario_guid: str) -> str:
        """UNOFFICIAL — Get a presigned URL to the variants Excel export. ``GET /sympheny-app/master-scenario/{guid}/scenario-variants-excel``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/master-scenario/{master_scenario_guid}/scenario-variants-excel")
        return str(raw["data"]["s3PresignedUrl"])

    async def create_variants_from_excel_url(self, presigned_url: str, master_scenario_guid: str, *, delete_existing: bool = True) -> Any:
        """UNOFFICIAL — Create scenario variants from an uploaded Excel file. ``PUT /sympheny-app/scenario-variants-excel``"""
        payload = {"s3PresignedUrl": presigned_url, "masterScenarioGuid": master_scenario_guid, "deleteExisting": delete_existing}
        raw = await self._t.request_json("PUT", "/sympheny-app/scenario-variants-excel", json=payload)
        return raw["data"] if isinstance(raw, dict) else raw

    # -- scenario creation & preparation ----------------------------------

    async def get_upload_url(self) -> str:
        """UNOFFICIAL — Get a presigned S3 URL for file uploads. ``GET /sympheny-app/db-update/s3-presigned-url``"""
        raw = await self._t.request_json("GET", "/sympheny-app/db-update/s3-presigned-url")
        return str(raw["data"]["s3PresignedUrl"])

    async def upload_to_presigned_url(self, presigned_url: str, content: bytes) -> None:
        """UNOFFICIAL — Upload raw bytes to a presigned S3 URL (no Sympheny auth)."""
        await self._t.request_unauthenticated("PUT", presigned_url, content=content)

    async def create_scenario_from_excel_url(self, presigned_url: str, scenario_name: str, analysis_guid: str) -> str:
        """UNOFFICIAL — Create a scenario from an uploaded Excel file; returns the scenario GUID.

        ``POST /sympheny-app/v2/analysis/{guid}/scenario/excel``
        """
        payload = {"s3PresignedUrl": presigned_url, "scenarioName": scenario_name}
        raw = await self._t.request_json("POST", f"/sympheny-app/v2/analysis/{analysis_guid}/scenario/excel", json=payload)
        return str(raw["data"]["scenarioGuid"])

    async def close_diagram(self, scenario_guid: str) -> None:
        """UNOFFICIAL — Close the hub diagram of a scenario. ``PUT /sympheny-app/scenarios/{guid}/close-diagram``"""
        await self._t.request_json("PUT", f"/sympheny-app/scenarios/{scenario_guid}/close-diagram")

    async def generate_specs(self, scenario_guids: list[str]) -> None:
        """UNOFFICIAL — Trigger input-file (specs) generation for scenarios. ``PUT /sympheny-app/v2/specs``"""
        await self._t.request_json("PUT", "/sympheny-app/v2/specs", json={"scenarioGuids": scenario_guids})

    async def generate_scenario_specs(self, scenario_guid: str) -> None:
        """UNOFFICIAL — Trigger specs generation for a single scenario. ``PUT /sympheny-app/v2/scenarios/{guid}/specs``"""
        await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/{scenario_guid}/specs")

    # -- enymap ------------------------------------------------------------

    async def create_scenario_enymap(self, analysis_guid: str, payload: dict[str, Any]) -> dict[str, Any]:
        """UNOFFICIAL — Create an enymap scenario. ``POST /sympheny-app/analysis/{guid}/scenario-enymap``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/analysis/{analysis_guid}/scenario-enymap", json=payload)
        return dict(raw["data"])

    async def create_gis_hub(self, scenario_guid: str, polygon: list[Any]) -> Any:
        """UNOFFICIAL — Create a GIS hub for an enymap scenario. ``POST /sympheny-app/scenario-enymap/{guid}/create-gis-hub``"""
        return await self._t.request_json("POST", f"/sympheny-app/scenario-enymap/{scenario_guid}/create-gis-hub", json={"polygon": polygon})

    async def create_demand_solar(self, scenario_guid: str) -> Any:
        """UNOFFICIAL — Create demands and solar resources for an enymap scenario.

        ``POST /sympheny-app/scenario-enymap/{guid}/create-demand-solar``
        """
        return await self._t.request_json("POST", f"/sympheny-app/scenario-enymap/{scenario_guid}/create-demand-solar")

    # -- api-services backend ----------------------------------------------

    async def gis_background_jobs(self) -> list[dict[str, Any]]:
        """UNOFFICIAL — List GIS background jobs (``api-services`` backend). ``GET /api-services/gis/background``"""
        raw = await self._t.request_json("GET", "/api-services/gis/background")
        return list(raw)

    async def hub_demand(self, demand_type: str, building_type: str, buildings: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """UNOFFICIAL — Estimate building energy demand (``api-services`` backend). ``POST /api-services/demand/hub_demand``"""
        params = {"demand_type": demand_type, "building_type": building_type}
        raw = await self._t.request_json("POST", "/api-services/demand/hub_demand", params=params, json=buildings)
        return list(raw)

    # -- database energy demands -------------------------------------------

    async def get_database_demand_profile(self, demand_guid: str) -> list[dict[str, Any]]:
        """UNOFFICIAL — Get the normalized profile of a database energy demand.

        ``GET /sympheny-app/database-energy-demands/{guid}/profile``
        """
        raw = await self._t.request_json("GET", f"/sympheny-app/database-energy-demands/{demand_guid}/profile")
        return list(raw["data"])
