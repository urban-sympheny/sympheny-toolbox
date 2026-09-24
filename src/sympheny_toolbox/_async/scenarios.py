"""Operations on scenarios of the Sympheny platform API (``scenario-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ResponseDtoListFScenarioResponseDto,
    ResponseDtoS3PresignedUrlDto,
    ResponseDtoScenarioResponseDto,
    ResponseDtoSpecsInputFilePresignedUrlResponseDto,
    ResponseDtoStatus,
    ScenarioExcelRequestDto,
    ScenarioExcelRequestDtoPUT,
    ScenarioGuidListDto,
    ScenarioRequestDto,
    ScenarioResponseDto,
    Status,
)


if TYPE_CHECKING:
    import builtins

    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncScenarios:
    """Operations on scenarios (``scenario-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def list(self, analysis_guid: str) -> list[ScenarioResponseDto]:
        """List the scenarios of an analysis. ``GET /sympheny-app/analysis/{guid}/scenario``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/analysis/{analysis_guid}/scenario")
        envelope = ResponseDtoListFScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def create(self, analysis_guid: str, request: ScenarioRequestDto) -> ScenarioResponseDto:
        """Create a new scenario in an analysis. ``POST /sympheny-app/analysis/{guid}/scenario``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/analysis/{analysis_guid}/scenario", json=dump(request))
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, scenario_guid: str) -> ScenarioResponseDto:
        """Get scenario details. ``GET /sympheny-app/scenario/{scenarioGuid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/scenario/{scenario_guid}")
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def rename(self, scenario_guid: str, request: ScenarioRequestDto) -> ScenarioResponseDto:
        """Rename a scenario in place. ``PUT /sympheny-app/scenarios/{scenarioGuid}``

        Unlike [copy][sympheny_toolbox._async.scenarios.AsyncScenarios.copy], this sets the scenario's
        name directly, so it works within the scenario's current analysis without creating a duplicate.
        """
        raw = await self._t.request_json("PUT", f"/sympheny-app/scenarios/{scenario_guid}", json=dump(request))
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str) -> Status:
        """Delete a scenario. ``DELETE /sympheny-app/scenario/{scenarioGuid}``

        The API returns no ``data`` payload for this endpoint even on success, so a missing payload is
        treated as an empty [Status][sympheny_toolbox.models.Status] rather than an error.
        """
        raw = await self._t.request_json("DELETE", f"/sympheny-app/scenario/{scenario_guid}")
        envelope = ResponseDtoStatus.model_validate(raw)
        return envelope.data if envelope.data is not None else Status()

    async def copy(self, scenario_guid: str, *, analysis_destination_guid: str | None = None, name: str | None = None) -> ScenarioResponseDto:
        """Copy a scenario, optionally into another analysis. ``PUT /sympheny-app/scenarios/copy/{scenarioGuid}``

        With no ``analysis_destination_guid`` the copy stays in the source's analysis; ``name`` sets
        the copy's name in either case.
        """
        params: dict[str, str] = {}
        if analysis_destination_guid is not None:
            params["analysisDestinationGuid"] = analysis_destination_guid
        if name is not None:
            params["name"] = name
        raw = await self._t.request_json("PUT", f"/sympheny-app/scenarios/copy/{scenario_guid}", params=params or None)
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def excel_upload_url(self, *, delete_previous: bool | None = None) -> str:
        """Get a presigned URL to upload a scenario Excel file to. ``GET /sympheny-app/db-update/s3-presigned-url``

        Upload the file to the returned URL with a plain HTTP ``PUT`` (no bearer token), then pass the
        URL to [create_from_excel][sympheny_toolbox._async.scenarios.AsyncScenarios.create_from_excel]
        or [replace_from_excel][sympheny_toolbox._async.scenarios.AsyncScenarios.replace_from_excel].
        """
        params = {"deletePrevious": str(delete_previous).lower()} if delete_previous is not None else None
        raw = await self._t.request_json("GET", "/sympheny-app/db-update/s3-presigned-url", params=params)
        envelope = ResponseDtoS3PresignedUrlDto.model_validate(raw)
        return unwrap(unwrap(envelope.data).s3_presigned_url)

    async def create_from_excel(self, analysis_guid: str, s3_presigned_url: str, name: str) -> ScenarioResponseDto:
        """Create a scenario in an analysis from an uploaded Excel file. ``POST /sympheny-app/v2/analysis/{guid}/scenario/excel``"""
        request = ScenarioExcelRequestDto(s3_presigned_url=s3_presigned_url, scenario_name=name)
        raw = await self._t.request_json("POST", f"/sympheny-app/v2/analysis/{analysis_guid}/scenario/excel", json=dump(request))
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def replace_from_excel(self, scenario_guid: str, s3_presigned_url: str) -> ScenarioResponseDto:
        """Replace a scenario's content with an uploaded Excel file. ``PUT /sympheny-app/v2/scenarios/{scenarioGuid}/excel``"""
        request = ScenarioExcelRequestDtoPUT(s3_presigned_url=s3_presigned_url)
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/{scenario_guid}/excel", json=dump(request))
        envelope = ResponseDtoScenarioResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def prepare_specs_input_files(self, scenario_guids: builtins.list[str]) -> Status:
        """Start generating the specs input files of scenarios of one analysis. ``PUT /sympheny-app/v2/specs``

        Generation runs in the background: poll
        [specs_input_file_url][sympheny_toolbox._async.scenarios.AsyncScenarios.specs_input_file_url]
        for each scenario until it returns a URL.
        """
        request = ScenarioGuidListDto(scenario_guids=scenario_guids)
        raw = await self._t.request_json("PUT", "/sympheny-app/v2/specs", json=dump(request))
        envelope = ResponseDtoStatus.model_validate(raw)
        return unwrap(envelope.data)

    async def specs_input_file_url(self, scenario_guid: str) -> str | None:
        """Get the download URL of a scenario's specs input file. ``GET /sympheny-app/scenario/{scenarioGuid}/specs-input-file-url``

        Returns ``None`` until the file started by
        [prepare_specs_input_files][sympheny_toolbox._async.scenarios.AsyncScenarios.prepare_specs_input_files]
        is ready.
        """
        raw = await self._t.request_json("GET", f"/sympheny-app/scenario/{scenario_guid}/specs-input-file-url")
        envelope = ResponseDtoSpecsInputFilePresignedUrlResponseDto.model_validate(raw)
        return unwrap(envelope.data).presigned_url
