<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Conversion technologies

## Get conversion tech details v2 { #operation-getConversionTechDetailsV2 }

```
GET /sympheny-app/v2/scenarios/conversion-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.conversion_technologies.get()`](../../sdk/reference/conversion_technologies.md#method-conversion_technologies-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/conversion-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoConversionTechnologyDetailResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "fixedInvestmentCost": 0.0,
    "fixedOmCostChf": 0.0,
    "variableOmCostPercent": 0.0,
    "variableOmCostYear": 0.0,
    "variableOmCost": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "variableEmbodiedCo2": 0.0,
    "variableEmittedCo2": 0.0,
    "variableCapturedCo2": 0.0,
    "fixedReplacementCost": 0.0,
    "variableReplacementCostPercent": 0.0,
    "variableReplacementCostCHF": 0.0,
    "fixedSalvageValue": 0.0,
    "variableSalvageValuePercent": 0.0,
    "variableSalvageValueCHF": 0.0,
    "mustBeInstalledInHubs": "canBeInstalled",
    "conversionTechnologyGuid": "string",
    "processName": "string",
    "exchangeCurrency": "string",
    "exchangeRate": 0.0,
    "variableInvestmentCost": 0.0,
    "lifetime": 0.0,
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "technologyModes": [
      {
        "capacity": 0.0,
        "minimumAnnualOutput": 0.0,
        "maximumAnnualOutput": 0.0,
        "curtailmentLimitation": 0.0,
        "peakPower": 0.0,
        "minPartLoad": 0.0,
        "minimumUpTime": 0,
        "minimumDownTime": 0,
        "technologyModeGuid": "string",
        "inputEnergyCarriers": [
          {
            "energyCarrierGuid": "string",
            "typeKey": "string",
            "typeDisplayName": "string",
            "subtypeKey": "string",
            "subtypeDisplayName": "string",
            "energyCarrierName": "string",
            "colorHexCode": "string",
            "outputEfficiency": 0.0,
            "fixedInputShare": 0.0,
            "customOutputEfficiencyActivated": true,
            "customInputShareActivated": true,
            "customSeasonalityValues": [
              {
                "month": null,
                "value": null
              }
            ],
            "inputShareProfileId": 0,
            "outputEfficiencyProfileId": 0,
            "created": "2026-01-01T00:00:00Z",
            "primary": true
          }
        ],
        "outputEnergyCarriers": [
          {
            "energyCarrierGuid": "string",
            "typeKey": "string",
            "typeDisplayName": "string",
            "subtypeKey": "string",
            "subtypeDisplayName": "string",
            "energyCarrierName": "string",
            "colorHexCode": "string",
            "outputEfficiency": 0.0,
            "fixedInputShare": 0.0,
            "customOutputEfficiencyActivated": true,
            "customInputShareActivated": true,
            "customSeasonalityValues": [
              {
                "month": null,
                "value": null
              }
            ],
            "inputShareProfileId": 0,
            "outputEfficiencyProfileId": 0,
            "created": "2026-01-01T00:00:00Z",
            "primary": true
          }
        ],
        "seasonalOperationName": "string",
        "seasonalOperationValue": "string",
        "allowedOperationProfileId": 0,
        "primary": true,
        "maximumCapacity": 0.0,
        "minimumCapacity": 0.0,
        "simultaneousOperation": true
      }
    ],
    "category": "string",
    "technologyCategory": "string",
    "mutuallyExclusiveGroup": "string",
    "notes": "string",
    "virtual": true,
    "technologyOptional": true,
    "partOfTechnologyPackage": true,
    "technologyCapacity": "string",
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
    "comesFromDb": "string",
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

## Delete conversion technology v2 { #operation-deleteConversionTechnologyV2 }

```
DELETE /sympheny-app/v2/scenarios/conversion-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.conversion_technologies.delete()`](../../sdk/reference/conversion_technologies.md#method-conversion_technologies-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/conversion-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | — |

## Get all conversion technologies by scenario v2 { #operation-getAllConversionTechnologiesByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/conversion-technologies
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.conversion_technologies.list()`](../../sdk/reference/conversion_technologies.md#method-conversion_technologies-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/conversion-technologies" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoConversionTechnologyListResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "conversionTechnologies": [
      {
        "conversionTechnologyGuid": "string",
        "processName": "string",
        "lifetime": 0,
        "created": "2026-01-01T00:00:00Z",
        "updated": "2026-01-01T00:00:00Z",
        "conversionTechnologyModes": [
          {
            "capacity": 0.0,
            "minimumAnnualOutput": 0.0,
            "maximumAnnualOutput": 0.0,
            "curtailmentLimitation": 0.0,
            "peakPower": 0.0,
            "minPartLoad": 0.0,
            "minimumUpTime": 0,
            "minimumDownTime": 0,
            "technologyModeGuid": "string",
            "inputEnergyCarriers": [
              {
                "energyCarrierGuid": null,
                "typeKey": null,
                "typeDisplayName": null,
                "subtypeKey": null,
                "subtypeDisplayName": null,
                "energyCarrierName": null,
                "colorHexCode": null,
                "outputEfficiency": null,
                "fixedInputShare": null,
                "customOutputEfficiencyActivated": null,
                "customInputShareActivated": null,
                "customSeasonalityValues": null,
                "inputShareProfileId": null,
                "outputEfficiencyProfileId": null,
                "created": null,
                "primary": null
              }
            ],
            "outputEnergyCarriers": [
              {
                "energyCarrierGuid": null,
                "typeKey": null,
                "typeDisplayName": null,
                "subtypeKey": null,
                "subtypeDisplayName": null,
                "energyCarrierName": null,
                "colorHexCode": null,
                "outputEfficiency": null,
                "fixedInputShare": null,
                "customOutputEfficiencyActivated": null,
                "customInputShareActivated": null,
                "customSeasonalityValues": null,
                "inputShareProfileId": null,
                "outputEfficiencyProfileId": null,
                "created": null,
                "primary": null
              }
            ],
            "seasonalOperationName": "string",
            "seasonalOperationValue": "string",
            "allowedOperationProfileId": 0,
            "primary": true,
            "maximumCapacity": 0.0,
            "minimumCapacity": 0.0,
            "simultaneousOperation": true
          }
        ],
        "hubs": [
          {
            "hubGuid": "string",
            "hubName": "string",
            "updated": "2026-01-01T00:00:00Z",
            "created": "2026-01-01T00:00:00Z"
          }
        ],
        "virtual": true,
        "mustBeInstalledInHubs": "canBeInstalled",
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

## Update conversion technology { #operation-updateConversionTechnology }

```
PUT /sympheny-app/v2_1/scenarios/conversion-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.conversion_technologies.update()`](../../sdk/reference/conversion_technologies.md#method-conversion_technologies-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`ConversionTechnologyDetailResponseDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixedInvestmentCost` | number, nullable | no |  |
| `fixedOmCostChf` | number, nullable | no |  |
| `variableOmCostPercent` | number, nullable | no |  |
| `variableOmCostYear` | number, nullable | no |  |
| `variableOmCost` | number, nullable | no |  |
| `fixedEmbodiedCo2` | number, nullable | no |  |
| `variableEmbodiedCo2` | number, nullable | no |  |
| `variableEmittedCo2` | number, nullable | no |  |
| `variableCapturedCo2` | number, nullable | no |  |
| `fixedReplacementCost` | number, nullable | no |  |
| `variableReplacementCostPercent` | number, nullable | no |  |
| `variableReplacementCostCHF` | number, nullable | no |  |
| `fixedSalvageValue` | number, nullable | no |  |
| `variableSalvageValuePercent` | number, nullable | no |  |
| `variableSalvageValueCHF` | number, nullable | no |  |
| `mustBeInstalledInHubs` | string | yes | One of: `canBeInstalled`, `mustBeInstalled`, `mustBeInstalledInAtLeastOneHub`. |
| `conversionTechnologyGuid` | string, nullable | no |  |
| `processName` | string | yes |  |
| `exchangeCurrency` | string, nullable | no |  |
| `exchangeRate` | number, nullable | no |  |
| `variableInvestmentCost` | number, nullable | no |  |
| `lifetime` | number | yes |  |
| `created` | string (date-time), nullable | no |  |
| `updated` | string (date-time), nullable | no |  |
| `hubs` | array of `HubResponseDto` | yes |  |
| `technologyModes` | array of `TechnologyModeResponseDtoV2`, nullable | no |  |
| `category` | string, nullable | no |  |
| `technologyCategory` | string, nullable | no |  |
| `mutuallyExclusiveGroup` | string, nullable | no |  |
| `notes` | string, nullable | no |  |
| `virtual` | boolean | yes |  |
| `technologyOptional` | boolean, nullable | no |  |
| `partOfTechnologyPackage` | boolean, nullable | no |  |
| `technologyCapacity` | string, nullable | no |  |
| `costComponents` | array of `AdvancedCostComponentResponseDto`, nullable | no |  |
| `comesFromDb` | string, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/conversion-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "fixedInvestmentCost": 0.0,
  "fixedOmCostChf": 0.0,
  "variableOmCostPercent": 0.0,
  "variableOmCostYear": 0.0,
  "variableOmCost": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "variableEmbodiedCo2": 0.0,
  "variableEmittedCo2": 0.0,
  "variableCapturedCo2": 0.0,
  "fixedReplacementCost": 0.0,
  "variableReplacementCostPercent": 0.0,
  "variableReplacementCostCHF": 0.0,
  "fixedSalvageValue": 0.0,
  "variableSalvageValuePercent": 0.0,
  "variableSalvageValueCHF": 0.0,
  "mustBeInstalledInHubs": "canBeInstalled",
  "conversionTechnologyGuid": "string",
  "processName": "string",
  "exchangeCurrency": "string",
  "exchangeRate": 0.0,
  "variableInvestmentCost": 0.0,
  "lifetime": 0.0,
  "created": "2026-01-01T00:00:00Z",
  "updated": "2026-01-01T00:00:00Z",
  "hubs": [
    {
      "hubGuid": "string",
      "hubName": "string",
      "updated": "2026-01-01T00:00:00Z",
      "created": "2026-01-01T00:00:00Z"
    }
  ],
  "technologyModes": [
    {
      "capacity": 0.0,
      "minimumAnnualOutput": 0.0,
      "maximumAnnualOutput": 0.0,
      "curtailmentLimitation": 0.0,
      "peakPower": 0.0,
      "minPartLoad": 0.0,
      "minimumUpTime": 0,
      "minimumDownTime": 0,
      "technologyModeGuid": "string",
      "inputEnergyCarriers": [
        {
          "energyCarrierGuid": "string",
          "typeKey": "string",
          "typeDisplayName": "string",
          "subtypeKey": "string",
          "subtypeDisplayName": "string",
          "energyCarrierName": "string",
          "colorHexCode": "string",
          "outputEfficiency": 0.0,
          "fixedInputShare": 0.0,
          "customOutputEfficiencyActivated": true,
          "customInputShareActivated": true,
          "customSeasonalityValues": [
            {
              "month": "JANUARY",
              "value": 0.0
            }
          ],
          "inputShareProfileId": 0,
          "outputEfficiencyProfileId": 0,
          "created": "2026-01-01T00:00:00Z",
          "primary": true
        }
      ],
      "outputEnergyCarriers": [
        {
          "energyCarrierGuid": "string",
          "typeKey": "string",
          "typeDisplayName": "string",
          "subtypeKey": "string",
          "subtypeDisplayName": "string",
          "energyCarrierName": "string",
          "colorHexCode": "string",
          "outputEfficiency": 0.0,
          "fixedInputShare": 0.0,
          "customOutputEfficiencyActivated": true,
          "customInputShareActivated": true,
          "customSeasonalityValues": [
            {
              "month": "JANUARY",
              "value": 0.0
            }
          ],
          "inputShareProfileId": 0,
          "outputEfficiencyProfileId": 0,
          "created": "2026-01-01T00:00:00Z",
          "primary": true
        }
      ],
      "seasonalOperationName": "string",
      "seasonalOperationValue": "string",
      "allowedOperationProfileId": 0,
      "primary": true,
      "maximumCapacity": 0.0,
      "minimumCapacity": 0.0,
      "simultaneousOperation": true
    }
  ],
  "category": "string",
  "technologyCategory": "string",
  "mutuallyExclusiveGroup": "string",
  "notes": "string",
  "virtual": true,
  "technologyOptional": true,
  "partOfTechnologyPackage": true,
  "technologyCapacity": "string",
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
  "comesFromDb": "string",
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoConversionTechnologyResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "conversionTechnologyGuid": "string",
    "processName": "string",
    "lifetime": 0,
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "conversionTechnologyModes": [
      {
        "capacity": 0.0,
        "minimumAnnualOutput": 0.0,
        "maximumAnnualOutput": 0.0,
        "curtailmentLimitation": 0.0,
        "peakPower": 0.0,
        "minPartLoad": 0.0,
        "minimumUpTime": 0,
        "minimumDownTime": 0,
        "technologyModeGuid": "string",
        "inputEnergyCarriers": [
          {
            "energyCarrierGuid": "string",
            "typeKey": "string",
            "typeDisplayName": "string",
            "subtypeKey": "string",
            "subtypeDisplayName": "string",
            "energyCarrierName": "string",
            "colorHexCode": "string",
            "outputEfficiency": 0.0,
            "fixedInputShare": 0.0,
            "customOutputEfficiencyActivated": true,
            "customInputShareActivated": true,
            "customSeasonalityValues": [
              {
                "month": null,
                "value": null
              }
            ],
            "inputShareProfileId": 0,
            "outputEfficiencyProfileId": 0,
            "created": "2026-01-01T00:00:00Z",
            "primary": true
          }
        ],
        "outputEnergyCarriers": [
          {
            "energyCarrierGuid": "string",
            "typeKey": "string",
            "typeDisplayName": "string",
            "subtypeKey": "string",
            "subtypeDisplayName": "string",
            "energyCarrierName": "string",
            "colorHexCode": "string",
            "outputEfficiency": 0.0,
            "fixedInputShare": 0.0,
            "customOutputEfficiencyActivated": true,
            "customInputShareActivated": true,
            "customSeasonalityValues": [
              {
                "month": null,
                "value": null
              }
            ],
            "inputShareProfileId": 0,
            "outputEfficiencyProfileId": 0,
            "created": "2026-01-01T00:00:00Z",
            "primary": true
          }
        ],
        "seasonalOperationName": "string",
        "seasonalOperationValue": "string",
        "allowedOperationProfileId": 0,
        "primary": true,
        "maximumCapacity": 0.0,
        "minimumCapacity": 0.0,
        "simultaneousOperation": true
      }
    ],
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "virtual": true,
    "mustBeInstalledInHubs": "canBeInstalled",
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

## Specify conversion technology v2 2 { #operation-specifyConversionTechnologyV2_2 }

```
POST /sympheny-app/v2_2/scenarios/{scenarioGuid}/conversion-technologies
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.conversion_technologies.create()`](../../sdk/reference/conversion_technologies.md#method-conversion_technologies-create).

Needs at least 1 mode. Each mode needs at least 1 carrier INPUT and 1 carrier OUTPUT. Cannot have same carrier in both INPUT and OUTPUT

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`ConversionTechnologyRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixedInvestmentCost` | number, nullable | no |  |
| `fixedOmCostChf` | number, nullable | no |  |
| `variableOmCostPercent` | number, nullable | no |  |
| `variableOmCostYear` | number, nullable | no |  |
| `variableOmCost` | number, nullable | no |  |
| `fixedEmbodiedCo2` | number, nullable | no |  |
| `variableEmbodiedCo2` | number, nullable | no |  |
| `variableEmittedCo2` | number, nullable | no |  |
| `variableCapturedCo2` | number, nullable | no |  |
| `fixedReplacementCost` | number, nullable | no |  |
| `variableReplacementCostPercent` | number, nullable | no |  |
| `variableReplacementCostCHF` | number, nullable | no |  |
| `fixedSalvageValue` | number, nullable | no |  |
| `variableSalvageValuePercent` | number, nullable | no |  |
| `variableSalvageValueCHF` | number, nullable | no |  |
| `mustBeInstalledInHubs` | string | yes | One of: `canBeInstalled`, `mustBeInstalled`, `mustBeInstalledInAtLeastOneHub`. |
| `processName` | string | yes |  |
| `variableInvestmentCost` | number, nullable | no |  |
| `lifetime` | integer (int32) | yes |  |
| `hubGuids` | array of string | yes |  |
| `conversionTechnologyModes` | array of `TechnologyModeRequestDtoV2` | yes |  |
| `virtual` | boolean | yes |  |
| `costComponents` | array of `AdvancedCostComponentRequestDto`, nullable | no |  |
| `suggested` | boolean, nullable | no |  |
| `technologyCategory` | string, nullable | no |  |
| `notes` | string, nullable | no |  |
| `source` | string, nullable | no |  |
| `comesFromDb` | string, nullable | no |  |
| `exchangeCurrency` | string | yes |  |
| `exchangeRate` | number | yes |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_2/scenarios/{scenarioGuid}/conversion-technologies" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "fixedInvestmentCost": 0.0,
  "fixedOmCostChf": 0.0,
  "variableOmCostPercent": 0.0,
  "variableOmCostYear": 0.0,
  "variableOmCost": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "variableEmbodiedCo2": 0.0,
  "variableEmittedCo2": 0.0,
  "variableCapturedCo2": 0.0,
  "fixedReplacementCost": 0.0,
  "variableReplacementCostPercent": 0.0,
  "variableReplacementCostCHF": 0.0,
  "fixedSalvageValue": 0.0,
  "variableSalvageValuePercent": 0.0,
  "variableSalvageValueCHF": 0.0,
  "mustBeInstalledInHubs": "canBeInstalled",
  "processName": "string",
  "variableInvestmentCost": 0.0,
  "lifetime": 0,
  "hubGuids": [
    "string"
  ],
  "conversionTechnologyModes": [
    {
      "capacity": 0.0,
      "minimumAnnualOutput": 0.0,
      "maximumAnnualOutput": 0.0,
      "curtailmentLimitation": 0.0,
      "peakPower": 0.0,
      "minPartLoad": 0.0,
      "minimumUpTime": 0,
      "minimumDownTime": 0,
      "primary": true,
      "seasonalOperation": "ALL_SEASONS",
      "allowedOperationProfileId": 0,
      "energyCarriers": [
        {
          "energyCarrierGuid": "string",
          "fixedInputShare": 0.0,
          "outputEfficiency": 0.0,
          "customInputShareActivated": true,
          "customOutputEfficiencyActivated": true,
          "inputShareProfileId": 0,
          "outputEfficiencyProfileId": 0,
          "customSeasonalityValues": [
            {
              "month": "JANUARY",
              "value": 0.0
            }
          ],
          "type": "INPUT",
          "primary": true
        }
      ],
      "maximumCapacity": 0.0,
      "minimumCapacity": 0.0,
      "simultaneousOperation": true
    }
  ],
  "virtual": true,
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
| 201 | Created | `ResponseDtoConversionTechnologyResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "conversionTechnologyGuid": "string",
    "processName": "string",
    "lifetime": 0,
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "conversionTechnologyModes": [
      {
        "capacity": 0.0,
        "minimumAnnualOutput": 0.0,
        "maximumAnnualOutput": 0.0,
        "curtailmentLimitation": 0.0,
        "peakPower": 0.0,
        "minPartLoad": 0.0,
        "minimumUpTime": 0,
        "minimumDownTime": 0,
        "technologyModeGuid": "string",
        "inputEnergyCarriers": [
          {
            "energyCarrierGuid": "string",
            "typeKey": "string",
            "typeDisplayName": "string",
            "subtypeKey": "string",
            "subtypeDisplayName": "string",
            "energyCarrierName": "string",
            "colorHexCode": "string",
            "outputEfficiency": 0.0,
            "fixedInputShare": 0.0,
            "customOutputEfficiencyActivated": true,
            "customInputShareActivated": true,
            "customSeasonalityValues": [
              {
                "month": null,
                "value": null
              }
            ],
            "inputShareProfileId": 0,
            "outputEfficiencyProfileId": 0,
            "created": "2026-01-01T00:00:00Z",
            "primary": true
          }
        ],
        "outputEnergyCarriers": [
          {
            "energyCarrierGuid": "string",
            "typeKey": "string",
            "typeDisplayName": "string",
            "subtypeKey": "string",
            "subtypeDisplayName": "string",
            "energyCarrierName": "string",
            "colorHexCode": "string",
            "outputEfficiency": 0.0,
            "fixedInputShare": 0.0,
            "customOutputEfficiencyActivated": true,
            "customInputShareActivated": true,
            "customSeasonalityValues": [
              {
                "month": null,
                "value": null
              }
            ],
            "inputShareProfileId": 0,
            "outputEfficiencyProfileId": 0,
            "created": "2026-01-01T00:00:00Z",
            "primary": true
          }
        ],
        "seasonalOperationName": "string",
        "seasonalOperationValue": "string",
        "allowedOperationProfileId": 0,
        "primary": true,
        "maximumCapacity": 0.0,
        "minimumCapacity": 0.0,
        "simultaneousOperation": true
      }
    ],
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "virtual": true,
    "mustBeInstalledInHubs": "canBeInstalled",
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
