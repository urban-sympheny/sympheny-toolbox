<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Imports and exports (impex)

## Delete impex { #operation-deleteImpex }

```
DELETE /sympheny-app/impex/{type}/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.impex.delete()`](../../sdk/reference/impex.md#method-impex-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | path | string | yes | One of: `IMPORT`, `EXPORT`. |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/impex/{type}/{guid}" \
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

## Get impex by guid v2 { #operation-getImpexByGuidV2 }

```
GET /sympheny-app/v2/impex/{type}/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.impex.get()`](../../sdk/reference/impex.md#method-impex-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | path | string | yes | One of: `IMPORT`, `EXPORT`. |
| `guid` | path | string | yes |  |
| `scenarioVariantGuid` | query | string | no |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/impex/{type}/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoImportExportResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "energyPriceCHFkWh": 0.0,
    "maxCapacityKW": 0.0,
    "totalAnnualEnergyAvailableKWhA": 0.0,
    "capacityPriceCHFkWYear": 0.0,
    "name": "string",
    "hourlyEnergyPriceProfileId": 0,
    "capacityPriceCHFkWMonth": 0.0,
    "fixedOmPriceCHFYear": 0.0,
    "co2IntensityKgCo2kWhCo2CompensationKgCo2kWh": 0.0,
    "dynamicCo2ProfileId": 0,
    "maximumHourlyEnergyAvailableProfileId": 0,
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
    "type": "string",
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "hubUpdated": "2026-01-01T00:00:00Z",
        "hubCreated": "2026-01-01T00:00:00Z",
        "impexGuid": "string"
      }
    ],
    "guid": "string",
    "updated": "2026-01-01T00:00:00Z",
    "created": "2026-01-01T00:00:00Z",
    "priceComponents": [
      {
        "name": "string",
        "guid": "string",
        "value": 0.0,
        "priceCategory": "string",
        "priceCategoryId": "ENERGY_DELIVERY",
        "priceDimension": "string",
        "priceDimensionId": "ENERGY_PRICE_CHF_KWH",
        "type": "TIME_OF_USE",
        "timeOfUses": [
          "string"
        ]
      }
    ],
    "timeOfUses": [
      {
        "name": "string",
        "months": [
          "string"
        ],
        "days": [
          "string"
        ],
        "startTime": "string",
        "endTime": "string"
      }
    ],
    "product": "string",
    "year": 0,
    "notes": "string",
    "source": "string",
    "suggested": true,
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

## Find all by scenario v2 { #operation-findAllByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/impexes
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.impex.list()`](../../sdk/reference/impex.md#method-impex-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/impexes" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListImportExportResponseDtoV2` |

**Example response** (200)

```json
{
  "data": [
    {
      "energyPriceCHFkWh": 0.0,
      "maxCapacityKW": 0.0,
      "totalAnnualEnergyAvailableKWhA": 0.0,
      "capacityPriceCHFkWYear": 0.0,
      "name": "string",
      "hourlyEnergyPriceProfileId": 0,
      "capacityPriceCHFkWMonth": 0.0,
      "fixedOmPriceCHFYear": 0.0,
      "co2IntensityKgCo2kWhCo2CompensationKgCo2kWh": 0.0,
      "dynamicCo2ProfileId": 0,
      "maximumHourlyEnergyAvailableProfileId": 0,
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
      "type": "string",
      "hubs": [
        {
          "hubGuid": "string",
          "hubName": "string",
          "hubUpdated": "2026-01-01T00:00:00Z",
          "hubCreated": "2026-01-01T00:00:00Z",
          "impexGuid": "string"
        }
      ],
      "guid": "string",
      "updated": "2026-01-01T00:00:00Z",
      "created": "2026-01-01T00:00:00Z",
      "priceComponents": [
        {
          "name": "string",
          "guid": "string",
          "value": 0.0,
          "priceCategory": "string",
          "priceCategoryId": "ENERGY_DELIVERY",
          "priceDimension": "string",
          "priceDimensionId": "ENERGY_PRICE_CHF_KWH",
          "type": "TIME_OF_USE",
          "timeOfUses": [
            "string"
          ]
        }
      ],
      "timeOfUses": [
        {
          "name": "string",
          "months": [
            "string"
          ],
          "days": [
            "string"
          ],
          "startTime": "string",
          "endTime": "string"
        }
      ],
      "product": "string",
      "year": 0,
      "notes": "string",
      "source": "string",
      "suggested": true,
      "stages": [
        "00000000-0000-0000-0000-000000000000"
      ]
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Create new impex v2 1 { #operation-createNewImpexV2_1 }

```
POST /sympheny-app/v2_1/scenario/{scenarioGuid}/impex
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.impex.create()`](../../sdk/reference/impex.md#method-impex-create).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`ImportExportRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energyPriceCHFkWh` | number, nullable | no |  |
| `maxCapacityKW` | number, nullable | no |  |
| `totalAnnualEnergyAvailableKWhA` | number, nullable | no |  |
| `capacityPriceCHFkWYear` | number, nullable | no |  |
| `name` | string | yes |  |
| `hourlyEnergyPriceProfileId` | integer (int64), nullable | no |  |
| `capacityPriceCHFkWMonth` | number, nullable | no |  |
| `fixedOmPriceCHFYear` | number, nullable | no |  |
| `co2IntensityKgCo2kWhCo2CompensationKgCo2kWh` | number, nullable | no |  |
| `dynamicCo2ProfileId` | integer (int64), nullable | no |  |
| `maximumHourlyEnergyAvailableProfileId` | integer (int64), nullable | no |  |
| `energyCarrierGuid` | string | yes |  |
| `type` | string | yes | One of: `IMPORT`, `EXPORT`. |
| `hubs` | array of `ImpexHubRequestDto` | yes |  |
| `product` | string, nullable | no |  |
| `year` | integer (int32), nullable | no |  |
| `notes` | string, nullable | no |  |
| `source` | string, nullable | no |  |
| `suggested` | boolean, nullable | no |  |
| `priceComponents` | array of `AdvancedPriceComponentRequestDtoV2`, nullable | no |  |
| `timeOfUses` | array of `TimeOfUseRequestDto`, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenario/{scenarioGuid}/impex" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "energyPriceCHFkWh": 0.0,
  "maxCapacityKW": 0.0,
  "totalAnnualEnergyAvailableKWhA": 0.0,
  "capacityPriceCHFkWYear": 0.0,
  "name": "string",
  "hourlyEnergyPriceProfileId": 0,
  "capacityPriceCHFkWMonth": 0.0,
  "fixedOmPriceCHFYear": 0.0,
  "co2IntensityKgCo2kWhCo2CompensationKgCo2kWh": 0.0,
  "dynamicCo2ProfileId": 0,
  "maximumHourlyEnergyAvailableProfileId": 0,
  "energyCarrierGuid": "string",
  "type": "IMPORT",
  "hubs": [
    {
      "hubGuid": "string"
    }
  ],
  "product": "string",
  "year": 0,
  "notes": "string",
  "source": "string",
  "suggested": true,
  "priceComponents": [
    {
      "name": "string",
      "value": 0.0,
      "priceCategory": "ENERGY_DELIVERY",
      "priceDimension": "ENERGY_PRICE_CHF_KWH",
      "type": "TIME_OF_USE",
      "timeOfUses": [
        "string"
      ],
      "priceCategoryId": "ENERGY_DELIVERY",
      "priceDimensionId": "ENERGY_PRICE_CHF_KWH"
    }
  ],
  "timeOfUses": [
    {
      "name": "string",
      "months": [
        "string"
      ],
      "days": [
        "string"
      ],
      "startTime": "string",
      "endTime": "string"
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
| 201 | Created | `ResponseDtoImportExportResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "energyPriceCHFkWh": 0.0,
    "maxCapacityKW": 0.0,
    "totalAnnualEnergyAvailableKWhA": 0.0,
    "capacityPriceCHFkWYear": 0.0,
    "name": "string",
    "hourlyEnergyPriceProfileId": 0,
    "capacityPriceCHFkWMonth": 0.0,
    "fixedOmPriceCHFYear": 0.0,
    "co2IntensityKgCo2kWhCo2CompensationKgCo2kWh": 0.0,
    "dynamicCo2ProfileId": 0,
    "maximumHourlyEnergyAvailableProfileId": 0,
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
    "type": "string",
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "hubUpdated": "2026-01-01T00:00:00Z",
        "hubCreated": "2026-01-01T00:00:00Z",
        "impexGuid": "string"
      }
    ],
    "guid": "string",
    "updated": "2026-01-01T00:00:00Z",
    "created": "2026-01-01T00:00:00Z",
    "priceComponents": [
      {
        "name": "string",
        "guid": "string",
        "value": 0.0,
        "priceCategory": "string",
        "priceCategoryId": "ENERGY_DELIVERY",
        "priceDimension": "string",
        "priceDimensionId": "ENERGY_PRICE_CHF_KWH",
        "type": "TIME_OF_USE",
        "timeOfUses": [
          "string"
        ]
      }
    ],
    "timeOfUses": [
      {
        "name": "string",
        "months": [
          "string"
        ],
        "days": [
          "string"
        ],
        "startTime": "string",
        "endTime": "string"
      }
    ],
    "product": "string",
    "year": 0,
    "notes": "string",
    "source": "string",
    "suggested": true,
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

## Edit impex v2 1 { #operation-editImpexV2_1 }

```
PUT /sympheny-app/v2_1/scenarios/impex/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.impex.update()`](../../sdk/reference/impex.md#method-impex-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Request body** (`ImportExportResponseDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energyPriceCHFkWh` | number, nullable | no |  |
| `maxCapacityKW` | number, nullable | no |  |
| `totalAnnualEnergyAvailableKWhA` | number, nullable | no |  |
| `capacityPriceCHFkWYear` | number, nullable | no |  |
| `name` | string | yes |  |
| `hourlyEnergyPriceProfileId` | integer (int64), nullable | no |  |
| `capacityPriceCHFkWMonth` | number, nullable | no |  |
| `fixedOmPriceCHFYear` | number, nullable | no |  |
| `co2IntensityKgCo2kWhCo2CompensationKgCo2kWh` | number, nullable | no |  |
| `dynamicCo2ProfileId` | integer (int64), nullable | no |  |
| `maximumHourlyEnergyAvailableProfileId` | integer (int64), nullable | no |  |
| `energyCarrier` | `EnergyCarrierResponseDto` | yes |  |
| `type` | string | yes |  |
| `hubs` | array of `ImpexHubResponseDto` | yes |  |
| `guid` | string, nullable | no |  |
| `updated` | string (date-time), nullable | no |  |
| `created` | string (date-time), nullable | no |  |
| `priceComponents` | array of `AdvancedPriceComponentResponseDtoV2` | yes |  |
| `timeOfUses` | array of `TimeOfUseResponseDto` | yes |  |
| `product` | string, nullable | no |  |
| `year` | integer (int32), nullable | no |  |
| `notes` | string, nullable | no |  |
| `source` | string, nullable | no |  |
| `suggested` | boolean, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/impex/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "energyPriceCHFkWh": 0.0,
  "maxCapacityKW": 0.0,
  "totalAnnualEnergyAvailableKWhA": 0.0,
  "capacityPriceCHFkWYear": 0.0,
  "name": "string",
  "hourlyEnergyPriceProfileId": 0,
  "capacityPriceCHFkWMonth": 0.0,
  "fixedOmPriceCHFYear": 0.0,
  "co2IntensityKgCo2kWhCo2CompensationKgCo2kWh": 0.0,
  "dynamicCo2ProfileId": 0,
  "maximumHourlyEnergyAvailableProfileId": 0,
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
  "type": "string",
  "hubs": [
    {
      "hubGuid": "string",
      "hubName": "string",
      "hubUpdated": "2026-01-01T00:00:00Z",
      "hubCreated": "2026-01-01T00:00:00Z",
      "impexGuid": "string"
    }
  ],
  "guid": "string",
  "updated": "2026-01-01T00:00:00Z",
  "created": "2026-01-01T00:00:00Z",
  "priceComponents": [
    {
      "name": "string",
      "guid": "string",
      "value": 0.0,
      "priceCategory": "string",
      "priceCategoryId": "ENERGY_DELIVERY",
      "priceDimension": "string",
      "priceDimensionId": "ENERGY_PRICE_CHF_KWH",
      "type": "TIME_OF_USE",
      "timeOfUses": [
        "string"
      ]
    }
  ],
  "timeOfUses": [
    {
      "name": "string",
      "months": [
        "string"
      ],
      "days": [
        "string"
      ],
      "startTime": "string",
      "endTime": "string"
    }
  ],
  "product": "string",
  "year": 0,
  "notes": "string",
  "source": "string",
  "suggested": true,
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ]
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoImportExportResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "energyPriceCHFkWh": 0.0,
    "maxCapacityKW": 0.0,
    "totalAnnualEnergyAvailableKWhA": 0.0,
    "capacityPriceCHFkWYear": 0.0,
    "name": "string",
    "hourlyEnergyPriceProfileId": 0,
    "capacityPriceCHFkWMonth": 0.0,
    "fixedOmPriceCHFYear": 0.0,
    "co2IntensityKgCo2kWhCo2CompensationKgCo2kWh": 0.0,
    "dynamicCo2ProfileId": 0,
    "maximumHourlyEnergyAvailableProfileId": 0,
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
    "type": "string",
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "hubUpdated": "2026-01-01T00:00:00Z",
        "hubCreated": "2026-01-01T00:00:00Z",
        "impexGuid": "string"
      }
    ],
    "guid": "string",
    "updated": "2026-01-01T00:00:00Z",
    "created": "2026-01-01T00:00:00Z",
    "priceComponents": [
      {
        "name": "string",
        "guid": "string",
        "value": 0.0,
        "priceCategory": "string",
        "priceCategoryId": "ENERGY_DELIVERY",
        "priceDimension": "string",
        "priceDimensionId": "ENERGY_PRICE_CHF_KWH",
        "type": "TIME_OF_USE",
        "timeOfUses": [
          "string"
        ]
      }
    ],
    "timeOfUses": [
      {
        "name": "string",
        "months": [
          "string"
        ],
        "days": [
          "string"
        ],
        "startTime": "string",
        "endTime": "string"
      }
    ],
    "product": "string",
    "year": 0,
    "notes": "string",
    "source": "string",
    "suggested": true,
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
