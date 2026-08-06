<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Storage technologies

## Delete storage technology { #operation-deleteStorageTechnology }

```
DELETE /sympheny-app/scenarios/storage-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.storage_technologies.delete()`](../../sdk/reference/storage_technologies.md#method-storage_technologies-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/storage-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStorageTechnologyListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "storageTechnologies": [
      {
        "storageTechnologyGuid": "string",
        "storageName": "string",
        "lifetime": 0.0,
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
        "hubs": [
          {
            "hubGuid": "string",
            "hubName": "string",
            "updated": "2026-01-01T00:00:00Z",
            "created": "2026-01-01T00:00:00Z"
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

## Get storage tech details v2 { #operation-getStorageTechDetailsV2 }

```
GET /sympheny-app/v2/scenarios/storage-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.storage_technologies.get()`](../../sdk/reference/storage_technologies.md#method-storage_technologies-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/storage-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStorageTechnologyDetailResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "variableOmCostPercent": 0.0,
    "variableOmEnergyFlowCost": 0.0,
    "capacity": 0.0,
    "maximumCapacity": 0.0,
    "minimumCapacity": 0.0,
    "fixedInvestmentCost": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "variableOmCost": 0.0,
    "maximumChargingRate": 0.0,
    "maximumDischargingRate": 0.0,
    "variableEmbodiedCo2": 0.0,
    "fixedReplacementCost": 0.0,
    "variableReplacementCostPercent": 0.0,
    "variableReplacementCostCHF": 0.0,
    "fixedSalvageValue": 0.0,
    "variableSalvageValuePercent": 0.0,
    "variableSalvageValueCHF": 0.0,
    "mustBeInstalled": "string",
    "storageTechnologyGuid": "string",
    "storageName": "string",
    "exchangeCurrency": "string",
    "exchangeRate": 0.0,
    "variableInvestmentCost": 0.0,
    "fixedOmCostChf": 0.0,
    "lifetime": 0,
    "standbyLoss": 0.0,
    "standByLossProfileId": 0,
    "minimumSoc": 0.0,
    "storageChargingEfficiency": 0.0,
    "storageDischargingEfficiency": 0.0,
    "technologyCapacity": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "storageCarrier": {
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
    "category": "string",
    "technologyCategory": "string",
    "mutuallyExclusiveGroup": "string",
    "notes": "string",
    "source": "string",
    "technologyOptional": true,
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
    ],
    "evPlugInTime": {
      "hour": 0,
      "minute": 0,
      "second": 0,
      "nano": 0
    },
    "evPlugOutTime": {
      "hour": 0,
      "minute": 0,
      "second": 0,
      "nano": 0
    },
    "evPlugInDurationHours": 0.0,
    "drivingDistanceKms": 0.0,
    "evSocStartPercent": 0.0,
    "evBatterySizeKWh": 0.0,
    "maximumSocPercent": 0.0,
    "evAverageKWhPerKm": 0.0,
    "evPlugInPowerKW": 0.0,
    "isEvBattery": true,
    "typeOfCharging": "Smart"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Get all storage technologies by scenario v2 { #operation-getAllStorageTechnologiesByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/storage-technologies
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.storage_technologies.list()`](../../sdk/reference/storage_technologies.md#method-storage_technologies-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/storage-technologies" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStorageTechnologyListResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "storageTechnologies": [
      {
        "storageTechnologyGuid": "string",
        "storageName": "string",
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
        "stages": [
          "00000000-0000-0000-0000-000000000000"
        ],
        "standByLossProfileId": 0
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

## Specify storage technology v2 1 { #operation-specifyStorageTechnologyV2_1 }

```
POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/storage-technologies
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.storage_technologies.create()`](../../sdk/reference/storage_technologies.md#method-storage_technologies-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`StorageTechnologyRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `variableOmCostPercent` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableOmEnergyFlowCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `capacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `maximumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `minimumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedInvestmentCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedEmbodiedCo2` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableOmCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `maximumChargingRate` | number, nullable | no |  |
| `maximumDischargingRate` | number, nullable | no |  |
| `variableEmbodiedCo2` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedReplacementCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableReplacementCostPercent` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableReplacementCostCHF` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedSalvageValue` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableSalvageValuePercent` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableSalvageValueCHF` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `mustBeInstalled` | string | yes |  |
| `storageName` | string | yes |  |
| `variableInvestmentCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedOmCostChf` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `lifetime` | integer (int32) | yes |  |
| `standbyLoss` | number, nullable | no |  |
| `standByLossProfileId` | integer (int64), nullable | no |  |
| `minimumSoc` | number, nullable | no |  |
| `hubGuids` | array of string | yes |  |
| `energyCarrierGuid` | string | yes |  |
| `storageChargingEfficiency` | number | yes |  |
| `storageDischargingEfficiency` | number | yes |  |
| `technologyCapacity` | string | yes |  |
| `costComponents` | array of `AdvancedCostComponentRequestDto`, nullable | no |  |
| `suggested` | boolean, nullable | no |  |
| `technologyCategory` | string, nullable | no |  |
| `notes` | string, nullable | no |  |
| `source` | string, nullable | no |  |
| `comesFromDb` | string, nullable | no |  |
| `exchangeCurrency` | string, nullable | no |  |
| `exchangeRate` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `stages` | array of string (uuid) | yes |  |
| `evPlugInTime` | `LocalTime`, nullable | no |  |
| `evPlugOutTime` | `LocalTime`, nullable | no |  |
| `evPlugInDurationHours` | number, nullable | no |  |
| `drivingDistanceKms` | number, nullable | no |  |
| `evSocStartPercent` | number, nullable | no |  |
| `evBatterySizeKWh` | number, nullable | no |  |
| `maximumSocPercent` | number, nullable | no |  |
| `evAverageKWhPerKm` | number, nullable | no |  |
| `evPlugInPowerKW` | number, nullable | no |  |
| `isEvBattery` | boolean, nullable | no |  |
| `typeOfCharging` | string, nullable | no | One of: `Smart`, `Dump`, `V2G`, `None`, `None`. |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/{scenarioGuid}/storage-technologies" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "variableOmCostPercent": 0.0,
  "variableOmEnergyFlowCost": 0.0,
  "capacity": 0.0,
  "maximumCapacity": 0.0,
  "minimumCapacity": 0.0,
  "fixedInvestmentCost": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "variableOmCost": 0.0,
  "maximumChargingRate": 0.0,
  "maximumDischargingRate": 0.0,
  "variableEmbodiedCo2": 0.0,
  "fixedReplacementCost": 0.0,
  "variableReplacementCostPercent": 0.0,
  "variableReplacementCostCHF": 0.0,
  "fixedSalvageValue": 0.0,
  "variableSalvageValuePercent": 0.0,
  "variableSalvageValueCHF": 0.0,
  "mustBeInstalled": "string",
  "storageName": "string",
  "variableInvestmentCost": 0.0,
  "fixedOmCostChf": 0.0,
  "lifetime": 0,
  "standbyLoss": 0.0,
  "standByLossProfileId": 0,
  "minimumSoc": 0.0,
  "hubGuids": [
    "string"
  ],
  "energyCarrierGuid": "string",
  "storageChargingEfficiency": 0.0,
  "storageDischargingEfficiency": 0.0,
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
  ],
  "evPlugInTime": {
    "hour": 0,
    "minute": 0,
    "second": 0,
    "nano": 0
  },
  "evPlugOutTime": {
    "hour": 0,
    "minute": 0,
    "second": 0,
    "nano": 0
  },
  "evPlugInDurationHours": 0.0,
  "drivingDistanceKms": 0.0,
  "evSocStartPercent": 0.0,
  "evBatterySizeKWh": 0.0,
  "maximumSocPercent": 0.0,
  "evAverageKWhPerKm": 0.0,
  "evPlugInPowerKW": 0.0,
  "isEvBattery": true,
  "typeOfCharging": "Smart"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoStorageTechnologyResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "storageTechnologyGuid": "string",
    "storageName": "string",
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
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "standByLossProfileId": 0
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Update storage technology v2 2 { #operation-updateStorageTechnologyV2_2 }

```
PUT /sympheny-app/v2_2/scenarios/storage-technologies/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.storage_technologies.update()`](../../sdk/reference/storage_technologies.md#method-storage_technologies-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`StorageTechnologyRequestDtoPUT`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `variableOmCostPercent` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableOmEnergyFlowCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `capacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `maximumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `minimumCapacity` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedInvestmentCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedEmbodiedCo2` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableOmCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `maximumChargingRate` | number, nullable | no |  |
| `maximumDischargingRate` | number, nullable | no |  |
| `variableEmbodiedCo2` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedReplacementCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableReplacementCostPercent` | number | yes | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableReplacementCostCHF` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedSalvageValue` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableSalvageValuePercent` | number | yes | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableSalvageValueCHF` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `mustBeInstalled` | string | yes |  |
| `storageName` | string | yes |  |
| `exchangeCurrency` | string | yes |  |
| `exchangeRate` | number | yes | Invalid NUMERIC. Max precision=16, max scale=5. |
| `variableInvestmentCost` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `fixedOmCostChf` | number, nullable | no | Invalid NUMERIC. Max precision=16, max scale=5. |
| `lifetime` | integer (int32) | yes |  |
| `standbyLoss` | number, nullable | no |  |
| `standByLossProfileId` | integer (int64), nullable | no |  |
| `minimumSoc` | number, nullable | no |  |
| `storageChargingEfficiency` | number | yes |  |
| `storageDischargingEfficiency` | number | yes |  |
| `technologyCapacity` | string | yes |  |
| `storageCarrier` | `EnergyCarrierRequestDtoPUTId` | yes |  |
| `hubs` | array of `HubRequestDtoPUTId` | yes |  |
| `category` | string | yes |  |
| `technologyCategory` | string, nullable | no |  |
| `mutuallyExclusiveGroup` | string, nullable | no |  |
| `notes` | string, nullable | no |  |
| `source` | string, nullable | no |  |
| `technologyOptional` | boolean, nullable | no |  |
| `costComponents` | array of `AdvancedCostComponentResponseDto`, nullable | no |  |
| `comesFromDb` | string, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |
| `evPlugInTime` | `LocalTime`, nullable | no |  |
| `evPlugOutTime` | `LocalTime`, nullable | no |  |
| `evPlugInDurationHours` | number, nullable | no |  |
| `drivingDistanceKms` | number, nullable | no |  |
| `evSocStartPercent` | number, nullable | no |  |
| `evBatterySizeKWh` | number, nullable | no |  |
| `maximumSocPercent` | number, nullable | no |  |
| `evAverageKWhPerKm` | number, nullable | no |  |
| `evPlugInPowerKW` | number, nullable | no |  |
| `isEvBattery` | boolean, nullable | no |  |
| `typeOfCharging` | string, nullable | no | One of: `Smart`, `Dump`, `V2G`, `None`, `None`. |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_2/scenarios/storage-technologies/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "variableOmCostPercent": 0.0,
  "variableOmEnergyFlowCost": 0.0,
  "capacity": 0.0,
  "maximumCapacity": 0.0,
  "minimumCapacity": 0.0,
  "fixedInvestmentCost": 0.0,
  "fixedEmbodiedCo2": 0.0,
  "variableOmCost": 0.0,
  "maximumChargingRate": 0.0,
  "maximumDischargingRate": 0.0,
  "variableEmbodiedCo2": 0.0,
  "fixedReplacementCost": 0.0,
  "variableReplacementCostPercent": 0.0,
  "variableReplacementCostCHF": 0.0,
  "fixedSalvageValue": 0.0,
  "variableSalvageValuePercent": 0.0,
  "variableSalvageValueCHF": 0.0,
  "mustBeInstalled": "string",
  "storageName": "string",
  "exchangeCurrency": "string",
  "exchangeRate": 0.0,
  "variableInvestmentCost": 0.0,
  "fixedOmCostChf": 0.0,
  "lifetime": 0,
  "standbyLoss": 0.0,
  "standByLossProfileId": 0,
  "minimumSoc": 0.0,
  "storageChargingEfficiency": 0.0,
  "storageDischargingEfficiency": 0.0,
  "technologyCapacity": "string",
  "storageCarrier": {
    "energyCarrierGuid": "string"
  },
  "hubs": [
    {
      "hubGuid": "string"
    }
  ],
  "category": "string",
  "technologyCategory": "string",
  "mutuallyExclusiveGroup": "string",
  "notes": "string",
  "source": "string",
  "technologyOptional": true,
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
  ],
  "evPlugInTime": {
    "hour": 0,
    "minute": 0,
    "second": 0,
    "nano": 0
  },
  "evPlugOutTime": {
    "hour": 0,
    "minute": 0,
    "second": 0,
    "nano": 0
  },
  "evPlugInDurationHours": 0.0,
  "drivingDistanceKms": 0.0,
  "evSocStartPercent": 0.0,
  "evBatterySizeKWh": 0.0,
  "maximumSocPercent": 0.0,
  "evAverageKWhPerKm": 0.0,
  "evPlugInPowerKW": 0.0,
  "isEvBattery": true,
  "typeOfCharging": "Smart"
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoStorageTechnologyDetailResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "variableOmCostPercent": 0.0,
    "variableOmEnergyFlowCost": 0.0,
    "capacity": 0.0,
    "maximumCapacity": 0.0,
    "minimumCapacity": 0.0,
    "fixedInvestmentCost": 0.0,
    "fixedEmbodiedCo2": 0.0,
    "variableOmCost": 0.0,
    "maximumChargingRate": 0.0,
    "maximumDischargingRate": 0.0,
    "variableEmbodiedCo2": 0.0,
    "fixedReplacementCost": 0.0,
    "variableReplacementCostPercent": 0.0,
    "variableReplacementCostCHF": 0.0,
    "fixedSalvageValue": 0.0,
    "variableSalvageValuePercent": 0.0,
    "variableSalvageValueCHF": 0.0,
    "mustBeInstalled": "string",
    "storageTechnologyGuid": "string",
    "storageName": "string",
    "exchangeCurrency": "string",
    "exchangeRate": 0.0,
    "variableInvestmentCost": 0.0,
    "fixedOmCostChf": 0.0,
    "lifetime": 0,
    "standbyLoss": 0.0,
    "standByLossProfileId": 0,
    "minimumSoc": 0.0,
    "storageChargingEfficiency": 0.0,
    "storageDischargingEfficiency": 0.0,
    "technologyCapacity": "string",
    "created": "2026-01-01T00:00:00Z",
    "updated": "2026-01-01T00:00:00Z",
    "storageCarrier": {
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
    "category": "string",
    "technologyCategory": "string",
    "mutuallyExclusiveGroup": "string",
    "notes": "string",
    "source": "string",
    "technologyOptional": true,
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
    ],
    "evPlugInTime": {
      "hour": 0,
      "minute": 0,
      "second": 0,
      "nano": 0
    },
    "evPlugOutTime": {
      "hour": 0,
      "minute": 0,
      "second": 0,
      "nano": 0
    },
    "evPlugInDurationHours": 0.0,
    "drivingDistanceKms": 0.0,
    "evSocStartPercent": 0.0,
    "evBatterySizeKWh": 0.0,
    "maximumSocPercent": 0.0,
    "evAverageKWhPerKm": 0.0,
    "evPlugInPowerKW": 0.0,
    "isEvBattery": true,
    "typeOfCharging": "Smart"
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
