<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Intra-hub network links

## Get intra hub network link details { #operation-getIntraHubNetworkLinkDetails }

```
GET /sympheny-app/scenarios/intra-hub-network-links/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.intra_hub_network_links.get()`](../../sdk/reference/intra_hub_network_links.md#method-intra_hub_network_links-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/intra-hub-network-links/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoIntraHubNetworkLinkResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "intraHubNetworkLinkGuid": "string",
    "name": "string",
    "networkLoss": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "inputEnergyCarrier": {
      "energyCarrierGuid": "string",
      "typeKey": "string",
      "typeDisplayName": "string",
      "subtypeKey": "string",
      "subtypeDisplayName": "string",
      "energyCarrierName": "string",
      "colorHexCode": "string",
      "fixedInputShare": 0.0,
      "outputEfficiency": 0.0,
      "customOutputEfficiencyActivated": true,
      "customInputEfficiencyActivated": true,
      "customSeasonalityValues": [
        {
          "month": "JANUARY",
          "value": 0.0
        }
      ],
      "outputEfficiencyProfileId": 0,
      "created": "2026-01-01T00:00:00Z",
      "primary": true
    },
    "outputEnergyCarrier": {
      "energyCarrierGuid": "string",
      "typeKey": "string",
      "typeDisplayName": "string",
      "subtypeKey": "string",
      "subtypeDisplayName": "string",
      "energyCarrierName": "string",
      "colorHexCode": "string",
      "fixedInputShare": 0.0,
      "outputEfficiency": 0.0,
      "customOutputEfficiencyActivated": true,
      "customInputEfficiencyActivated": true,
      "customSeasonalityValues": [
        {
          "month": "JANUARY",
          "value": 0.0
        }
      ],
      "outputEfficiencyProfileId": 0,
      "created": "2026-01-01T00:00:00Z",
      "primary": true
    },
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "advancedCostComponents": [
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
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ]
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Delete intra hub network link { #operation-deleteIntraHubNetworkLink }

```
DELETE /sympheny-app/scenarios/intra-hub-network-links/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.intra_hub_network_links.delete()`](../../sdk/reference/intra_hub_network_links.md#method-intra_hub_network_links-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/intra-hub-network-links/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoIntraHubNetworkLinkListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "intraHubNetworkLinks": [
      {
        "intraHubNetworkLinkGuid": "string",
        "name": "string",
        "networkLoss": 0.0,
        "fixedEmbodiedCo2": 0.0,
        "inputEnergyCarrier": {
          "energyCarrierGuid": "string",
          "typeKey": "string",
          "typeDisplayName": "string",
          "subtypeKey": "string",
          "subtypeDisplayName": "string",
          "energyCarrierName": "string",
          "colorHexCode": "string",
          "fixedInputShare": 0.0,
          "outputEfficiency": 0.0,
          "customOutputEfficiencyActivated": true,
          "customInputEfficiencyActivated": true,
          "customSeasonalityValues": [
            {
              "month": null,
              "value": null
            }
          ],
          "outputEfficiencyProfileId": 0,
          "created": "2026-01-01T00:00:00Z",
          "primary": true
        },
        "outputEnergyCarrier": {
          "energyCarrierGuid": "string",
          "typeKey": "string",
          "typeDisplayName": "string",
          "subtypeKey": "string",
          "subtypeDisplayName": "string",
          "energyCarrierName": "string",
          "colorHexCode": "string",
          "fixedInputShare": 0.0,
          "outputEfficiency": 0.0,
          "customOutputEfficiencyActivated": true,
          "customInputEfficiencyActivated": true,
          "customSeasonalityValues": [
            {
              "month": null,
              "value": null
            }
          ],
          "outputEfficiencyProfileId": 0,
          "created": "2026-01-01T00:00:00Z",
          "primary": true
        },
        "hubs": [
          {
            "hubGuid": "string",
            "hubName": "string",
            "updated": "2026-01-01T00:00:00Z",
            "created": "2026-01-01T00:00:00Z"
          }
        ],
        "advancedCostComponents": [
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
        "stages": [
          "00000000-0000-0000-0000-000000000000"
        ]
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

## Get all intra hub network links { #operation-getAllIntraHubNetworkLinks }

```
GET /sympheny-app/scenarios/{scenarioGuid}/intra-hub-network-links
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.intra_hub_network_links.list()`](../../sdk/reference/intra_hub_network_links.md#method-intra_hub_network_links-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/{scenarioGuid}/intra-hub-network-links" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoIntraHubNetworkLinkListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "intraHubNetworkLinks": [
      {
        "intraHubNetworkLinkGuid": "string",
        "name": "string",
        "networkLoss": 0.0,
        "fixedEmbodiedCo2": 0.0,
        "inputEnergyCarrier": {
          "energyCarrierGuid": "string",
          "typeKey": "string",
          "typeDisplayName": "string",
          "subtypeKey": "string",
          "subtypeDisplayName": "string",
          "energyCarrierName": "string",
          "colorHexCode": "string",
          "fixedInputShare": 0.0,
          "outputEfficiency": 0.0,
          "customOutputEfficiencyActivated": true,
          "customInputEfficiencyActivated": true,
          "customSeasonalityValues": [
            {
              "month": null,
              "value": null
            }
          ],
          "outputEfficiencyProfileId": 0,
          "created": "2026-01-01T00:00:00Z",
          "primary": true
        },
        "outputEnergyCarrier": {
          "energyCarrierGuid": "string",
          "typeKey": "string",
          "typeDisplayName": "string",
          "subtypeKey": "string",
          "subtypeDisplayName": "string",
          "energyCarrierName": "string",
          "colorHexCode": "string",
          "fixedInputShare": 0.0,
          "outputEfficiency": 0.0,
          "customOutputEfficiencyActivated": true,
          "customInputEfficiencyActivated": true,
          "customSeasonalityValues": [
            {
              "month": null,
              "value": null
            }
          ],
          "outputEfficiencyProfileId": 0,
          "created": "2026-01-01T00:00:00Z",
          "primary": true
        },
        "hubs": [
          {
            "hubGuid": "string",
            "hubName": "string",
            "updated": "2026-01-01T00:00:00Z",
            "created": "2026-01-01T00:00:00Z"
          }
        ],
        "advancedCostComponents": [
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
        "stages": [
          "00000000-0000-0000-0000-000000000000"
        ]
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

## Update intra hub network link v2 { #operation-updateIntraHubNetworkLinkV2 }

```
PUT /sympheny-app/v2/scenarios/intra-hub-network-links/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.intra_hub_network_links.update()`](../../sdk/reference/intra_hub_network_links.md#method-intra_hub_network_links-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`IntraHubNetworkLinkRequestDtoPUT`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `networkLoss` | number, nullable | no |  |
| `fixedEmbodiedCo2` | number, nullable | no |  |
| `inputEnergyCarrier` | `EnergyCarrierRequestDtoPUTId` | yes |  |
| `outputEnergyCarrier` | `EnergyCarrierRequestDtoPUTId` | yes |  |
| `hubs` | array of `HubRequestDtoPUTId` | yes |  |
| `advancedCostComponents` | array of `AdvancedCostComponentResponseDto`, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/intra-hub-network-links/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "networkLoss": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "inputEnergyCarrier": {
    "energyCarrierGuid": "string"
  },
  "outputEnergyCarrier": {
    "energyCarrierGuid": "string"
  },
  "hubs": [
    {
      "hubGuid": "string"
    }
  ],
  "advancedCostComponents": [
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
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoIntraHubNetworkLinkResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "intraHubNetworkLinkGuid": "string",
    "name": "string",
    "networkLoss": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "inputEnergyCarrier": {
      "energyCarrierGuid": "string",
      "typeKey": "string",
      "typeDisplayName": "string",
      "subtypeKey": "string",
      "subtypeDisplayName": "string",
      "energyCarrierName": "string",
      "colorHexCode": "string",
      "fixedInputShare": 0.0,
      "outputEfficiency": 0.0,
      "customOutputEfficiencyActivated": true,
      "customInputEfficiencyActivated": true,
      "customSeasonalityValues": [
        {
          "month": "JANUARY",
          "value": 0.0
        }
      ],
      "outputEfficiencyProfileId": 0,
      "created": "2026-01-01T00:00:00Z",
      "primary": true
    },
    "outputEnergyCarrier": {
      "energyCarrierGuid": "string",
      "typeKey": "string",
      "typeDisplayName": "string",
      "subtypeKey": "string",
      "subtypeDisplayName": "string",
      "energyCarrierName": "string",
      "colorHexCode": "string",
      "fixedInputShare": 0.0,
      "outputEfficiency": 0.0,
      "customOutputEfficiencyActivated": true,
      "customInputEfficiencyActivated": true,
      "customSeasonalityValues": [
        {
          "month": "JANUARY",
          "value": 0.0
        }
      ],
      "outputEfficiencyProfileId": 0,
      "created": "2026-01-01T00:00:00Z",
      "primary": true
    },
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "advancedCostComponents": [
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
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ]
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Specify intra hub network link v2 { #operation-specifyIntraHubNetworkLinkV2 }

```
POST /sympheny-app/v2/scenarios/{scenarioGuid}/intra-hub-network-links
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.intra_hub_network_links.create()`](../../sdk/reference/intra_hub_network_links.md#method-intra_hub_network_links-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`IntraHubNetworkLinkRequestDto`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | yes |  |
| `networkLoss` | number, nullable | no |  |
| `fixedEmbodiedCo2` | number, nullable | no |  |
| `inputEnergyCarrierGuid` | string | yes |  |
| `outputEnergyCarrierGuid` | string | yes |  |
| `hubGuids` | array of string | yes |  |
| `advancedCostComponents` | array of `AdvancedCostComponentRequestDto`, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/intra-hub-network-links" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "networkLoss": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "inputEnergyCarrierGuid": "string",
  "outputEnergyCarrierGuid": "string",
  "hubGuids": [
    "string"
  ],
  "advancedCostComponents": [
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
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoIntraHubNetworkLinkResponseDto` |

**Example response** (201)

```json
{
  "data": {
    "intraHubNetworkLinkGuid": "string",
    "name": "string",
    "networkLoss": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "inputEnergyCarrier": {
      "energyCarrierGuid": "string",
      "typeKey": "string",
      "typeDisplayName": "string",
      "subtypeKey": "string",
      "subtypeDisplayName": "string",
      "energyCarrierName": "string",
      "colorHexCode": "string",
      "fixedInputShare": 0.0,
      "outputEfficiency": 0.0,
      "customOutputEfficiencyActivated": true,
      "customInputEfficiencyActivated": true,
      "customSeasonalityValues": [
        {
          "month": "JANUARY",
          "value": 0.0
        }
      ],
      "outputEfficiencyProfileId": 0,
      "created": "2026-01-01T00:00:00Z",
      "primary": true
    },
    "outputEnergyCarrier": {
      "energyCarrierGuid": "string",
      "typeKey": "string",
      "typeDisplayName": "string",
      "subtypeKey": "string",
      "subtypeDisplayName": "string",
      "energyCarrierName": "string",
      "colorHexCode": "string",
      "fixedInputShare": 0.0,
      "outputEfficiency": 0.0,
      "customOutputEfficiencyActivated": true,
      "customInputEfficiencyActivated": true,
      "customSeasonalityValues": [
        {
          "month": "JANUARY",
          "value": 0.0
        }
      ],
      "outputEfficiencyProfileId": 0,
      "created": "2026-01-01T00:00:00Z",
      "primary": true
    },
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "advancedCostComponents": [
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
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ]
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
