# Known API issues & client workarounds

_Last updated: 2026-07-04._

A living record of Sympheny API behaviors that surprised us, and the client-side workarounds you can
apply. Each item is a backend or OpenAPI-spec matter rather than a client bug; where the SDK already
handles it, that is noted. Entries are removed once the API is fixed. Each has a **Status**:
`Open` (needs a client-side workaround) or `Fixed in SDK` (handled for you by `sympheny-toolbox`).

---

## 1. PUT/update endpoints reject the `created`/`updated` timestamps they themselves return

**Status: Open** (client-side workaround required). **Severity: high — blocks every update round-trip.**

**Endpoints (all `*Response*` DTOs reused as PUT bodies):**
- `PUT /sympheny-app/v2_1/scenarios/impex/{guid}` — `editImpexV2_1`
- `PUT /sympheny-app/v2_1/scenarios/conversion-technologies/{guid}` — `updateConversionTechnology`
- `PUT /sympheny-app/v2_2/scenarios/storage-technologies/{guid}` — `updateStorageTechnologyV2_2`
- `PUT /sympheny-app/v2_1/scenarios/network-technologies/{guid}` — `updateNetworkTechnologyV2_1`
- `PUT /sympheny-app/v2/scenarios/hubs/{guid}` — `editHub` (same DTO shape)

**Symptom.** The normal update flow is: `GET` an object, change one field, `PUT` it back. But the
GET returns audit timestamps as ISO-8601 strings with **microsecond** precision, and the PUT's own
Jackson parser then refuses to parse them:

```
HTTP 400 ESP_400 "JSON parse error: Cannot deserialize value of type `java.time.ZonedDateTime`
from String "2026-07-03T17:00:38.996000Z": Failed to deserialize java.time.ZonedDateTime:
Text '2026-07-03T17:00:38.996000Z' could not be parsed at index 23"
```

Index 23 is the start of the `.996000` fraction — the parser is configured for a format that does
not accept 6-digit fractional seconds + `Z`.

**These fields are server-managed audit metadata; the PUT request should not carry them at all.**
The failing fields are not only the top-level `created`/`updated` but also nested ones:
`hubs[].hubCreated`, `hubs[].hubUpdated`, and `energyCarrier.created` (the last is what actually
broke the impex update — it is one level deeper than an obvious top-level scrub would reach).

**Recommended fix (backend + spec).**
1. **Preferred:** give these PUT endpoints a dedicated *request* DTO that **omits** `created`,
   `updated`, `hubCreated`, `hubUpdated`, and any nested `created`/`updated` (e.g. on
   `energyCarrier`). The request contract should never contain server-owned audit timestamps.
   Update `specs/sympheny_openapi.json` so the `requestBody` schema for each endpoint above no longer
   lists those fields.
2. **Alternatively / additionally:** make the deserializer tolerant of the exact format the API
   emits (ISO-8601 with 6-digit fractional seconds and `Z`), and ignore audit fields on input.

**Client workaround.** Before re-submitting a fetched object, recursively null out **every** `datetime`
field at any depth (top-level `created`/`updated`, `hubs[].hubCreated`/`hubUpdated`, nested
`energyCarrier.created`, …); the client's serializer drops `None`s, so the audit fields are omitted.

---

## 2. `copyScenario` ignores `name` when copying into another analysis, and doesn't deduplicate (→ 409)

**Status: Open** (client-side workaround required, using `scenarios.rename`). **Severity: high —
copying one source into an analysis more than once fails.**

**Endpoint:** `PUT /sympheny-app/scenarios/copy/{scenarioGuid}` — `copyScenario`, documented query
params `analysisDestinationGuid` and `name` (both `in: query`, `type: string`).

**Observed behavior (the copy is synchronous — the response is final).** The `name` query param is
honored **only when `analysisDestinationGuid` is omitted** (the copy stays in the source's analysis):

- **No `analysisDestinationGuid`, `name="X"`** → the copy is created in the source's analysis and named
  `X` (name **respected**).
- **`analysisDestinationGuid` set, `name="X"`** → `name` is **ignored**; the copy takes the *source's*
  name verbatim and is **not** deduplicated. Copying the same source into that analysis a second time
  therefore violates the unique constraint:

```
HTTP 409 ESP_409 constraint [scenarios_scenario_name_analysis_id_key]
org.hibernate.exception.ConstraintViolationException: could not execute statement
```

**A rename endpoint exists on the backend but is missing from the OpenAPI export.**
`PUT /sympheny-app/scenarios/{scenarioGuid}` (`renameScenario`, body `ScenarioRequestDto` =
`{scenarioName}`) is present in the legacy Swagger 2.0 export (`specs/webapp_legacy_openapi.json`) but
**absent from the current webapp export**. It is re-added by hand in `scripts/merge_openapi.py` (exactly
as `copyScenario` is), so the published spec — and the SDK's `scenarios.rename` — expose it.

**Recommended fix (backend + spec).** (a) Add `renameScenario` back to the `webapp_openapi.json`
export so it isn't a manual patch. (b) Ideally, also honor the `name` query param on `copyScenario`
**regardless of `analysisDestinationGuid`** (and deduplicate within the destination analysis) so a
named copy into another analysis is one call instead of copy-then-rename.

**Client workaround.** Copy into the target analysis **without** a name (the server assigns the source
name), then call `scenarios.rename` to set the wanted name **before the next copy of the same source
runs**, so the source name is never doubly occupied — one copy + one rename.

---

## 3. `deleteAnalysis` and `deleteScenario` return `data: null` on success

**Status: Fixed in SDK** (`sympheny-toolbox` ≥ 2.1.0). **Severity: low — cosmetic contract mismatch.**

**Endpoints:**
- `DELETE /sympheny-app/analysis/{analysisGuid}` — `deleteAnalysis`
- `DELETE /sympheny-app/scenario/{scenarioGuid}` — `deleteScenario`

**Symptom.** On a successful delete the response envelope is `{"data": null, ...}`, unlike sibling
endpoints that return a payload. A strict client that treats a missing `data` as an error (the usual
`unwrap`) raises on a perfectly successful call — this surfaced as an `UnexpectedResponseError` while
deleting a scenario.

**Recommended fix (spec).** Either return a `Status` payload on success, or document in
`ResponseDtoStatus` that `data` is nullable for these endpoints.

**Client workaround in place.** SDK `Analyses.delete` and `Scenarios.delete` treat a null `data` as an
empty `Status` (`src/sympheny_toolbox/_async/projects.py` and `.../scenarios.py`, regenerated into
`_sync/`). Handled at the SDK level.

---

## 4. Conversion-carrier request requires fields the response returns as `null`

**Status: Open** (client-side workaround required). **Severity: medium — blocks rebuilding a
technology from its own detail response.**

**DTO:** `ConversionCarrierRequestDtoV2` (used when re-creating conversion technologies).

**Symptom.** `fixedInputShare`, `outputEfficiency`, and `primary` are **required** (non-nullable) on
the request DTO, but the corresponding detail *response* returns them as `null` for one-directional
carriers (an input-only carrier has no `outputEfficiency`, etc.). Faithfully copying a fetched
technology back therefore fails validation on fields the server itself left null.

**Recommended fix (spec/backend).** Make `fixedInputShare` / `outputEfficiency` / `primary` nullable
(or supply server-side defaults) on the request DTO so a response object round-trips cleanly.

**Client workaround.** When rebuilding a carrier, default `fixedInputShare` / `outputEfficiency` to
`0.0` and `primary` to `False` where the fetched value is `null`.

---

## 5. Cost/CO2/capacity fields reject values with more than 5 decimal places

**Status: Open** (client-side workaround required). **Severity: low — a real DB constraint, but easy
to trip and not advertised in the spec.**

**Fields:** cost/CO2/capacity numerics (e.g. `fixedInvestmentCost`, `variableInvestmentCost`,
`variableEmbodiedCo2`, mode/storage `capacity`) on the conversion/storage/impex/network update DTOs.

**Symptom.** These are stored as `NUMERIC(16, 5)`, so any value serialized with more than 5 fractional
digits is rejected — which ordinary IEEE-754 floats routinely produce (`0.1 + 0.2`,
`249.99999999999997`, spreadsheet-derived values):

```
HTTP 400 ESP_400 "fixedInvestmentCost: Invalid NUMERIC. Max precision=16, max scale=5"
```

**Recommended fix (spec/backend).** Document the precision/scale in the schema (`multipleOf: 0.00001`
or a description), and ideally round on the server instead of rejecting.

**Client workaround.** Quantize numeric values to 5 decimals before sending, e.g.
`float(Decimal(str(value)).quantize(Decimal("0.00001")))`.

---

## Summary for the spec update (`specs/sympheny_openapi.json`)

| # | Endpoint / DTO | Change |
|---|---|---|
| 1 | `editImpexV2_1`, `updateConversionTechnology`, `updateStorageTechnologyV2_2`, `updateNetworkTechnologyV2_1`, `editHub` | Request body must **not** include `created`/`updated`/`hubCreated`/`hubUpdated`/nested `created` |
| 2 | `copyScenario` / `renameScenario` | Add `renameScenario` (`PUT /scenarios/{scenarioGuid}`) back to the `webapp_openapi.json` export; ideally also honor `copyScenario`'s `name` even with `analysisDestinationGuid` set (with dedup) |
| 3 | `deleteAnalysis`, `deleteScenario` | Document `data` as nullable on success (or return `Status`) |
| 4 | `ConversionCarrierRequestDtoV2` | Make `fixedInputShare`/`outputEfficiency`/`primary` nullable |
| 5 | cost/CO2/capacity numerics | Document `NUMERIC(16, 5)` precision/scale in the schema; ideally round server-side instead of rejecting |
