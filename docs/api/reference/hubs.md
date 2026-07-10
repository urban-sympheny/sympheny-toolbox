<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Hubs

## Get hub { #operation-getHub }

```
GET /sympheny-app/scenarios/hubs/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.hubs.get()`](../../sdk/reference/hubs.md#method-hubs-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/hubs/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoHubResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "hubGuid": "string",
    "hubName": "string",
    "updated": "2026-01-01T00:00:00Z",
    "created": "2026-01-01T00:00:00Z"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Delete hub { #operation-deleteHub }

```
DELETE /sympheny-app/scenarios/hubs/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.hubs.delete()`](../../sdk/reference/hubs.md#method-hubs-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/hubs/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListHubResponseDto` |

**Example response** (200)

```json
{
  "data": [
    {
      "hubGuid": "string",
      "hubName": "string",
      "updated": "2026-01-01T00:00:00Z",
      "created": "2026-01-01T00:00:00Z"
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Find all hubs by scenario { #operation-findAllHubsByScenario }

```
GET /sympheny-app/scenarios/{scenarioGuid}/hubs
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.hubs.list()`](../../sdk/reference/hubs.md#method-hubs-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/hubs" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListFHubResponseDto` |

**Example response** (200)

```json
{
  "data": [
    {
      "hubGuid": "string",
      "hubName": "string",
      "updated": "2026-01-01T00:00:00Z",
      "created": "2026-01-01T00:00:00Z"
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Create new hub { #operation-createNewHub }

```
POST /sympheny-app/scenarios/{scenarioGuid}/hubs
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.hubs.create()`](../../sdk/reference/hubs.md#method-hubs-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`HubRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hubName` | string | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/hubs" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "hubName": "string"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoHubResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "hubGuid": "string",
    "hubName": "string",
    "updated": "2026-01-01T00:00:00Z",
    "created": "2026-01-01T00:00:00Z"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Edit hub { #operation-editHub }

```
PUT /sympheny-app/v2/scenarios/hubs/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.hubs.update()`](../../sdk/reference/hubs.md#method-hubs-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`HubResponseDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hubGuid` | string | yes |  |
| `hubName` | string | yes |  |
| `updated` | string (date-time) | yes |  |
| `created` | string (date-time) | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/hubs/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "hubGuid": "string",
  "hubName": "string",
  "updated": "2026-01-01T00:00:00Z",
  "created": "2026-01-01T00:00:00Z"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoHubResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "hubGuid": "string",
    "hubName": "string",
    "updated": "2026-01-01T00:00:00Z",
    "created": "2026-01-01T00:00:00Z"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
