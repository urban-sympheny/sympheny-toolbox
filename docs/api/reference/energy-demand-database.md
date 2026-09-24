<!-- GENERATED — do not edit by hand. Source: specs/sympheny_openapi.json.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-api-reference. -->

# Energy demand database

## Get database energy profile { #operation-getDatabaseEnergyProfile }

```
POST /sympheny-app/database-energy-demand-profile/{demandType}/calculate
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_demand_database.calculate()`](../../sdk/reference/energy_demand_database.md#method-energy_demand_database-calculate).

areaM2 or annualKwh must be not null

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `demandType` | path | string | yes | One of: `ELECTRICITY`, `SPACE_HEATING`, `HOT_WATER`, `COOLING`. |

**Request body** (array of `EnergyDemandDBRequest`)

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `buildingType` | string | yes | One of: `RESIDENCE_MFH`, `RESIDENCE_SFH`, `ADMINISTRATION`, `OFFICES`, `SCHOOLS`, `RETAIL`, `RESTAURANT`, `ASSEMBLY`, `HOSPITALS`, `INDUSTRY`, `WAREHOUSE`, `SPORTS_CENTER`, `INDOOR_POOL`, `HOTEL`, `INDUSTRY_1_SHIFT_FABRICATED_METALS`, `INDUSTRY_2_SHIFT_FABRICATED_METALS`, `INDUSTRY_FOOD_PROCESSING`, `INDUSTRY_GENERAL_MANUFACTURER`, `INDUSTRY_PHARMACEUTICAL`, `INDUSTRY_PLASTIC_MANUFACTURER`, `INDUSTRY_SERVICES`, `INDUSTRY_WAREHOUSE`. |
| `year` | integer (int32) | yes |  |
| `areaM2` | number (double), nullable | no |  |
| `annualKwh` | number (double), nullable | no |  |

**Example request**

```bash
curl -X POST "https://eu-north-1-api.sympheny.com/sympheny-app/database-energy-demand-profile/{demandType}/calculate" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "buildingType": "RESIDENCE_MFH",
    "year": 0,
    "areaM2": 0.0,
    "annualKwh": 0.0
  }
]'
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListBigDecimal` |

**Example response** (200)

```json
{
  "data": [
    0.0
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```

## Get database energy demand table { #operation-getDatabaseEnergyDemandTable }

```
GET /sympheny-app/database-energy-demand-table
```

Requires a [Bearer token](../authentication.md). SDK method: [`client.energy_demand_database.list()`](../../sdk/reference/energy_demand_database.md#method-energy_demand_database-list).

**Example request**

```bash
curl -X GET "https://eu-north-1-api.sympheny.com/sympheny-app/database-energy-demand-table" \
  -H "Authorization: Bearer $SYMPHENY_TOKEN"
```

**Responses**

| Status | Description | Schema |
| --- | --- | --- |
| 200 | OK | `ResponseDtoListEnergyDemandDBResponse` |

**Example response** (200)

```json
{
  "data": [
    {
      "demandType": "ELECTRICITY",
      "buildingType": "RESIDENCE_MFH",
      "yearFrom": 0,
      "yearTo": 0,
      "kwhPerM2a": 0.0
    }
  ],
  "status": {
    "code": "string",
    "desc": "string",
    "message": "string"
  }
}
```
