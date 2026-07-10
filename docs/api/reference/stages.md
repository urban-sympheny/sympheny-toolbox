<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Stages

## Get 1 { #operation-get_1 }

```
GET /sympheny-app/scenarios/stages/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.stages.get()`](../../sdk/reference/stages.md#method-stages-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/stages/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStageResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "name": "string",
    "length": 0,
    "interestRate": 0.0,
    "inflationRate": 0.0,
    "index": 0,
    "guid": "00000000-0000-0000-0000-000000000000"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## List { #operation-list }

```
GET /sympheny-app/scenarios/{scenarioGuid}/stages
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.stages.list()`](../../sdk/reference/stages.md#method-stages-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/stages" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListStageResponseDto` |

**Example response** (200)

```json
{
  "data": [
    {
      "name": "string",
      "length": 0,
      "interestRate": 0.0,
      "inflationRate": 0.0,
      "index": 0,
      "guid": "00000000-0000-0000-0000-000000000000"
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Create { #operation-create }

```
POST /sympheny-app/scenarios/{scenarioGuid}/stages
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.stages.create()`](../../sdk/reference/stages.md#method-stages-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`StageRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `length` | integer (int32) | yes |  |
| `interestRate` | number, nullable | no |  |
| `inflationRate` | number, nullable | no |  |
| `index` | integer (int32) | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/stages" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "length": 0,
  "interestRate": 0.0,
  "inflationRate": 0.0,
  "index": 0
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoStageResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "name": "string",
    "length": 0,
    "interestRate": 0.0,
    "inflationRate": 0.0,
    "index": 0,
    "guid": "00000000-0000-0000-0000-000000000000"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Update { #operation-update }

```
PUT /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.stages.update()`](../../sdk/reference/stages.md#method-stages-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `stageGuid` | path | string (uuid) | yes |  |

**Request body** (`StageResponseDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `length` | integer (int32) | yes |  |
| `interestRate` | number, nullable | no |  |
| `inflationRate` | number, nullable | no |  |
| `index` | integer (int32) | yes |  |
| `guid` | string (uuid), nullable | no |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "length": 0,
  "interestRate": 0.0,
  "inflationRate": 0.0,
  "index": 0,
  "guid": "00000000-0000-0000-0000-000000000000"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStageResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "name": "string",
    "length": 0,
    "interestRate": 0.0,
    "inflationRate": 0.0,
    "index": 0,
    "guid": "00000000-0000-0000-0000-000000000000"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Delete { #operation-delete }

```
DELETE /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.stages.delete()`](../../sdk/reference/stages.md#method-stages-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `stageGuid` | path | string (uuid) | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | — |
