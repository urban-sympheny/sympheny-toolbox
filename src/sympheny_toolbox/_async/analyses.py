"""Operations on analyses of the Sympheny platform API (``analysis-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    AnalysisDetailsResponseDto,
    AnalysisRequestDto,
    AnalysisResponseDto,
    PagedResponseAnalysisResponseDto,
    ResponseDtoAnalysisDetailsResponseDto,
    ResponseDtoAnalysisResponseDto,
    ResponseDtoStatus,
    Status,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncAnalyses:
    """Operations on analyses (``analysis-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def list(self, project_guid: str) -> list[AnalysisResponseDto]:
        """List the analyses of a project. ``GET /sympheny-app/projects/{guid}/analyses``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/projects/{project_guid}/analyses")
        envelope = PagedResponseAnalysisResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def create(self, project_guid: str, request: AnalysisRequestDto) -> AnalysisResponseDto:
        """Create a new analysis in a project. ``POST /sympheny-app/projects/{guid}/analyses``"""
        raw = await self._t.request_json("POST", f"/sympheny-app/projects/{project_guid}/analyses", json=dump(request))
        envelope = ResponseDtoAnalysisResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, project_guid: str, analysis_guid: str) -> AnalysisDetailsResponseDto:
        """Get analysis details. ``GET /sympheny-app/projects/{guid}/analysis/{analysisGuid}``"""
        raw = await self._t.request_json("GET", f"/sympheny-app/projects/{project_guid}/analysis/{analysis_guid}")
        envelope = ResponseDtoAnalysisDetailsResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, analysis_guid: str) -> Status:
        """Delete an analysis. ``DELETE /sympheny-app/analysis/{analysisGuid}``

        The API returns no ``data`` payload for this endpoint even on success, so a missing
        payload is treated as an empty [Status][sympheny_toolbox.models.Status] rather than an error.
        """
        raw = await self._t.request_json("DELETE", f"/sympheny-app/analysis/{analysis_guid}")
        envelope = ResponseDtoStatus.model_validate(raw)
        return envelope.data if envelope.data is not None else Status()
