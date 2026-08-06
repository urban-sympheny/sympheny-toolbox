---
tags:
  - sdk
  - workflow
---

# Workflows

The [SDK reference](../reference/projects.md) documents one method at a time. These
guides string those methods together into the end-to-end flows you actually run: take a
scenario, optimize it, and read the results back.

## The end-to-end flow

Most automation follows the same two steps, each covered by one guide:

1. **[Run a solver job](run-solver-job.md)**: submit the scenario to the solver and
   poll until the optimization finishes.
2. **[Download the results](download-results.md)**: fetch the result file of a finished
   job, or link straight to its results dashboard.

Both start from a scenario GUID. Build the scenario with the resource groups on the
client (`client.scenarios`, `client.hubs`, `client.conversion_technologies`, …), or model
it in the [web app](../../web-app/index.md) and take the GUID from there.

## Prerequisites

- The SDK installed and a Sympheny account. See the [SDK overview](../index.md).
- Familiarity with the Sympheny domain model helps; the
  [concepts](../../web-app/concepts/index.md) pages define hubs, energy carriers,
  demands, and technologies once, and the reference pages link back to them.

## Sync or async

Every example has a **Sync** and an **Async** tab, and your choice persists across pages.
The two are identical apart from `Sympheny`/`AsyncSympheny`, `await`, and `time.sleep`
vs `asyncio.sleep`.

!!! note "Convenience helpers are sync-only"
    The `sympheny_toolbox.workflows` module bundles several of these flows into
    one-line helpers (for example `workflows.execute_scenario`). They are built on the
    synchronous client and have no async twin. Each guide points them out where they
    apply, and shows the client-level calls you would use on the async client.
