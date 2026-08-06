<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Profiles

## List 1 { #operation-list_1 }

```
GET /sympheny-app/scenarios/{scenarioGuid}/profiles
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.profiles.list()`](../../sdk/reference/profiles.md#method-profiles-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/profiles" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListProfileResponseDto` |

**Example response** (200)

```json
{
  "data": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Create json { #operation-createJson }

```
POST /sympheny-app/scenarios/{scenarioGuid}/profiles-json
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.profiles.create()`](../../sdk/reference/profiles.md#method-profiles-create).

values array size must be exactly 8760, with period from 1 to 8760, and positive demandValue

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`ProfileJsonRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `values` | array of `ProfilePeriodValueDto` | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/profiles-json" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "values": [
    {
      "period": 0,
      "demandValue": 0.0
    }
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoProfileResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "id": 0,
    "name": "string"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Get { #operation-get }

```
GET /sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.profiles.get()`](../../sdk/reference/profiles.md#method-profiles-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `profileId` | path | integer (int64) | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoProfileDetailsResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "id": 0,
    "name": "string",
    "values": [
      {
        "period": 0,
        "demandValue": 0.0
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

## Delete 1 { #operation-delete_1 }

```
DELETE /sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.profiles.delete()`](../../sdk/reference/profiles.md#method-profiles-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `profileId` | path | integer (int64) | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/profiles/{profileId}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | n/a |

## Edit json v2 { #operation-editJsonV2 }

```
PUT /sympheny-app/v2/scenarios/{scenarioGuid}/profiles-json/{profileId}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.profiles.update()`](../../sdk/reference/profiles.md#method-profiles-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `profileId` | path | integer (int64) | yes |  |

**Request body** (`ProfileRequestDtoPUT`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `values` | array of `ProfilePeriodValueDto` | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/profiles-json/{profileId}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "values": [
    {
      "period": 0,
      "demandValue": 0.0
    }
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoProfileDetailsResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "id": 0,
    "name": "string",
    "values": [
      {
        "period": 0,
        "demandValue": 0.0
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
