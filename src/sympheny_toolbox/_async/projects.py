"""Operations on projects of the Sympheny platform API (``project-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ProjectDetailResponseDto,
    ProjectRequestDto,
    ProjectResponseDto,
    ProjectSummaryResponseDto,
    ResponseDtoProjectDetailResponseDto,
    ResponseDtoProjectResponseDto,
    ResponseDtoProjectSummaryResponseDto,
    Version,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


class AsyncProjects:
    """Operations on projects (``project-controller``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def list(self) -> list[ProjectResponseDto]:
        """List all projects visible to the authenticated user. ``GET /sympheny-app/projects``"""
        raw = await self._t.request_json("GET", "/sympheny-app/projects")
        envelope = ResponseDtoProjectSummaryResponseDto.model_validate(raw)
        return unwrap(envelope.data).projects or []

    async def create(self, request: ProjectRequestDto) -> ProjectResponseDto:
        """Create a new project. Only V2 projects are supported. ``POST /sympheny-app/projects``"""
        if request.version != Version.v2:
            raise ValueError("Only V2 projects are supported; set version=Version.v2")
        raw = await self._t.request_json("POST", "/sympheny-app/projects", json=dump(request))
        envelope = ResponseDtoProjectResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def get(self, project_guid: str, *, include_analyses: bool | None = None) -> ProjectDetailResponseDto:
        """Get project details. ``GET /sympheny-app/projects/{guid}``"""
        params = {"includeAnalyses": include_analyses} if include_analyses is not None else None
        raw = await self._t.request_json("GET", f"/sympheny-app/projects/{project_guid}", params=params)
        envelope = ResponseDtoProjectDetailResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, project_guid: str) -> ProjectSummaryResponseDto:
        """Delete a project; returns the remaining projects. ``DELETE /sympheny-app/projects/{guid}``"""
        raw = await self._t.request_json("DELETE", f"/sympheny-app/projects/{project_guid}")
        envelope = ResponseDtoProjectSummaryResponseDto.model_validate(raw)
        return unwrap(envelope.data)
