<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Scenarios

## List scenarios { #operation-listScenarios }

```
GET /sympheny-app/analysis/{guid}/scenario
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.scenarios.list()`](../../sdk/reference/scenarios.md#method-scenarios-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/analysis/{guid}/scenario" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListFScenarioResponseDto` |

**Example response** (200)

```json
{
  "data": [
    {
      "scenarioGuid": "string",
      "scenarioName": "string",
      "updated": "2026-01-01T00:00:00Z",
      "readyForExecution": true,
      "preparingExecutionV2": true,
      "masterScenarioGuid": "string",
      "projectGuid": "string",
      "projectName": "string",
      "analysisGuid": "string",
      "analysisName": "string",
      "enymap": {
        "length": 0,
        "interestRate": 0.0,
        "exchangeCurrency": "string",
        "exchangeRate": 0.0,
        "scope": "BUILDING_DEVELOPMENTS",
        "technologies": [
          "PV"
        ],
        "demands": [
          "HOT_WATER"
        ],
        "imports": [
          "ELECTRICITY"
        ],
        "exports": [
          "HEAT_AMBIENT"
        ],
        "multiHubs": true
      },
      "variant": true
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Create new scenario { #operation-createNewScenario }

```
POST /sympheny-app/analysis/{guid}/scenario
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.scenarios.create()`](../../sdk/reference/scenarios.md#method-scenarios-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`ScenarioRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scenarioName` | string | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/analysis/{guid}/scenario" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "scenarioName": "string"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoScenarioResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "scenarioGuid": "string",
    "scenarioName": "string",
    "updated": "2026-01-01T00:00:00Z",
    "readyForExecution": true,
    "preparingExecutionV2": true,
    "masterScenarioGuid": "string",
    "projectGuid": "string",
    "projectName": "string",
    "analysisGuid": "string",
    "analysisName": "string",
    "enymap": {
      "length": 0,
      "interestRate": 0.0,
      "exchangeCurrency": "string",
      "exchangeRate": 0.0,
      "scope": "BUILDING_DEVELOPMENTS",
      "technologies": [
        "PV"
      ],
      "demands": [
        "HOT_WATER"
      ],
      "imports": [
        "ELECTRICITY"
      ],
      "exports": [
        "HEAT_AMBIENT"
      ],
      "multiHubs": true
    },
    "variant": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Get scenario { #operation-getScenario }

```
GET /sympheny-app/scenario/{scenarioGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.scenarios.get()`](../../sdk/reference/scenarios.md#method-scenarios-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenario/{scenarioGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoScenarioResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "scenarioGuid": "string",
    "scenarioName": "string",
    "updated": "2026-01-01T00:00:00Z",
    "readyForExecution": true,
    "preparingExecutionV2": true,
    "masterScenarioGuid": "string",
    "projectGuid": "string",
    "projectName": "string",
    "analysisGuid": "string",
    "analysisName": "string",
    "enymap": {
      "length": 0,
      "interestRate": 0.0,
      "exchangeCurrency": "string",
      "exchangeRate": 0.0,
      "scope": "BUILDING_DEVELOPMENTS",
      "technologies": [
        "PV"
      ],
      "demands": [
        "HOT_WATER"
      ],
      "imports": [
        "ELECTRICITY"
      ],
      "exports": [
        "HEAT_AMBIENT"
      ],
      "multiHubs": true
    },
    "variant": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Delete scenario { #operation-deleteScenario }

```
DELETE /sympheny-app/scenario/{scenarioGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.scenarios.delete()`](../../sdk/reference/scenarios.md#method-scenarios-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenario/{scenarioGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStatus` |

**Example response** (200)

```json
{
  "data": {
    "code": "string",
    "desc": "string",
    "message": "string"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Copy scenario { #operation-copyScenario }

```
PUT /sympheny-app/scenarios/copy/{scenarioGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.scenarios.copy()`](../../sdk/reference/scenarios.md#method-scenarios-copy).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `analysisDestinationGuid` | query | string | no |  |
| `name` | query | string | no |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/copy/{scenarioGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoScenarioResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "scenarioGuid": "string",
    "scenarioName": "string",
    "updated": "2026-01-01T00:00:00Z",
    "readyForExecution": true,
    "preparingExecutionV2": true,
    "masterScenarioGuid": "string",
    "projectGuid": "string",
    "projectName": "string",
    "analysisGuid": "string",
    "analysisName": "string",
    "enymap": {
      "length": 0,
      "interestRate": 0.0,
      "exchangeCurrency": "string",
      "exchangeRate": 0.0,
      "scope": "BUILDING_DEVELOPMENTS",
      "technologies": [
        "PV"
      ],
      "demands": [
        "HOT_WATER"
      ],
      "imports": [
        "ELECTRICITY"
      ],
      "exports": [
        "HEAT_AMBIENT"
      ],
      "multiHubs": true
    },
    "variant": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Rename scenario { #operation-renameScenario }

```
PUT /sympheny-app/scenarios/{scenarioGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.scenarios.rename()`](../../sdk/reference/scenarios.md#method-scenarios-rename).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`ScenarioRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scenarioName` | string | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "scenarioName": "string"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoScenarioResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "scenarioGuid": "string",
    "scenarioName": "string",
    "updated": "2026-01-01T00:00:00Z",
    "readyForExecution": true,
    "preparingExecutionV2": true,
    "masterScenarioGuid": "string",
    "projectGuid": "string",
    "projectName": "string",
    "analysisGuid": "string",
    "analysisName": "string",
    "enymap": {
      "length": 0,
      "interestRate": 0.0,
      "exchangeCurrency": "string",
      "exchangeRate": 0.0,
      "scope": "BUILDING_DEVELOPMENTS",
      "technologies": [
        "PV"
      ],
      "demands": [
        "HOT_WATER"
      ],
      "imports": [
        "ELECTRICITY"
      ],
      "exports": [
        "HEAT_AMBIENT"
      ],
      "multiHubs": true
    },
    "variant": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
