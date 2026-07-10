<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Energy demands

## Delete energy demand profile { #operation-deleteEnergyDemandProfile }

```
DELETE /sympheny-app/scenarios/energy-demands/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_demands.delete()`](../../sdk/reference/energy_demands.md#method-energy_demands-delete).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |

**Example request**

```bash
curl -X DELETE "https://eu-north-1-api.sympheny.com/sympheny-app/scenarios/energy-demands/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoEnergyDemandListResponseDto` |

**Example response** (200)

```json
{
  "data": {
    "energyDemands": [
      {
        "energyDemandGuid": "string",
        "energyCarrierName": "string",
        "hubName": "string",
        "energyDemandName": "string",
        "energyCarrierGuid": "string",
        "hubGuid": "string",
        "demandSalePrice": 0.0,
        "energyDemandUserSavedMetadataGuid": "string",
        "energyDemandUserSavedMetadataName": "string",
        "energyDemandUserSavedMetadataReferenceArea": 0.0,
        "scalingFactor": 0.0,
        "energyDemandMetadataGuid": "string",
        "energyDemandMetadataName": "string",
        "energyDemandMetadataDbOrganization": "string",
        "energyDemandMetadataType": "ELECTRICITY",
        "energyDemandMetadataBuildingType": "RESIDENCE_MFH",
        "energyDemandMetadataBuildingAge": "AGE_UNDER_1970",
        "energyDemandMetadataOption": "OPTION_1",
        "energyDemandMetadataReferencedAreaM2": 0.0,
        "energyDemandMetadataSpecificEnergyDemandValueKWhM2": 0.0,
        "energyDemandMetadataTotalAnnualDemand": 0.0,
        "multiplicationFactorPreview": 0,
        "multiplicationFactor": 0
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

## Get energy demand details by guid v2 { #operation-getEnergyDemandDetailsByGuidV2 }

```
GET /sympheny-app/v2/energy-demands/{guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_demands.get()`](../../sdk/reference/energy_demands.md#method-energy_demands-get).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `guid` | path | string | yes |  |
| `scenarioVariantGuid` | query | string | no |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/energy-demands/{guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoEnergyDemandDetailResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "energyDemandGuid": "string",
    "energyDemandName": "string",
    "energyCarrierGuid": "string",
    "energyCarrierName": "string",
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "demandSalePrice": 0.0,
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "demandProfileId": 0,
    "demandScalingFactor": 0.0,
    "demandSalePriceProfileId": 0,
    "demandSalePriceScalingFactor": 0.0,
    "energyDemandUserSavedMetadataGuid": "string",
    "energyDemandUserSavedMetadataName": "string",
    "energyDemandUserSavedMetadataReferenceArea": 0.0,
    "scalingFactor": 0.0,
    "energyDemandMetadataGuid": "string",
    "energyDemandMetadataName": "string",
    "energyDemandMetadataDbOrganization": "string",
    "energyDemandMetadataType": "ELECTRICITY",
    "energyDemandMetadataBuildingType": "RESIDENCE_MFH",
    "energyDemandMetadataBuildingAge": "AGE_UNDER_1970",
    "energyDemandMetadataOption": "OPTION_1",
    "energyDemandMetadataReferencedAreaM2": 0.0,
    "energyDemandMetadataSpecificEnergyDemandValueKWhM2": 0.0,
    "energyDemandMetadataTotalAnnualDemand": 0.0,
    "multiplicationFactorPreview": 0,
    "multiplicationFactor": 0,
    "reverse": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Get all energy demands by scenario v2 { #operation-getAllEnergyDemandsByScenarioV2 }

```
GET /sympheny-app/v2/scenarios/{scenarioGuid}/energy-demands
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_demands.list()`](../../sdk/reference/energy_demands.md#method-energy_demands-list).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/v2/scenarios/{scenarioGuid}/energy-demands" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListEnergyDemandResponseDtoV2` |

**Example response** (200)

```json
{
  "data": [
    {
      "energyDemandGuid": "string",
      "energyCarrierName": "string",
      "hubs": [
        {
          "hubGuid": "string",
          "hubName": "string",
          "updated": "2026-01-01T00:00:00Z",
          "created": "2026-01-01T00:00:00Z"
        }
      ],
      "energyDemandName": "string",
      "energyCarrierGuid": "string",
      "demandSalePrice": 0.0,
      "stages": [
        "00000000-0000-0000-0000-000000000000"
      ],
      "demandProfileId": 0,
      "demandScalingFactor": 0.0,
      "demandSalePriceProfileId": 0,
      "demandSalePriceScalingFactor": 0.0,
      "energyDemandUserSavedMetadataGuid": "string",
      "energyDemandUserSavedMetadataName": "string",
      "energyDemandUserSavedMetadataReferenceArea": 0.0,
      "scalingFactor": 0.0,
      "energyDemandMetadataGuid": "string",
      "energyDemandMetadataName": "string",
      "energyDemandMetadataDbOrganization": "string",
      "energyDemandMetadataType": "ELECTRICITY",
      "energyDemandMetadataBuildingType": "RESIDENCE_MFH",
      "energyDemandMetadataBuildingAge": "AGE_UNDER_1970",
      "energyDemandMetadataOption": "OPTION_1",
      "energyDemandMetadataReferencedAreaM2": 0.0,
      "energyDemandMetadataSpecificEnergyDemandValueKWhM2": 0.0,
      "energyDemandMetadataTotalAnnualDemand": 0.0,
      "multiplicationFactorPreview": 0,
      "multiplicationFactor": 0,
      "reverse": true
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Upload new energy demand profile v2 1 { #operation-uploadNewEnergyDemandProfileV2_1 }

```
POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/energy-demands
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_demands.create()`](../../sdk/reference/energy_demands.md#method-energy_demands-create).

demandProfileId and demandSalePrice must be exclusive

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |

**Request body** (`EnergyDemandRequestDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hubGuids` | array of string | yes |  |
| `energyCarrierGuid` | string | yes |  |
| `demandProfileId` | integer (int64) | yes |  |
| `demandScalingFactor` | number, nullable | no |  |
| `name` | string | yes |  |
| `demandSalePrice` | number, nullable | no |  |
| `demandSalePriceProfileId` | integer (int64), nullable | no |  |
| `demandSalePriceScalingFactor` | number, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |
| `multiplicationFactor` | integer (int32), nullable | no |  |
| `reverse` | boolean, nullable | no |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/v2_1/scenarios/{scenarioGuid}/energy-demands" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "hubGuids": [
    "string"
  ],
  "energyCarrierGuid": "string",
  "demandProfileId": 0,
  "demandScalingFactor": 0.0,
  "name": "string",
  "demandSalePrice": 0.0,
  "demandSalePriceProfileId": 0,
  "demandSalePriceScalingFactor": 0.0,
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ],
  "multiplicationFactor": 0,
  "reverse": true
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 201 | Created | `ResponseDtoEnergyDemandResponseDtoV2` |

**Example response** (201)

```json
{
  "data": {
    "energyDemandGuid": "string",
    "energyCarrierName": "string",
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "energyDemandName": "string",
    "energyCarrierGuid": "string",
    "demandSalePrice": 0.0,
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "demandProfileId": 0,
    "demandScalingFactor": 0.0,
    "demandSalePriceProfileId": 0,
    "demandSalePriceScalingFactor": 0.0,
    "energyDemandUserSavedMetadataGuid": "string",
    "energyDemandUserSavedMetadataName": "string",
    "energyDemandUserSavedMetadataReferenceArea": 0.0,
    "scalingFactor": 0.0,
    "energyDemandMetadataGuid": "string",
    "energyDemandMetadataName": "string",
    "energyDemandMetadataDbOrganization": "string",
    "energyDemandMetadataType": "ELECTRICITY",
    "energyDemandMetadataBuildingType": "RESIDENCE_MFH",
    "energyDemandMetadataBuildingAge": "AGE_UNDER_1970",
    "energyDemandMetadataOption": "OPTION_1",
    "energyDemandMetadataReferencedAreaM2": 0.0,
    "energyDemandMetadataSpecificEnergyDemandValueKWhM2": 0.0,
    "energyDemandMetadataTotalAnnualDemand": 0.0,
    "multiplicationFactorPreview": 0,
    "multiplicationFactor": 0,
    "reverse": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Update energy demand v2 2 { #operation-updateEnergyDemandV2_2 }

```
PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/energy-demands/{demand-guid}
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_demands.update()`](../../sdk/reference/energy_demands.md#method-energy_demands-update).

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scenarioGuid` | path | string | yes |  |
| `demand-guid` | path | string | yes |  |

**Request body** (`EnergyDemandResponseDtoV2`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energyDemandGuid` | string, nullable | no |  |
| `energyCarrierName` | string | yes |  |
| `hubs` | array of `HubResponseDto` | yes |  |
| `energyDemandName` | string | yes |  |
| `energyCarrierGuid` | string | yes |  |
| `demandSalePrice` | number, nullable | no |  |
| `stages` | array of string (uuid) | yes |  |
| `demandProfileId` | integer (int64) | yes |  |
| `demandScalingFactor` | number, nullable | no |  |
| `demandSalePriceProfileId` | integer (int64), nullable | no |  |
| `demandSalePriceScalingFactor` | number, nullable | no |  |
| `energyDemandUserSavedMetadataGuid` | string, nullable | no |  |
| `energyDemandUserSavedMetadataName` | string, nullable | no |  |
| `energyDemandUserSavedMetadataReferenceArea` | number, nullable | no |  |
| `scalingFactor` | number, nullable | no |  |
| `energyDemandMetadataGuid` | string, nullable | no |  |
| `energyDemandMetadataName` | string, nullable | no |  |
| `energyDemandMetadataDbOrganization` | string, nullable | no |  |
| `energyDemandMetadataType` | string, nullable | no | One of: `ELECTRICITY`, `SPACE_HEATING`, `HOT_WATER`, `COOLING`, `None`. |
| `energyDemandMetadataBuildingType` | string, nullable | no | One of: `RESIDENCE_MFH`, `RESIDENCE_SFH`, `ADMINISTRATION`, `OFFICES`, `SCHOOLS`, `RETAIL`, `RESTAURANT`, `ASSEMBLY`, `HOSPITALS`, `INDUSTRY`, `WAREHOUSE`, `SPORTS_CENTER`, `INDOOR_POOL`, `HOTEL`, `INDUSTRY_1_SHIFT_FABRICATED_METALS`, `INDUSTRY_2_SHIFT_FABRICATED_METALS`, `INDUSTRY_FOOD_PROCESSING`, `INDUSTRY_GENERAL_MANUFACTURER`, `INDUSTRY_PHARMACEUTICAL`, `INDUSTRY_PLASTIC_MANUFACTURER`, `INDUSTRY_SERVICES`, `INDUSTRY_WAREHOUSE`, `None`. |
| `energyDemandMetadataBuildingAge` | string, nullable | no | One of: `AGE_UNDER_1970`, `AGE_1970_1980`, `AGE_1980_1995`, `AGE_1995_2005`, `AGE_2005_2015`, `AGE_OVER_2015`, `SIA_2024_EXISTING_MFH`, `SIA_2024_EXISTING_SFH`, `SIA_2024_EXISTING_HOTEL_ROOM`, `SIA_2024_EXISTING_LOBBY`, `SIA_2024_EXISTING_SINGLE_GROUP_OFFICE`, `SIA_2024_EXISTING_OPEN_PLAN_OFFICE`, `SIA_2024_EXISTING_MEETING_ROOM`, `SIA_2024_EXISTING_COUNTER_HALL`, `SIA_2024_EXISTING_CLASS_ROOM`, `SIA_2024_EXISTING_TEACHERS_LOUNGE`, `SIA_2024_EXISTING_LIBRARY`, `SIA_2024_EXISTING_AUDITORIUM`, `SIA_2024_EXISTING_SCHOOL_SUBJECT_ROOM`, `SIA_2024_EXISTING_FOOD_SALE_STORE`, `SIA_2024_EXISTING_SPECIALTY_STORE`, `SIA_2024_EXISTING_SALES_FURNITURE_DIY_GARDEN`, `SIA_2024_EXISTING_PATIENT_ROOM`, `SIA_2024_EXISTING_WARD_ROOM`, `SIA_2024_EXISTING_TREATMENT_ROOM`, `SIA_2024_EXISTING_WAREHOUSE`, `SIA_2024_EXISTING_GYMNASIUM`, `SIA_2024_EXISTING_FITNESS_ROOM`, `SIA_2024_EXISTING_INDOOR_SWIMMING_POOL`, `SIA_2024_STANDARD_MFH`, `SIA_2024_STANDARD_SFH`, `SIA_2024_STANDARD_HOTEL_ROOM`, `SIA_2024_STANDARD_LOBBY`, `SIA_2024_STANDARD_SINGLE_GROUP_OFFICE`, `SIA_2024_STANDARD_OPEN_PLAN_OFFICE`, `SIA_2024_STANDARD_MEETING_ROOM`, `SIA_2024_STANDARD_COUNTER_HALL`, `SIA_2024_STANDARD_CLASS_ROOM`, `SIA_2024_STANDARD_TEACHERS_LOUNGE`, `SIA_2024_STANDARD_LIBRARY`, `SIA_2024_STANDARD_AUDITORIUM`, `SIA_2024_STANDARD_SCHOOL_SUBJECT_ROOM`, `SIA_2024_STANDARD_FOOD_SALE_STORE`, `SIA_2024_STANDARD_SPECIALTY_STORE`, `SIA_2024_STANDARD_SALES_FURNITURE_DIY_GARDEN`, `SIA_2024_STANDARD_PATIENT_ROOM`, `SIA_2024_STANDARD_WARD_ROOM`, `SIA_2024_STANDARD_TREATMENT_ROOM`, `SIA_2024_STANDARD_WAREHOUSE`, `SIA_2024_STANDARD_GYMNASIUM`, `SIA_2024_STANDARD_FITNESS_ROOM`, `SIA_2024_STANDARD_INDOOR_SWIMMING_POOL`, `SIA_2024_TARGET_MFH`, `SIA_2024_TARGET_SFH`, `SIA_2024_TARGET_HOTEL_ROOM`, `SIA_2024_TARGET_LOBBY`, `SIA_2024_TARGET_SINGLE_GROUP_OFFICE`, `SIA_2024_TARGET_OPEN_PLAN_OFFICE`, `SIA_2024_TARGET_MEETING_ROOM`, `SIA_2024_TARGET_COUNTER_HALL`, `SIA_2024_TARGET_CLASS_ROOM`, `SIA_2024_TARGET_TEACHERS_LOUNGE`, `SIA_2024_TARGET_LIBRARY`, `SIA_2024_TARGET_AUDITORIUM`, `SIA_2024_TARGET_SCHOOL_SUBJECT_ROOM`, `SIA_2024_TARGET_FOOD_SALE_STORE`, `SIA_2024_TARGET_SPECIALTY_STORE`, `SIA_2024_TARGET_SALES_FURNITURE_DIY_GARDEN`, `SIA_2024_TARGET_PATIENT_ROOM`, `SIA_2024_TARGET_WARD_ROOM`, `SIA_2024_TARGET_TREATMENT_ROOM`, `SIA_2024_TARGET_WAREHOUSE`, `SIA_2024_TARGET_GYMNASIUM`, `SIA_2024_TARGET_FITNESS_ROOM`, `SIA_2024_TARGET_INDOOR_SWIMMING_POOL`, `MINERGIE_NEW_CONSTRUCTION`, `MINERGIE_RENOVATION`, `MINERGIE_A`, `MINERGIE_P_NEW_CONSTRUCTION`, `MINERGIE_P_RENOVATION`, `OTHERS`, `None`. |
| `energyDemandMetadataOption` | string, nullable | no | One of: `OPTION_1`, `OPTION_2`, `OPTION_3`, `None`. |
| `energyDemandMetadataReferencedAreaM2` | number, nullable | no |  |
| `energyDemandMetadataSpecificEnergyDemandValueKWhM2` | number, nullable | no |  |
| `energyDemandMetadataTotalAnnualDemand` | number, nullable | no |  |
| `multiplicationFactorPreview` | integer (int32), nullable | no |  |
| `multiplicationFactor` | integer (int32), nullable | no |  |
| `reverse` | boolean | yes |  |

**Example request**

```bash
curl -X PUT "https://eu-north-1-api.sympheny.com/sympheny-app/v2_2/scenarios/{scenarioGuid}/energy-demands/{demand-guid}" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "energyDemandGuid": "string",
  "energyCarrierName": "string",
  "hubs": [
    {
      "hubGuid": "string",
      "hubName": "string",
      "updated": "2026-01-01T00:00:00Z",
      "created": "2026-01-01T00:00:00Z"
    }
  ],
  "energyDemandName": "string",
  "energyCarrierGuid": "string",
  "demandSalePrice": 0.0,
  "stages": [
    "00000000-0000-0000-0000-000000000000"
  ],
  "demandProfileId": 0,
  "demandScalingFactor": 0.0,
  "demandSalePriceProfileId": 0,
  "demandSalePriceScalingFactor": 0.0,
  "energyDemandUserSavedMetadataGuid": "string",
  "energyDemandUserSavedMetadataName": "string",
  "energyDemandUserSavedMetadataReferenceArea": 0.0,
  "scalingFactor": 0.0,
  "energyDemandMetadataGuid": "string",
  "energyDemandMetadataName": "string",
  "energyDemandMetadataDbOrganization": "string",
  "energyDemandMetadataType": "ELECTRICITY",
  "energyDemandMetadataBuildingType": "RESIDENCE_MFH",
  "energyDemandMetadataBuildingAge": "AGE_UNDER_1970",
  "energyDemandMetadataOption": "OPTION_1",
  "energyDemandMetadataReferencedAreaM2": 0.0,
  "energyDemandMetadataSpecificEnergyDemandValueKWhM2": 0.0,
  "energyDemandMetadataTotalAnnualDemand": 0.0,
  "multiplicationFactorPreview": 0,
  "multiplicationFactor": 0,
  "reverse": true
}'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoEnergyDemandResponseDtoV2` |

**Example response** (200)

```json
{
  "data": {
    "energyDemandGuid": "string",
    "energyCarrierName": "string",
    "hubs": [
      {
        "hubGuid": "string",
        "hubName": "string",
        "updated": "2026-01-01T00:00:00Z",
        "created": "2026-01-01T00:00:00Z"
      }
    ],
    "energyDemandName": "string",
    "energyCarrierGuid": "string",
    "demandSalePrice": 0.0,
    "stages": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "demandProfileId": 0,
    "demandScalingFactor": 0.0,
    "demandSalePriceProfileId": 0,
    "demandSalePriceScalingFactor": 0.0,
    "energyDemandUserSavedMetadataGuid": "string",
    "energyDemandUserSavedMetadataName": "string",
    "energyDemandUserSavedMetadataReferenceArea": 0.0,
    "scalingFactor": 0.0,
    "energyDemandMetadataGuid": "string",
    "energyDemandMetadataName": "string",
    "energyDemandMetadataDbOrganization": "string",
    "energyDemandMetadataType": "ELECTRICITY",
    "energyDemandMetadataBuildingType": "RESIDENCE_MFH",
    "energyDemandMetadataBuildingAge": "AGE_UNDER_1970",
    "energyDemandMetadataOption": "OPTION_1",
    "energyDemandMetadataReferencedAreaM2": 0.0,
    "energyDemandMetadataSpecificEnergyDemandValueKWhM2": 0.0,
    "energyDemandMetadataTotalAnnualDemand": 0.0,
    "multiplicationFactorPreview": 0,
    "multiplicationFactor": 0,
    "reverse": true
  },
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
