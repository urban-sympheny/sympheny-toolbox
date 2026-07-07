<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/models.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Shared models

Models used across several resource groups.

## CustomSeasonalityResponseDto { #model-CustomSeasonalityResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `month` | [`Month`](#model-Month), optional | no |  |
| `value` | `float`, optional | no |  |

## Demand { #model-Demand }

| Member | Value |
| --- | --- |
| `Demand.hot_water` | `'HOT_WATER'` |
| `Demand.space_heating` | `'SPACE_HEATING'` |
| `Demand.electricity` | `'ELECTRICITY'` |
| `Demand.cooling` | `'COOLING'` |

## EnergyCarrierResponseDto { #model-EnergyCarrierResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_carrier_guid` | `str` | yes |  |
| `type_key` | `str` | yes |  |
| `type_display_name` | `str` | yes |  |
| `subtype_key` | `str` | yes |  |
| `subtype_display_name` | `str` | yes |  |
| `energy_carrier_name` | `str` | yes |  |
| `color_hex_code` | `str` | yes |  |
| `fixed_input_share` | `float`, optional | no |  |
| `output_efficiency` | `float`, optional | no |  |
| `custom_output_efficiency_activated` | `bool` | yes |  |
| `custom_input_efficiency_activated` | `bool` | yes |  |
| `custom_seasonality_values` | list of [`CustomSeasonalityResponseDto`](#model-CustomSeasonalityResponseDto), optional | no |  |
| `output_efficiency_profile_id` | `int`, optional | no |  |
| `created` | `AwareDatetime` | yes |  |
| `primary` | `bool`, optional | no |  |

## Export { #model-Export }

| Member | Value |
| --- | --- |
| `Export.heat_ambient` | `'HEAT_AMBIENT'` |
| `Export.cooling` | `'COOLING'` |

## HubResponseDto { #model-HubResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guid` | `str` | yes |  |
| `hub_name` | `str` | yes |  |
| `updated` | `AwareDatetime` | yes |  |
| `created` | `AwareDatetime` | yes |  |

## Import { #model-Import }

| Member | Value |
| --- | --- |
| `Import.electricity` | `'ELECTRICITY'` |

## Month { #model-Month }

| Member | Value |
| --- | --- |
| `Month.january` | `'JANUARY'` |
| `Month.february` | `'FEBRUARY'` |
| `Month.march` | `'MARCH'` |
| `Month.april` | `'APRIL'` |
| `Month.may` | `'MAY'` |
| `Month.june` | `'JUNE'` |
| `Month.july` | `'JULY'` |
| `Month.august` | `'AUGUST'` |
| `Month.september` | `'SEPTEMBER'` |
| `Month.october` | `'OCTOBER'` |
| `Month.november` | `'NOVEMBER'` |
| `Month.december` | `'DECEMBER'` |
| `Month.none_type_none` | `None` |

## ScenarioEnymapResponseDto { #model-ScenarioEnymapResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `length` | `int`, optional | no |  |
| `interest_rate` | `float`, optional | no |  |
| `exchange_currency` | `str`, optional | no |  |
| `exchange_rate` | `float`, optional | no |  |
| `scope` | [`Scope`](#model-Scope), optional | no |  |
| `technologies` | list of [`Technology`](#model-Technology), optional | no |  |
| `demands` | list of [`Demand`](#model-Demand), optional | no |  |
| `imports` | list of [`Import`](#model-Import), optional | no |  |
| `exports` | list of [`Export`](#model-Export), optional | no |  |
| `multi_hubs` | `bool`, optional | no |  |

## ScenarioResponseDto { #model-ScenarioResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str`, optional | no |  |
| `scenario_name` | `str`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `ready_for_execution` | `bool`, optional | no |  |
| `preparing_execution_v2` | `bool`, optional | no |  |
| `master_scenario_guid` | `str`, optional | no |  |
| `project_guid` | `str`, optional | no |  |
| `project_name` | `str`, optional | no |  |
| `analysis_guid` | `str`, optional | no |  |
| `analysis_name` | `str`, optional | no |  |
| `enymap` | [`ScenarioEnymapResponseDto`](#model-ScenarioEnymapResponseDto), optional | no |  |
| `variant` | `bool`, optional | no |  |

## Scope { #model-Scope }

| Member | Value |
| --- | --- |
| `Scope.building_developments` | `'BUILDING_DEVELOPMENTS'` |
| `Scope.regional_national` | `'REGIONAL_NATIONAL'` |
| `Scope.industrial_parks` | `'INDUSTRIAL_PARKS'` |
| `Scope.none_type_none` | `None` |

## Status { #model-Status }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `str`, optional | no |  |
| `desc` | `str`, optional | no |  |
| `message` | `str`, optional | no |  |

## Technology { #model-Technology }

| Member | Value |
| --- | --- |
| `Technology.pv` | `'PV'` |
| `Technology.heat_pump` | `'HEAT_PUMP'` |
| `Technology.gas_boiler` | `'GAS_BOILER'` |
| `Technology.hot_water_storage` | `'HOT_WATER_STORAGE'` |
| `Technology.chiller` | `'CHILLER'` |
| `Technology.battery` | `'BATTERY'` |
