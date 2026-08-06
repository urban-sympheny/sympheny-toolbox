"""The Sympheny API client (asynchronous)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sympheny_toolbox._async._transport import DEFAULT_BASE_URL, DEV_BASE_URL, AsyncTransport
from sympheny_toolbox._async.analyses import AsyncAnalyses
from sympheny_toolbox._async.conversion_technologies import AsyncConversionTechnologies
from sympheny_toolbox._async.energy_carriers import AsyncEnergyCarriers
from sympheny_toolbox._async.energy_demands import AsyncEnergyDemands
from sympheny_toolbox._async.hubs import AsyncHubs
from sympheny_toolbox._async.impex import AsyncImpex
from sympheny_toolbox._async.intra_hub_network_links import AsyncIntraHubNetworkLinks
from sympheny_toolbox._async.network_links import AsyncNetworkLinks
from sympheny_toolbox._async.network_technologies import AsyncNetworkTechnologies
from sympheny_toolbox._async.profiles import AsyncProfiles
from sympheny_toolbox._async.projects import AsyncProjects
from sympheny_toolbox._async.scenarios import AsyncScenarios
from sympheny_toolbox._async.solar_resources import AsyncSolarResources
from sympheny_toolbox._async.solver_jobs import AsyncSolverJobs
from sympheny_toolbox._async.stages import AsyncStages
from sympheny_toolbox._async.storage_technologies import AsyncStorageTechnologies
from sympheny_toolbox._async.technology_packages import AsyncTechnologyPackages
from sympheny_toolbox._async.users import AsyncUsers


if TYPE_CHECKING:
    from types import TracebackType


class AsyncSympheny:
    """Sympheny API client (asynchronous variant).

    Authenticates with email/password credentials against the Sympheny API and
    exposes the documented endpoints as typed resource groups, e.g.
    ``client.projects.list()``.

    Args:
        username: Sympheny account email address.
        password: Sympheny account password.
        is_dev: Use the development environment instead of production.
        base_url: Override the API base URL entirely (takes precedence over ``is_dev``).
        timeout: Request timeout in seconds.
    """

    def __init__(
        self,
        username: str,
        password: str,
        *,
        is_dev: bool = False,
        base_url: str | None = None,
        timeout: float = 30.0,
    ) -> None:
        if base_url is None:
            base_url = DEV_BASE_URL if is_dev else DEFAULT_BASE_URL
        self.is_dev = is_dev
        self._transport = AsyncTransport(username, password, base_url=base_url, timeout=timeout)

        self.projects = AsyncProjects(self._transport)
        self.analyses = AsyncAnalyses(self._transport)
        self.scenarios = AsyncScenarios(self._transport)
        self.stages = AsyncStages(self._transport)
        self.hubs = AsyncHubs(self._transport)
        self.energy_carriers = AsyncEnergyCarriers(self._transport)
        self.impex = AsyncImpex(self._transport)
        self.profiles = AsyncProfiles(self._transport)
        self.energy_demands = AsyncEnergyDemands(self._transport)
        self.solar_resources = AsyncSolarResources(self._transport)
        self.conversion_technologies = AsyncConversionTechnologies(self._transport)
        self.storage_technologies = AsyncStorageTechnologies(self._transport)
        self.technology_packages = AsyncTechnologyPackages(self._transport)
        self.network_technologies = AsyncNetworkTechnologies(self._transport)
        self.network_links = AsyncNetworkLinks(self._transport)
        self.intra_hub_network_links = AsyncIntraHubNetworkLinks(self._transport)
        self.solver_jobs = AsyncSolverJobs(self._transport)
        self.users = AsyncUsers(self._transport)

    @property
    def base_url(self) -> str:
        """The API base URL this client talks to."""
        return self._transport.base_url

    async def aclose(self) -> None:
        """Close the underlying HTTP connection pool."""
        await self._transport.aclose()

    async def __aenter__(self) -> AsyncSympheny:
        return self

    async def __aexit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None:
        await self.aclose()
