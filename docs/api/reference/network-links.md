<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Network links

## Delete network link { #operation-deleteNetworkLink }

```
DELETE /sympheny-app/scenarios/{scenarioGuid}/network-links/{network-link-guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_links.delete()`](../../sdk/reference/network_links.md#method-network_links-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `network-link-guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/network-links/{network-link-guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoNetworkLinkListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "networkLinks": [
      {
        "networkLinkGuid": "string",
        "length": 0.0,
        "technologyCapacity": "optimize",
        "installedCapacity": 0.0,
        "uniDirectionalFlow": true,
        "mustBeInstalled": true,
        "node1Guid": "string",
        "node1Name": "string",
        "node2Guid": "string",
        "node2Name": "string",
        "networkTechnologyName": "string",
        "networkTechnologyGuid": "string",
        "costComponents": [
          {
            "name": "string",
            "value": 0.0,
            "category": "string",
            "lifetime": 0.0,
            "interestRate": 0.0,
            "length": 0.0,
            "complexityFactor": 0.0,
            "dataPoints": 0.0,
            "numberOfPumps": 0.0,
            "guid": "string",
            "categoryId": "string"
          }
        ],
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z"
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

## Get network link details v2 { #operation-getNetworkLinkDetailsV2 }

```
GET /sympheny-app/v2/network-links/{network-link-guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_links.get()`](../../sdk/reference/network_links.md#method-network_links-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `network-link-guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/network-links/{network-link-guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoNetworkLinkResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "installedCapacity": 0.0,
    "maximumCapacity": 0.0,
    "networkLinkGuid": "string",
    "name": "string",
    "length": 0.0,
    "technologyCapacity": "optimize",
    "uniDirectionalFlow": true,
    "mustBeInstalled": true,
    "node1Guid": "string",
    "node1Name": "string",
    "node2Guid": "string",
    "node2Name": "string",
    "networkTechnologyName": "string",
    "networkTechnologyGuid": "string",
    "costComponents": [
      {
        "name": "string",
        "value": 0.0,
        "category": "string",
        "lifetime": 0.0,
        "interestRate": 0.0,
        "length": 0.0,
        "complexityFactor": 0.0,
        "dataPoints": 0.0,
        "numberOfPumps": 0.0,
        "guid": "string",
        "categoryId": "string"
      }
    ],
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "minimumCapacity": 0.0,
    "networkLoss": 0.0,
    "networkLossProfileId": 0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Get all network links by scenario v2 { #operation-getAllNetworkLinksByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/network-links
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_links.list()`](../../sdk/reference/network_links.md#method-network_links-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/network-links" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListNetworkLinkResponseDtoV2` |

**Example response** (200)

```json
{
  "data": [
    {
      "installedCapacity": 0.0,
      "maximumCapacity": 0.0,
      "networkLinkGuid": "string",
      "name": "string",
      "length": 0.0,
      "technologyCapacity": "optimize",
      "uniDirectionalFlow": true,
      "mustBeInstalled": true,
      "node1Guid": "string",
      "node1Name": "string",
      "node2Guid": "string",
      "node2Name": "string",
      "networkTechnologyName": "string",
      "networkTechnologyGuid": "string",
      "costComponents": [
        {
          "name": "string",
          "value": 0.0,
          "category": "string",
          "lifetime": 0.0,
          "interestRate": 0.0,
          "length": 0.0,
          "complexityFactor": 0.0,
          "dataPoints": 0.0,
          "numberOfPumps": 0.0,
          "guid": "string",
          "categoryId": "string"
        }
      ],
      "created": "2026-01-01T00:00:00Z",
      "updated": "2026-01-01T00:00:00Z",
      "minimumCapacity": 0.0,
      "networkLoss": 0.0,
      "networkLossProfileId": 0
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Specify network link v2 1 { #operation-specifyNetworkLinkV2_1 }

```
POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/network-links
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_links.create()`](../../sdk/reference/network_links.md#method-network_links-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`NetworkLinkRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `installedCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `maximumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `name` | string | yes |  |
| `length` | number | yes | Invalid NUMERIC. Max precision=16, max scale=5. |
| `technologyCapacity` | string | yes | One of: `optimize`, `specify`. |
| `uniDirectionalFlow` | boolean, nullable | no |  |
| `mustBeInstalled` | boolean, nullable | no |  |
| `node1Guid` | string | yes |  |
| `node2Guid` | string | yes |  |
| `networkTechnologyGuid` | string | yes |  |
| `costComponents` | array of `AdvancedCostComponentRequestDto`, nullable | no |  |
| `minimumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `networkLoss` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `networkLossProfileId` | integer (int64), nullable | no |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/{scenarioGuid}/network-links" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "installedCapacity": 0.0,
  "maximumCapacity": 0.0,
  "name": "string",
  "length": 0.0,
  "technologyCapacity": "optimize",
  "uniDirectionalFlow": true,
  "mustBeInstalled": true,
  "node1Guid": "string",
  "node2Guid": "string",
  "networkTechnologyGuid": "string",
  "costComponents": [
    {
      "name": "string",
      "value": 0.0,
      "category": "string",
      "lifetime": 0.0,
      "interestRate": 0.0,
      "length": 0.0,
      "complexityFactor": 0.0,
      "dataPoints": 0.0,
      "numberOfPumps": 0.0
    }
  ],
  "minimumCapacity": 0.0,
  "networkLoss": 0.0,
  "networkLossProfileId": 0
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoNetworkLinkResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "installedCapacity": 0.0,
    "maximumCapacity": 0.0,
    "networkLinkGuid": "string",
    "name": "string",
    "length": 0.0,
    "technologyCapacity": "optimize",
    "uniDirectionalFlow": true,
    "mustBeInstalled": true,
    "node1Guid": "string",
    "node1Name": "string",
    "node2Guid": "string",
    "node2Name": "string",
    "networkTechnologyName": "string",
    "networkTechnologyGuid": "string",
    "costComponents": [
      {
        "name": "string",
        "value": 0.0,
        "category": "string",
        "lifetime": 0.0,
        "interestRate": 0.0,
        "length": 0.0,
        "complexityFactor": 0.0,
        "dataPoints": 0.0,
        "numberOfPumps": 0.0,
        "guid": "string",
        "categoryId": "string"
      }
    ],
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "minimumCapacity": 0.0,
    "networkLoss": 0.0,
    "networkLossProfileId": 0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Update network link v2 2 { #operation-updateNetworkLinkV2_2 }

```
PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/network-links/{network-link-guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_links.update()`](../../sdk/reference/network_links.md#method-network_links-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `network-link-guid` | path | string | yes |  |

**Request body** (`NetworkLinkRequestDtoPUT`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `installedCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `maximumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `name` | string | yes |  |
| `length` | number | yes | Invalid NUMERIC. Max precision=16, max scale=5. |
| `technologyCapacity` | string | yes | One of: `optimize`, `specify`. |
| `uniDirectionalFlow` | boolean, nullable | no |  |
| `mustBeInstalled` | boolean, nullable | no |  |
| `node1Guid` | string | yes |  |
| `node1Name` | string | yes |  |
| `node2Guid` | string | yes |  |
| `node2Name` | string | yes |  |
| `networkTechnologyName` | string | yes |  |
| `networkTechnologyGuid` | string | yes |  |
| `costComponents` | array of `AdvancedCostComponentResponseDto`, nullable | no |  |
| `minimumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `networkLoss` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `networkLossProfileId` | integer (int64), nullable | no |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_2/scenarios/{scenarioGuid}/network-links/{network-link-guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "installedCapacity": 0.0,
  "maximumCapacity": 0.0,
  "name": "string",
  "length": 0.0,
  "technologyCapacity": "optimize",
  "uniDirectionalFlow": true,
  "mustBeInstalled": true,
  "node1Guid": "string",
  "node1Name": "string",
  "node2Guid": "string",
  "node2Name": "string",
  "networkTechnologyName": "string",
  "networkTechnologyGuid": "string",
  "costComponents": [
    {
      "name": "string",
      "value": 0.0,
      "category": "string",
      "lifetime": 0.0,
      "interestRate": 0.0,
      "length": 0.0,
      "complexityFactor": 0.0,
      "dataPoints": 0.0,
      "numberOfPumps": 0.0,
      "guid": "string",
      "categoryId": "string"
    }
  ],
  "minimumCapacity": 0.0,
  "networkLoss": 0.0,
  "networkLossProfileId": 0
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoNetworkLinkResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "installedCapacity": 0.0,
    "maximumCapacity": 0.0,
    "networkLinkGuid": "string",
    "name": "string",
    "length": 0.0,
    "technologyCapacity": "optimize",
    "uniDirectionalFlow": true,
    "mustBeInstalled": true,
    "node1Guid": "string",
    "node1Name": "string",
    "node2Guid": "string",
    "node2Name": "string",
    "networkTechnologyName": "string",
    "networkTechnologyGuid": "string",
    "costComponents": [
      {
        "name": "string",
        "value": 0.0,
        "category": "string",
        "lifetime": 0.0,
        "interestRate": 0.0,
        "length": 0.0,
        "complexityFactor": 0.0,
        "dataPoints": 0.0,
        "numberOfPumps": 0.0,
        "guid": "string",
        "categoryId": "string"
      }
    ],
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "minimumCapacity": 0.0,
    "networkLoss": 0.0,
    "networkLossProfileId": 0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
