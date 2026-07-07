---
tags:
  - sdk
  - workflow
---

# Workflows

The [SDK reference](../reference/projects.md) documents one method at a time. These
guides string those methods together into the end-to-end flows you actually run: take a
scenario from an Excel workbook, optimize it, and read the results back.

## The end-to-end flow

Most automation follows the same three steps, each covered by one guide:

1. **[Create a scenario from Excel](scenario-from-excel.md)** — upload a filled-in
   scenario workbook and turn it into a scenario you can execute.
2. **[Run a solver job](run-solver-job.md)** — submit the scenario to the solver and
   poll until the optimization finishes.
3. **[Download the results](download-results.md)** — fetch the result file of a finished
   job, or link straight to its results dashboard.

You can also start in the middle: if you already modelled a scenario in the
[web application](../../web-app/index.md), skip to step 2 with its scenario GUID.

## Prerequisites

- The SDK installed and a Sympheny account — see the [SDK overview](../index.md).
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
    synchronous client and have no async twin — each guide points them out where they
    apply, and shows the client-level calls you would use on the async client.
