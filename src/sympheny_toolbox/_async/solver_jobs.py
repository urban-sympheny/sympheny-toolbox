"""Operations on solver jobs of the Sympheny solver API (``External Solver Jobs``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import TypeAdapter

from sympheny_toolbox._envelope import dump
from sympheny_toolbox.models import (
    GetScenarioGuidsPage,
    GetSolverJobExt,
    GetUsageExt,
    JobStatus,
    PostSolverJobExt,
    SolverJob,
)


if TYPE_CHECKING:
    from uuid import UUID

    from sympheny_toolbox._async._transport import AsyncTransport


_SOLVER_JOB_LIST = TypeAdapter(list[SolverJob])


class AsyncSolverJobs:
    """Operations on solver jobs (``External Solver Jobs``)."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._t = transport

    async def submit(self, jobs: list[PostSolverJobExt]) -> list[SolverJob]:
        """Submit one or more solver jobs for execution. ``POST /sense-api/ext/solver/jobs``"""
        raw = await self._t.request_json("POST", "/sense-api/ext/solver/jobs", json=[dump(job) for job in jobs])
        return _SOLVER_JOB_LIST.validate_python(raw)

    async def list_for_scenarios(self, scenario_guids: list[str], *, limit: int = 200, status: JobStatus | None = None) -> list[SolverJob]:
        """List solver jobs for the given scenarios, optionally filtered by status. ``POST /sense-api/ext/solver/jobs/get-scenarios``"""
        # Built via model_validate with alias keys: type checkers disagree on the synthesized
        # __init__ parameter names of aliased fields (mypy plugin: field names; pyright/ty: aliases).
        request = GetScenarioGuidsPage.model_validate({"scenarioGuids": scenario_guids, "limit": limit})
        raw = await self._t.request_json("POST", "/sense-api/ext/solver/jobs/get-scenarios", json=dump(request))
        jobs = _SOLVER_JOB_LIST.validate_python(raw)
        if status is not None:
            jobs = [job for job in jobs if job.status == status]
        return jobs

    async def usage(self) -> GetUsageExt:
        """Get solver usage of the current subscription and user. ``GET /sense-api/ext/solver/jobs/usage``"""
        raw = await self._t.request_json("GET", "/sense-api/ext/solver/jobs/usage")
        return GetUsageExt.model_validate(raw)

    async def get(self, job_id: str | UUID) -> GetSolverJobExt:
        """Get a solver job by id. ``GET /sense-api/ext/solver/jobs/{id}``"""
        raw = await self._t.request_json("GET", f"/sense-api/ext/solver/jobs/{job_id}")
        return GetSolverJobExt.model_validate(raw)

    async def delete(self, job_id: str | UUID) -> str:
        """Delete a solver job. ``DELETE /sense-api/ext/solver/jobs/{id}``"""
        raw = await self._t.request_json("DELETE", f"/sense-api/ext/solver/jobs/{job_id}")
        return str(raw)

    async def stop(self, job_id: str | UUID) -> str:
        """Stop a running solver job. ``PUT /sense-api/ext/solver/jobs/{id}/stop``"""
        raw = await self._t.request_json("PUT", f"/sense-api/ext/solver/jobs/{job_id}/stop")
        return str(raw)
