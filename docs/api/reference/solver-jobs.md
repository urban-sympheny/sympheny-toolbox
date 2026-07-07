<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Solver jobs

## Post Solver Jobs { #operation-post_solver_jobs_sense_api_ext_solver_jobs_post }

```
POST /sense-api/ext/solver/jobs
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solver_jobs.submit()`](../../sdk/reference/solver_jobs.md#method-solver_jobs-submit).

**Request body** (array of `PostSolverJobExt`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `objective1` | `ObjectiveFunction` | yes | One of: `MIN_LIFE_CYCLE_COST`, `MIN_ANNUALIZED_COST`, `MIN_CO2_EMISSIONS`, `MIN_INVESTMENT`, `MIN_OM`, `MIN_FUEL_IMPORTS`, `MIN_REPLACEMENT`, `MAX_EXPORTS`, `MAX_SALVAGE`. |
| `objective2` | `ObjectiveFunction`, nullable | no |  |
| `scenarioGuid` | string, nullable | no |  |
| `scenarioName` | string, nullable | no |  |
| `temporalResolution` | `TemporalResolution` | yes | One of: `LOW`, `MEDIUM`, `HIGH`, `FULL`. |
| `points` | integer | yes |  |
| `timeLimit` | integer | yes |  |
| `mipGap` | number | yes |  |
| `inputFileId` | string (uuid4), nullable | no |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sense-api/ext/solver/jobs" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "name": "string",
    "objective1": "MIN_LIFE_CYCLE_COST",
    "objective2": "MIN_LIFE_CYCLE_COST",
    "scenarioGuid": "string",
    "scenarioName": "string",
    "temporalResolution": "LOW",
    "points": 0,
    "timeLimit": 0,
    "mipGap": 0.0,
    "inputFileId": "string"
  }
]'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | array of `SolverJob` |
| 400 | Bad Request | `CustomHTTPException` |
| 401 | Unauthorized | `CustomHTTPException` |
| 404 | Not Found | `CustomHTTPException` |
| 409 | Conflict | `CustomHTTPException` |
| 413 | Request Entity Too Large | `CustomHTTPException` |
| 500 | Internal Server Error | `CustomHTTPException` |
| 422 | Validation Error | `HTTPValidationError` |

**Example response** (200)

```json
[
  {
    "status": "VALIDATING",
    "statusMsg": "Validating",
    "batchId": "string",
    "pointsCompleted": 0,
    "started": "2026-01-01T00:00:00Z",
    "terminated": "2026-01-01T00:00:00Z",
    "infeasibilityInfo": "string",
    "name": "string",
    "objective1": "MIN_LIFE_CYCLE_COST",
    "objective2": "MIN_LIFE_CYCLE_COST",
    "scenarioGuid": "string",
    "scenarioName": "string",
    "temporalResolution": "LOW",
    "points": 0,
    "timeLimit": 0,
    "mipGap": 0.0,
    "accountGuid": "string",
    "organizationId": "string",
    "subscriptionId": "string",
    "id": "string",
    "created": "2026-01-01T00:00:00Z"
  }
]
```

## Post Get Scenario Jobs { #operation-post_get_scenario_jobs_sense_api_ext_solver_jobs_get_scenarios_post }

```
POST /sense-api/ext/solver/jobs/get-scenarios
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solver_jobs.list_for_scenarios()`](../../sdk/reference/solver_jobs.md#method-solver_jobs-list_for_scenarios).

**Request body** (`GetScenarioGuidsPage`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scenarioGuids` | array of string | yes |  |
| `limit` | integer | no | Default: `200`. |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sense-api/ext/solver/jobs/get-scenarios" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "scenarioGuids": [
    "string"
  ],
  "limit": 200
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | array of `SolverJob` |
| 400 | Bad Request | `CustomHTTPException` |
| 401 | Unauthorized | `CustomHTTPException` |
| 404 | Not Found | `CustomHTTPException` |
| 409 | Conflict | `CustomHTTPException` |
| 413 | Request Entity Too Large | `CustomHTTPException` |
| 500 | Internal Server Error | `CustomHTTPException` |
| 422 | Validation Error | `HTTPValidationError` |

**Example response** (200)

```json
[
  {
    "status": "VALIDATING",
    "statusMsg": "Validating",
    "batchId": "string",
    "pointsCompleted": 0,
    "started": "2026-01-01T00:00:00Z",
    "terminated": "2026-01-01T00:00:00Z",
    "infeasibilityInfo": "string",
    "name": "string",
    "objective1": "MIN_LIFE_CYCLE_COST",
    "objective2": "MIN_LIFE_CYCLE_COST",
    "scenarioGuid": "string",
    "scenarioName": "string",
    "temporalResolution": "LOW",
    "points": 0,
    "timeLimit": 0,
    "mipGap": 0.0,
    "accountGuid": "string",
    "organizationId": "string",
    "subscriptionId": "string",
    "id": "string",
    "created": "2026-01-01T00:00:00Z"
  }
]
```

## Get Solver Jobs Usage { #operation-get_solver_jobs_usage_sense_api_ext_solver_jobs_usage_get }

```
GET /sense-api/ext/solver/jobs/usage
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solver_jobs.usage()`](../../sdk/reference/solver_jobs.md#method-solver_jobs-usage).

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sense-api/ext/solver/jobs/usage" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | `GetUsageExt` |
| 400 | Bad Request | `CustomHTTPException` |
| 401 | Unauthorized | `CustomHTTPException` |
| 404 | Not Found | `CustomHTTPException` |
| 409 | Conflict | `CustomHTTPException` |
| 413 | Request Entity Too Large | `CustomHTTPException` |
| 500 | Internal Server Error | `CustomHTTPException` |

**Example response** (200)

```json
{
  "subscription": {
    "totalCountOverage": 0,
    "totalMinutesOverage": 0,
    "weeklyCountOverage": 0,
    "weeklyMinutesOverage": 0,
    "totalCount": 0,
    "totalMinutes": 0,
    "currentWeekCount": 0,
    "currentWeekMinutes": 0
  },
  "user": {
    "totalCount": 0,
    "totalMinutes": 0,
    "currentWeekCount": 0,
    "currentWeekMinutes": 0,
    "historyCount": 0
  }
}
```

## Get Solver Job { #operation-get_solver_job_sense_api_ext_solver_jobs__id__get }

```
GET /sense-api/ext/solver/jobs/{id}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solver_jobs.get()`](../../sdk/reference/solver_jobs.md#method-solver_jobs-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string (uuid) | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sense-api/ext/solver/jobs/{id}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | `GetSolverJobExt` |
| 400 | Bad Request | `CustomHTTPException` |
| 401 | Unauthorized | `CustomHTTPException` |
| 404 | Not Found | `CustomHTTPException` |
| 409 | Conflict | `CustomHTTPException` |
| 413 | Request Entity Too Large | `CustomHTTPException` |
| 500 | Internal Server Error | `CustomHTTPException` |
| 422 | Validation Error | `HTTPValidationError` |

**Example response** (200)

```json
{
  "status": "VALIDATING",
  "statusMsg": "Validating",
  "batchId": "string",
  "pointsCompleted": 0,
  "started": "2026-01-01T00:00:00Z",
  "terminated": "2026-01-01T00:00:00Z",
  "infeasibilityInfo": "string",
  "name": "string",
  "objective1": "MIN_LIFE_CYCLE_COST",
  "objective2": "MIN_LIFE_CYCLE_COST",
  "scenarioGuid": "string",
  "scenarioName": "string",
  "temporalResolution": "LOW",
  "points": 0,
  "timeLimit": 0,
  "mipGap": 0.0,
  "accountGuid": "string",
  "organizationId": "string",
  "subscriptionId": "string",
  "id": "string",
  "created": "2026-01-01T00:00:00Z",
  "inputFile": "string",
  "outputFile": "string"
}
```

## Delete Solver Job { #operation-delete_solver_job_sense_api_ext_solver_jobs__id__delete }

```
DELETE /sense-api/ext/solver/jobs/{id}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solver_jobs.delete()`](../../sdk/reference/solver_jobs.md#method-solver_jobs-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string (uuid) | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sense-api/ext/solver/jobs/{id}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | string |
| 400 | Bad Request | `CustomHTTPException` |
| 401 | Unauthorized | `CustomHTTPException` |
| 404 | Not Found | `CustomHTTPException` |
| 409 | Conflict | `CustomHTTPException` |
| 413 | Request Entity Too Large | `CustomHTTPException` |
| 500 | Internal Server Error | `CustomHTTPException` |
| 422 | Validation Error | `HTTPValidationError` |

**Example response** (200)

```json
"string"
```

## Stop Job { #operation-stop_job_sense_api_ext_solver_jobs__id__stop_put }

```
PUT /sense-api/ext/solver/jobs/{id}/stop
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.solver_jobs.stop()`](../../sdk/reference/solver_jobs.md#method-solver_jobs-stop).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string (uuid) | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sense-api/ext/solver/jobs/{id}/stop" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | Successful Response | string |
| 400 | Bad Request | `CustomHTTPException` |
| 401 | Unauthorized | `CustomHTTPException` |
| 404 | Not Found | `CustomHTTPException` |
| 409 | Conflict | `CustomHTTPException` |
| 413 | Request Entity Too Large | `CustomHTTPException` |
| 500 | Internal Server Error | `CustomHTTPException` |
| 422 | Validation Error | `HTTPValidationError` |

**Example response** (200)

```json
"string"
```
