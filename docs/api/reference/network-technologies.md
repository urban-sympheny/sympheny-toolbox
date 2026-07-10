<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Network technologies

## Delete network technology { #operation-deleteNetworkTechnology }

```
DELETE /sympheny-app/scenarios/network-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_technologies.delete()`](../../sdk/reference/network_technologies.md#method-network_technologies-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/network-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoNetworkTechnologyListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "networkTechnologies": [
      {
        "networkTechnologyGuid": "string",
        "networkTechnologyName": "string",
        "networkLoss": 0.0,
        "fixedInvestmentCost": 0.0,
        "variableInvestmentCost": 0.0,
        "variableOmCostYear": 0.0,
        "fixedOmCostChf": 0.0,
        "fixedOmCostPercent": 0.0,
        "lifetime": 0.0,
        "maximumCapacity": 0.0,
        "minimumCapacity": 0.0,
        "variableEmbodiedCo2": 0.0,
        "fixedEmbodiedCo2": 0.0,
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z",
        "energyCarrier": {
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
        "category": "string",
        "technologyCategory": "string",
        "notes": "string",
        "source": "string",
        "networkSize": "string",
        "comesFromDb": "string",
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

## Get network tech details v2 { #operation-getNetworkTechDetailsV2 }

```
GET /sympheny-app/v2/scenarios/network-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_technologies.get()`](../../sdk/reference/network_technologies.md#method-network_technologies-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/network-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoNetworkTechnologyResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "fixedInvestmentCost": 0.0,
    "variableInvestmentCost": 0.0,
    "fixedOmCostChf": 0.0,
    "variableOmCostPercent": 0.0,
    "variableOmCostYear": 0.0,
    "variableOmCostCHFkWh": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "variableEmbodiedCo2": 0.0,
    "fixedReplacementCost": 0.0,
    "variableReplacementCostPercent": 0.0,
    "variableReplacementCostCHF": 0.0,
    "fixedSalvageValue": 0.0,
    "variableSalvageValuePercent": 0.0,
    "variableSalvageValueCHF": 0.0,
    "networkTechnologyGuid": "string",
    "networkTechnologyName": "string",
    "exchangeCurrency": "string",
    "exchangeRate": 0.0,
    "lifetime": 0,
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "energyCarrier": {
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
    "category": "string",
    "technologyCategory": "string",
    "notes": "string",
    "source": "string",
    "networkSize": "string",
    "comesFromDb": "string",
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

## Get all network technologies by scenario v2 { #operation-getAllNetworkTechnologiesByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/network-technologies
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_technologies.list()`](../../sdk/reference/network_technologies.md#method-network_technologies-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/network-technologies" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoNetworkTechnologyListResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "networkTechnologies": [
      {
        "fixedInvestmentCost": 0.0,
        "variableInvestmentCost": 0.0,
        "fixedOmCostChf": 0.0,
        "variableOmCostPercent": 0.0,
        "variableOmCostYear": 0.0,
        "variableOmCostCHFkWh": 0.0,
        "fixedEmbodiedCo2": 0.0,
        "variableEmbodiedCo2": 0.0,
        "fixedReplacementCost": 0.0,
        "variableReplacementCostPercent": 0.0,
        "variableReplacementCostCHF": 0.0,
        "fixedSalvageValue": 0.0,
        "variableSalvageValuePercent": 0.0,
        "variableSalvageValueCHF": 0.0,
        "networkTechnologyGuid": "string",
        "networkTechnologyName": "string",
        "exchangeCurrency": "string",
        "exchangeRate": 0.0,
        "lifetime": 0,
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z",
        "energyCarrier": {
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
        "category": "string",
        "technologyCategory": "string",
        "notes": "string",
        "source": "string",
        "networkSize": "string",
        "comesFromDb": "string",
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

## Update network technology v2 1 { #operation-updateNetworkTechnologyV2_1 }

```
PUT /sympheny-app/v2_1/scenarios/network-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_technologies.update()`](../../sdk/reference/network_technologies.md#method-network_technologies-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`NetworkTechnologyResponseDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixedInvestmentCost` | number, nullable | no |  |
| `variableInvestmentCost` | number, nullable | no |  |
| `fixedOmCostChf` | number, nullable | no |  |
| `variableOmCostPercent` | number, nullable | no |  |
| `variableOmCostYear` | number, nullable | no |  |
| `variableOmCostCHFkWh` | number, nullable | no |  |
| `fixedEmbodiedCo2` | number, nullable | no |  |
| `variableEmbodiedCo2` | number, nullable | no |  |
| `fixedReplacementCost` | number, nullable | no |  |
| `variableReplacementCostPercent` | number | yes |  |
| `variableReplacementCostCHF` | number, nullable | no |  |
| `fixedSalvageValue` | number, nullable | no |  |
| `variableSalvageValuePercent` | number | yes |  |
| `variableSalvageValueCHF` | number, nullable | no |  |
| `networkTechnologyGuid` | string, nullable | no |  |
| `networkTechnologyName` | string | yes |  |
| `exchangeCurrency` | string | yes |  |
| `exchangeRate` | number | yes |  |
| `lifetime` | integer (int32) | yes |  |
| `created` | string (date-time), nullable | no |  |
| `updated` | string (date-time), nullable | no |  |
| `energyCarrier` | `EnergyCarrierResponseDto` | yes |  |
| `category` | string | yes |  |
| `technologyCategory` | string, nullable | no |  |
| `notes` | string, nullable | no |  |
| `source` | string, nullable | no |  |
| `networkSize` | string, nullable | no |  |
| `comesFromDb` | string, nullable | no |  |
| `costComponents` | array of `AdvancedCostComponentResponseDto` | yes |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/network-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "fixedInvestmentCost": 0.0,
  "variableInvestmentCost": 0.0,
  "fixedOmCostChf": 0.0,
  "variableOmCostPercent": 0.0,
  "variableOmCostYear": 0.0,
  "variableOmCostCHFkWh": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "variableEmbodiedCo2": 0.0,
  "fixedReplacementCost": 0.0,
  "variableReplacementCostPercent": 0.0,
  "variableReplacementCostCHF": 0.0,
  "fixedSalvageValue": 0.0,
  "variableSalvageValuePercent": 0.0,
  "variableSalvageValueCHF": 0.0,
  "networkTechnologyGuid": "string",
  "networkTechnologyName": "string",
  "exchangeCurrency": "string",
  "exchangeRate": 0.0,
  "lifetime": 0,
  "created": "2026-01-01T00:00:00Z",
  "updated": "2026-01-01T00:00:00Z",
  "energyCarrier": {
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
  "category": "string",
  "technologyCategory": "string",
  "notes": "string",
  "source": "string",
  "networkSize": "string",
  "comesFromDb": "string",
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
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoNetworkTechnologyResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "fixedInvestmentCost": 0.0,
    "variableInvestmentCost": 0.0,
    "fixedOmCostChf": 0.0,
    "variableOmCostPercent": 0.0,
    "variableOmCostYear": 0.0,
    "variableOmCostCHFkWh": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "variableEmbodiedCo2": 0.0,
    "fixedReplacementCost": 0.0,
    "variableReplacementCostPercent": 0.0,
    "variableReplacementCostCHF": 0.0,
    "fixedSalvageValue": 0.0,
    "variableSalvageValuePercent": 0.0,
    "variableSalvageValueCHF": 0.0,
    "networkTechnologyGuid": "string",
    "networkTechnologyName": "string",
    "exchangeCurrency": "string",
    "exchangeRate": 0.0,
    "lifetime": 0,
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "energyCarrier": {
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
    "category": "string",
    "technologyCategory": "string",
    "notes": "string",
    "source": "string",
    "networkSize": "string",
    "comesFromDb": "string",
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

## Specify network technology v2 1 { #operation-specifyNetworkTechnologyV2_1 }

```
POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/network-technologies
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.network_technologies.create()`](../../sdk/reference/network_technologies.md#method-network_technologies-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`NetworkTechnologyRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixedInvestmentCost` | number, nullable | no |  |
| `variableInvestmentCost` | number, nullable | no |  |
| `fixedOmCostChf` | number, nullable | no |  |
| `variableOmCostPercent` | number, nullable | no |  |
| `variableOmCostYear` | number, nullable | no |  |
| `variableOmCostCHFkWh` | number, nullable | no |  |
| `fixedEmbodiedCo2` | number, nullable | no |  |
| `variableEmbodiedCo2` | number, nullable | no |  |
| `fixedReplacementCost` | number, nullable | no |  |
| `variableReplacementCostPercent` | number, nullable | no |  |
| `variableReplacementCostCHF` | number, nullable | no |  |
| `fixedSalvageValue` | number, nullable | no |  |
| `variableSalvageValuePercent` | number, nullable | no |  |
| `variableSalvageValueCHF` | number, nullable | no |  |
| `networkTechnologyName` | string | yes |  |
| `lifetime` | integer (int32) | yes |  |
| `energyCarrierGuid` | string | yes |  |
| `costComponents` | array of `AdvancedCostComponentRequestDto`, nullable | no |  |
| `suggested` | boolean, nullable | no |  |
| `technologyCategory` | string, nullable | no |  |
| `networkSize` | string, nullable | no |  |
| `notes` | string, nullable | no |  |
| `source` | string, nullable | no |  |
| `comesFromDb` | string, nullable | no |  |
| `exchangeCurrency` | string, nullable | no |  |
| `exchangeRate` | number, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/{scenarioGuid}/network-technologies" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "fixedInvestmentCost": 0.0,
  "variableInvestmentCost": 0.0,
  "fixedOmCostChf": 0.0,
  "variableOmCostPercent": 0.0,
  "variableOmCostYear": 0.0,
  "variableOmCostCHFkWh": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "variableEmbodiedCo2": 0.0,
  "fixedReplacementCost": 0.0,
  "variableReplacementCostPercent": 0.0,
  "variableReplacementCostCHF": 0.0,
  "fixedSalvageValue": 0.0,
  "variableSalvageValuePercent": 0.0,
  "variableSalvageValueCHF": 0.0,
  "networkTechnologyName": "string",
  "lifetime": 0,
  "energyCarrierGuid": "string",
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
  "suggested": true,
  "technologyCategory": "string",
  "networkSize": "string",
  "notes": "string",
  "source": "string",
  "comesFromDb": "string",
  "exchangeCurrency": "string",
  "exchangeRate": 0.0,
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoNetworkTechnologyResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "fixedInvestmentCost": 0.0,
    "variableInvestmentCost": 0.0,
    "fixedOmCostChf": 0.0,
    "variableOmCostPercent": 0.0,
    "variableOmCostYear": 0.0,
    "variableOmCostCHFkWh": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "variableEmbodiedCo2": 0.0,
    "fixedReplacementCost": 0.0,
    "variableReplacementCostPercent": 0.0,
    "variableReplacementCostCHF": 0.0,
    "fixedSalvageValue": 0.0,
    "variableSalvageValuePercent": 0.0,
    "variableSalvageValueCHF": 0.0,
    "networkTechnologyGuid": "string",
    "networkTechnologyName": "string",
    "exchangeCurrency": "string",
    "exchangeRate": 0.0,
    "lifetime": 0,
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "energyCarrier": {
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
    "category": "string",
    "technologyCategory": "string",
    "notes": "string",
    "source": "string",
    "networkSize": "string",
    "comesFromDb": "string",
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
