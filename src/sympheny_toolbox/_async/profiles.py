"""Operations on profiles of the Sympheny platform API (``profile-controller``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._envelope import dump, unwrap
from sympheny_toolbox.models import (
    ProfileDetailsResponseDto,
    ProfileJsonRequestDto,
    ProfileRequestDtoPUT,
    ProfileResponseDto,
    ResponseDtoListProfileResponseDto,
    ResponseDtoProfileDetailsResponseDto,
    ResponseDtoProfileResponseDto,
)


if TYPE_CHECKING:
    from sympheny_toolbox._async._transport import AsyncTransport


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

    async def update(self, scenario_guid: str, profile_id: int, request: ProfileRequestDtoPUT) -> ProfileDetailsResponseDto:
        """Update a profile. ``PUT /sympheny-app/v2/scenarios/{scenarioGuid}/profiles-json/{profileId}``"""
        raw = await self._t.request_json("PUT", f"/sympheny-app/v2/scenarios/{scenario_guid}/profiles-json/{profile_id}", json=dump(request))
        envelope = ResponseDtoProfileDetailsResponseDto.model_validate(raw)
        return unwrap(envelope.data)

    async def delete(self, scenario_guid: str, profile_id: int) -> None:
        """Delete a profile. ``DELETE /sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}``"""
        await self._t.request_json("DELETE", f"/sympheny-app/scenarios/{scenario_guid}/profiles/{profile_id}")
