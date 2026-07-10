<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Analyses

## Delete analysis { #operation-deleteAnalysis }

```
DELETE /sympheny-app/analysis/{analysisGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.analyses.delete()`](../../sdk/reference/analyses.md#method-analyses-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `analysisGuid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/analysis/{analysisGuid}" \
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

## List 2 { #operation-list_2 }

```
GET /sympheny-app/projects/{guid}/analyses
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.analyses.list()`](../../sdk/reference/analyses.md#method-analyses-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/projects/{guid}/analyses" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `PagedResponseAnalysisResponseDto` |

**Example response** (200)

```json
{
  "data": [
    {
      "analysisGuid": "string",
      "analysisName": "string",
      "created": "2026-01-01T00:00:00Z",
      "updated": "2026-01-01T00:00:00Z",
      "scenarios": [
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
      ]
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  },
  "totalElements": 0,
  "totalPages": 0,
  "hasNext": true
}
```

## Create new analysis { #operation-createNewAnalysis }

```
POST /sympheny-app/projects/{guid}/analyses
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.analyses.create()`](../../sdk/reference/analyses.md#method-analyses-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`AnalysisRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `analysisName` | string | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/projects/{guid}/analyses" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "analysisName": "string"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoAnalysisResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "analysisGuid": "string",
    "analysisName": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "scenarios": [
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
    ]
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## View analysis details { #operation-viewAnalysisDetails }

```
GET /sympheny-app/projects/{guid}/analysis/{analysisGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.analyses.get()`](../../sdk/reference/analyses.md#method-analyses-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |
| `analysisGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/projects/{guid}/analysis/{analysisGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoAnalysisDetailsResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "analysisGuid": "string",
    "analysisName": "string",
    "executionStatus": "IN_SPECIFICATION",
    "executionInProgress": true,
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "coverImage": "string",
    "projectName": "string",
    "scenarios": [
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
    "executionOptions": {
      "objective1": "string",
      "objective2": "string",
      "numberOfParetoPoints": 0,
      "scenarios": [
        "string"
      ]
    },
    "results": {
      "executionSubmitted": "2026-01-01T00:00:00Z",
      "scenarios": [
        {
          "scenarioName": "string",
          "status": "IN_SPECIFICATION",
          "statusMessage": "string",
          "paretoPointsCompleted": "string",
          "inputFilepath": "string",
          "outputFilepath": "string"
        }
      ],
      "dashboardUrl": "string"
    },
    "projectGuid": "string"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
