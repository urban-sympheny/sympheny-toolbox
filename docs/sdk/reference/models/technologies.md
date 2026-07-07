<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/models.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Technology and network models

## AdvancedCostComponentRequestDto { #model-AdvancedCostComponentRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `value` | `float`, optional | no |  |
| `category` | `str`, optional | no |  |
| `lifetime` | `float`, optional | no | (≥ 0.0) |
| `interest_rate` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `length` | `float`, optional | no |  |
| `complexity_factor` | `float`, optional | no |  |
| `data_points` | `float`, optional | no |  |
| `number_of_pumps` | `float`, optional | no |  |

## AdvancedCostComponentResponseDto { #model-AdvancedCostComponentResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `value` | `float`, optional | no |  |
| `category` | `str`, optional | no |  |
| `lifetime` | `float`, optional | no | (≥ 0.0) |
| `interest_rate` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `length` | `float`, optional | no |  |
| `complexity_factor` | `float`, optional | no |  |
| `data_points` | `float`, optional | no |  |
| `number_of_pumps` | `float`, optional | no |  |
| `guid` | `str`, optional | no |  |
| `category_id` | `str`, optional | no |  |

## ConversionCarrierRequestDtoV2 { #model-ConversionCarrierRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_carrier_guid` | `str` | yes |  |
| `fixed_input_share` | `float` | yes | (≥ 0.0) |
| `output_efficiency` | `float` | yes | (≥ 0.0) |
| `custom_input_share_activated` | `bool`, optional | no |  |
| `custom_output_efficiency_activated` | `bool`, optional | no |  |
| `input_share_profile_id` | `int`, optional | no |  |
| `output_efficiency_profile_id` | `int`, optional | no |  |
| `custom_seasonality_values` | list of [`CustomSeasonalityRequestDto`](#model-CustomSeasonalityRequestDto), optional | no |  |
| `type` | [`Type`](#model-Type) | yes |  |
| `primary` | `bool` | yes |  |

## ConversionTechnologyDetailResponseDtoV2 { #model-ConversionTechnologyDetailResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixed_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_om_cost_chf` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost_percent` | `float`, optional | no |  |
| `variable_om_cost_year` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_emitted_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_captured_co2` | `float`, optional | no | (≥ 0.0) |
| `fixed_replacement_cost` | `float`, optional | no | (≥ 0.0) |
| `variable_replacement_cost_percent` | `float`, optional | no | (≥ 0.0) |
| `variable_replacement_cost_chf` | `float`, optional | no | (≥ 0.0) |
| `fixed_salvage_value` | `float`, optional | no | (≥ 0.0) |
| `variable_salvage_value_percent` | `float`, optional | no | (≥ 0.0) |
| `variable_salvage_value_chf` | `float`, optional | no | (≥ 0.0) |
| `must_be_installed_in_hubs` | [`MustBeInstalledInHubs2`](#model-MustBeInstalledInHubs2) | yes |  |
| `conversion_technology_guid` | `str`, optional | no |  |
| `process_name` | `str` | yes |  |
| `exchange_currency` | `str`, optional | no |  |
| `exchange_rate` | `float`, optional | no |  |
| `variable_investment_cost` | `float`, optional | no |  |
| `lifetime` | `float` | yes |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto) | yes |  |
| `technology_modes` | list of [`TechnologyModeResponseDtoV2`](#model-TechnologyModeResponseDtoV2), optional | no |  |
| `category` | `str`, optional | no |  |
| `technology_category` | `str`, optional | no |  |
| `mutually_exclusive_group` | `str`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `virtual` | `bool` | yes |  |
| `technology_optional` | `bool`, optional | no |  |
| `part_of_technology_package` | `bool`, optional | no |  |
| `technology_capacity` | `str`, optional | no |  |
| `cost_components` | list of [`AdvancedCostComponentResponseDto`](#model-AdvancedCostComponentResponseDto), optional | no |  |
| `comes_from_db` | `str`, optional | no |  |
| `stages` | list of `UUID` | yes |  |

## ConversionTechnologyListResponseDtoV2 { #model-ConversionTechnologyListResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `conversion_technologies` | list of [`ConversionTechnologyResponseDtoV2`](#model-ConversionTechnologyResponseDtoV2), optional | no |  |

## ConversionTechnologyRequestDtoV2 { #model-ConversionTechnologyRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixed_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_om_cost_chf` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost_percent` | `float`, optional | no |  |
| `variable_om_cost_year` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_emitted_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_captured_co2` | `float`, optional | no | (≥ 0.0) |
| `fixed_replacement_cost` | `float`, optional | no | (≥ 0.0) |
| `variable_replacement_cost_percent` | `float`, optional | no | (≥ 0.0) |
| `variable_replacement_cost_chf` | `float`, optional | no | (≥ 0.0) |
| `fixed_salvage_value` | `float`, optional | no | (≥ 0.0) |
| `variable_salvage_value_percent` | `float`, optional | no | (≥ 0.0) |
| `variable_salvage_value_chf` | `float`, optional | no | (≥ 0.0) |
| `must_be_installed_in_hubs` | [`MustBeInstalledInHubs`](#model-MustBeInstalledInHubs) | yes |  |
| `process_name` | `str` | yes | (max length 100, min length 0) |
| `variable_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `lifetime` | `int` | yes |  |
| `hub_guids` | list of `str` | yes |  |
| `conversion_technology_modes` | list of [`TechnologyModeRequestDtoV2`](#model-TechnologyModeRequestDtoV2) | yes | (max length 3, min length 1) |
| `virtual` | `bool` | yes |  |
| `cost_components` | list of [`AdvancedCostComponentRequestDto`](#model-AdvancedCostComponentRequestDto), optional | no |  |
| `suggested` | `bool`, optional | no |  |
| `technology_category` | `str`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `comes_from_db` | `str`, optional | no |  |
| `exchange_currency` | `str` | yes | (max length 3, min length 0) |
| `exchange_rate` | `float` | yes | (≥ 0.0) |
| `stages` | list of `UUID` | yes |  |

## ConversionTechnologyResponseDtoV2 { #model-ConversionTechnologyResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `conversion_technology_guid` | `str`, optional | no |  |
| `process_name` | `str`, optional | no |  |
| `lifetime` | `int`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `conversion_technology_modes` | list of [`TechnologyModeResponseDtoV2`](#model-TechnologyModeResponseDtoV2), optional | no |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto), optional | no |  |
| `virtual` | `bool`, optional | no |  |
| `must_be_installed_in_hubs` | [`MustBeInstalledInHubs1`](#model-MustBeInstalledInHubs1), optional | no |  |
| `stages` | list of `UUID`, optional | no |  |

## CustomSeasonalityRequestDto { #model-CustomSeasonalityRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `month` | [`Month`](common.md#model-Month), optional | no |  |
| `value` | `float`, optional | no |  |

## EnergyCarrierResponseDtoV2 { #model-EnergyCarrierResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_carrier_guid` | `str`, optional | no |  |
| `type_key` | `str`, optional | no |  |
| `type_display_name` | `str`, optional | no |  |
| `subtype_key` | `str`, optional | no |  |
| `subtype_display_name` | `str`, optional | no |  |
| `energy_carrier_name` | `str`, optional | no |  |
| `color_hex_code` | `str`, optional | no |  |
| `output_efficiency` | `float`, optional | no |  |
| `fixed_input_share` | `float`, optional | no |  |
| `custom_output_efficiency_activated` | `bool`, optional | no |  |
| `custom_input_share_activated` | `bool`, optional | no |  |
| `custom_seasonality_values` | list of [`CustomSeasonalityResponseDto`](common.md#model-CustomSeasonalityResponseDto), optional | no |  |
| `input_share_profile_id` | `int`, optional | no |  |
| `output_efficiency_profile_id` | `int`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `primary` | `bool`, optional | no |  |

## GuidNameDto { #model-GuidNameDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `guid` | `str` | yes |  |
| `name` | `str` | yes |  |

## IntraHubNetworkLinkListResponseDto { #model-IntraHubNetworkLinkListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `intra_hub_network_links` | list of [`IntraHubNetworkLinkResponseDto`](#model-IntraHubNetworkLinkResponseDto), optional | no |  |

## IntraHubNetworkLinkRequestDto { #model-IntraHubNetworkLinkRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `network_loss` | `float`, optional | no |  |
| `fixed_embodied_co2` | `float`, optional | no |  |
| `input_energy_carrier_guid` | `str` | yes |  |
| `output_energy_carrier_guid` | `str` | yes |  |
| `hub_guids` | list of `str` | yes |  |
| `advanced_cost_components` | list of [`AdvancedCostComponentRequestDto`](#model-AdvancedCostComponentRequestDto), optional | no |  |
| `stages` | list of `UUID` | yes |  |

## IntraHubNetworkLinkResponseDto { #model-IntraHubNetworkLinkResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `intra_hub_network_link_guid` | `str`, optional | no |  |
| `name` | `str` | yes |  |
| `network_loss` | `float`, optional | no |  |
| `fixed_embodied_co2` | `float`, optional | no |  |
| `input_energy_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto) | yes |  |
| `output_energy_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto) | yes |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto) | yes |  |
| `advanced_cost_components` | list of [`AdvancedCostComponentResponseDto`](#model-AdvancedCostComponentResponseDto) | yes |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `stages` | list of `UUID` | yes |  |

## LocalTime { #model-LocalTime }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hour` | `int`, optional | no |  |
| `minute` | `int`, optional | no |  |
| `second` | `int`, optional | no |  |
| `nano` | `int`, optional | no |  |

## MustBeInstalled { #model-MustBeInstalled }

| Member | Value |
| --- | --- |
| `MustBeInstalled.can_be_installed` | `'canBeInstalled'` |
| `MustBeInstalled.must_be_installed` | `'mustBeInstalled'` |
| `MustBeInstalled.must_be_installed_in_at_least_one_hub` | `'mustBeInstalledInAtLeastOneHub'` |

## MustBeInstalledInHubs { #model-MustBeInstalledInHubs }

| Member | Value |
| --- | --- |
| `MustBeInstalledInHubs.can_be_installed` | `'canBeInstalled'` |
| `MustBeInstalledInHubs.must_be_installed` | `'mustBeInstalled'` |
| `MustBeInstalledInHubs.must_be_installed_in_at_least_one_hub` | `'mustBeInstalledInAtLeastOneHub'` |

## MustBeInstalledInHubs1 { #model-MustBeInstalledInHubs1 }

| Member | Value |
| --- | --- |
| `MustBeInstalledInHubs1.can_be_installed` | `'canBeInstalled'` |
| `MustBeInstalledInHubs1.must_be_installed` | `'mustBeInstalled'` |
| `MustBeInstalledInHubs1.must_be_installed_in_at_least_one_hub` | `'mustBeInstalledInAtLeastOneHub'` |
| `MustBeInstalledInHubs1.none_type_none` | `None` |

## MustBeInstalledInHubs2 { #model-MustBeInstalledInHubs2 }

| Member | Value |
| --- | --- |
| `MustBeInstalledInHubs2.can_be_installed` | `'canBeInstalled'` |
| `MustBeInstalledInHubs2.must_be_installed` | `'mustBeInstalled'` |
| `MustBeInstalledInHubs2.must_be_installed_in_at_least_one_hub` | `'mustBeInstalledInAtLeastOneHub'` |

## NetworkLinkListResponseDto { #model-NetworkLinkListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `network_links` | list of [`NetworkLinkResponseDto`](#model-NetworkLinkResponseDto), optional | no |  |

## NetworkLinkRequestDtoV2 { #model-NetworkLinkRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `installed_capacity` | `float`, optional | no | (≥ 0.0) |
| `maximum_capacity` | `float`, optional | no | (≥ 0.0) |
| `name` | `str` | yes |  |
| `length` | `float` | yes | (≥ 0.0) |
| `technology_capacity` | [`TechnologyCapacity`](#model-TechnologyCapacity) | yes |  |
| `uni_directional_flow` | `bool` | yes |  |
| `must_be_installed` | `bool` | yes |  |
| `node1_guid` | `str` | yes |  |
| `node2_guid` | `str` | yes |  |
| `network_technology_guid` | `str` | yes |  |
| `cost_components` | list of [`AdvancedCostComponentRequestDto`](#model-AdvancedCostComponentRequestDto), optional | no |  |
| `minimum_capacity` | `float`, optional | no | (≥ 0.0) |
| `network_loss` | `float` | yes | (≥ 0.0) |
| `network_loss_profile_id` | `int`, optional | no |  |

## NetworkLinkResponseDto { #model-NetworkLinkResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `network_link_guid` | `str`, optional | no |  |
| `length` | `float`, optional | no |  |
| `technology_capacity` | [`TechnologyCapacity2`](#model-TechnologyCapacity2), optional | no |  |
| `installed_capacity` | `float`, optional | no |  |
| `uni_directional_flow` | `bool`, optional | no |  |
| `must_be_installed` | `bool`, optional | no |  |
| `node1_guid` | `str`, optional | no |  |
| `node1_name` | `str`, optional | no |  |
| `node2_guid` | `str`, optional | no |  |
| `node2_name` | `str`, optional | no |  |
| `network_technology_name` | `str`, optional | no |  |
| `network_technology_guid` | `str`, optional | no |  |
| `cost_components` | list of [`AdvancedCostComponentResponseDto`](#model-AdvancedCostComponentResponseDto), optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |

## NetworkLinkResponseDtoV2 { #model-NetworkLinkResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `installed_capacity` | `float`, optional | no | (≥ 0.0) |
| `maximum_capacity` | `float`, optional | no | (≥ 0.0) |
| `network_link_guid` | `str`, optional | no |  |
| `name` | `str` | yes |  |
| `length` | `float` | yes |  |
| `technology_capacity` | [`TechnologyCapacity`](#model-TechnologyCapacity) | yes |  |
| `uni_directional_flow` | `bool` | yes |  |
| `must_be_installed` | `bool` | yes |  |
| `node1_guid` | `str` | yes |  |
| `node1_name` | `str` | yes |  |
| `node2_guid` | `str` | yes |  |
| `node2_name` | `str` | yes |  |
| `network_technology_name` | `str` | yes |  |
| `network_technology_guid` | `str` | yes |  |
| `cost_components` | list of [`AdvancedCostComponentResponseDto`](#model-AdvancedCostComponentResponseDto) | yes |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `minimum_capacity` | `float`, optional | no |  |
| `network_loss` | `float` | yes |  |
| `network_loss_profile_id` | `int`, optional | no |  |

## NetworkTechnologyListResponseDto { #model-NetworkTechnologyListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `network_technologies` | list of [`NetworkTechnologyResponseDto`](#model-NetworkTechnologyResponseDto), optional | no |  |

## NetworkTechnologyListResponseDtoV2 { #model-NetworkTechnologyListResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `network_technologies` | list of [`NetworkTechnologyResponseDtoV2`](#model-NetworkTechnologyResponseDtoV2), optional | no |  |

## NetworkTechnologyRequestDtoV2 { #model-NetworkTechnologyRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixed_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `variable_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_om_cost_chf` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost_percent` | `float`, optional | no |  |
| `variable_om_cost_year` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost_ch_fk_wh` | `float`, optional | no | (≥ 0.0) |
| `fixed_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `fixed_replacement_cost` | `float`, optional | no |  |
| `variable_replacement_cost_percent` | `float`, optional | no |  |
| `variable_replacement_cost_chf` | `float`, optional | no |  |
| `fixed_salvage_value` | `float`, optional | no |  |
| `variable_salvage_value_percent` | `float`, optional | no |  |
| `variable_salvage_value_chf` | `float`, optional | no |  |
| `network_technology_name` | `str` | yes | (max length 100, min length 0) |
| `lifetime` | `int` | yes |  |
| `energy_carrier_guid` | `str` | yes |  |
| `cost_components` | list of [`AdvancedCostComponentRequestDto`](#model-AdvancedCostComponentRequestDto), optional | no |  |
| `suggested` | `bool`, optional | no |  |
| `technology_category` | `str`, optional | no |  |
| `network_size` | `str`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `comes_from_db` | `str`, optional | no |  |
| `exchange_currency` | `str`, optional | no | (max length 3, min length 0) |
| `exchange_rate` | `float`, optional | no | (≥ 0.0) |
| `stages` | list of `UUID` | yes |  |

## NetworkTechnologyResponseDto { #model-NetworkTechnologyResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `network_technology_guid` | `str`, optional | no |  |
| `network_technology_name` | `str`, optional | no |  |
| `network_loss` | `float`, optional | no |  |
| `fixed_investment_cost` | `float`, optional | no |  |
| `variable_investment_cost` | `float`, optional | no |  |
| `variable_om_cost_year` | `float`, optional | no |  |
| `fixed_om_cost_chf` | `float`, optional | no |  |
| `fixed_om_cost_percent` | `float`, optional | no |  |
| `lifetime` | `float`, optional | no |  |
| `maximum_capacity` | `float`, optional | no |  |
| `minimum_capacity` | `float`, optional | no |  |
| `variable_embodied_co2` | `float`, optional | no |  |
| `fixed_embodied_co2` | `float`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `energy_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto), optional | no |  |
| `category` | `str`, optional | no |  |
| `technology_category` | `str`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `network_size` | `str`, optional | no |  |
| `comes_from_db` | `str`, optional | no |  |
| `cost_components` | list of [`AdvancedCostComponentResponseDto`](#model-AdvancedCostComponentResponseDto), optional | no |  |

## NetworkTechnologyResponseDtoV2 { #model-NetworkTechnologyResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fixed_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `variable_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_om_cost_chf` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost_percent` | `float`, optional | no |  |
| `variable_om_cost_year` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost_ch_fk_wh` | `float`, optional | no | (≥ 0.0) |
| `fixed_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `fixed_replacement_cost` | `float`, optional | no |  |
| `variable_replacement_cost_percent` | `float` | yes |  |
| `variable_replacement_cost_chf` | `float`, optional | no |  |
| `fixed_salvage_value` | `float`, optional | no |  |
| `variable_salvage_value_percent` | `float` | yes |  |
| `variable_salvage_value_chf` | `float`, optional | no |  |
| `network_technology_guid` | `str`, optional | no |  |
| `network_technology_name` | `str` | yes |  |
| `exchange_currency` | `str` | yes |  |
| `exchange_rate` | `float` | yes |  |
| `lifetime` | `int` | yes |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `energy_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto) | yes |  |
| `category` | `str` | yes |  |
| `technology_category` | `str`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `network_size` | `str`, optional | no |  |
| `comes_from_db` | `str`, optional | no |  |
| `cost_components` | list of [`AdvancedCostComponentResponseDto`](#model-AdvancedCostComponentResponseDto) | yes |  |
| `stages` | list of `UUID` | yes |  |

## SeasonalOperation { #model-SeasonalOperation }

| Member | Value |
| --- | --- |
| `SeasonalOperation.all_seasons` | `'ALL_SEASONS'` |
| `SeasonalOperation.winter` | `'WINTER'` |
| `SeasonalOperation.non_winter` | `'NON_WINTER'` |
| `SeasonalOperation.summer` | `'SUMMER'` |
| `SeasonalOperation.non_summer` | `'NON_SUMMER'` |

## StorageTechnologyDetailResponseDtoV2 { #model-StorageTechnologyDetailResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `variable_om_cost_percent` | `float`, optional | no |  |
| `variable_om_energy_flow_cost` | `float`, optional | no | (≥ 0.0) |
| `capacity` | `float`, optional | no | (≥ 0.0) |
| `maximum_capacity` | `float`, optional | no | (≥ 0.0) |
| `minimum_capacity` | `float`, optional | no | (≥ 0.0) |
| `fixed_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost` | `float`, optional | no | (≥ 0.0) |
| `maximum_charging_rate` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `maximum_discharging_rate` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `variable_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `fixed_replacement_cost` | `float`, optional | no |  |
| `variable_replacement_cost_percent` | `float` | yes |  |
| `variable_replacement_cost_chf` | `float`, optional | no |  |
| `fixed_salvage_value` | `float`, optional | no |  |
| `variable_salvage_value_percent` | `float` | yes |  |
| `variable_salvage_value_chf` | `float`, optional | no |  |
| `must_be_installed` | `str` | yes |  |
| `storage_technology_guid` | `str`, optional | no |  |
| `storage_name` | `str` | yes |  |
| `exchange_currency` | `str` | yes |  |
| `exchange_rate` | `float` | yes |  |
| `variable_investment_cost` | `float`, optional | no |  |
| `fixed_om_cost_chf` | `float`, optional | no |  |
| `lifetime` | `int` | yes |  |
| `standby_loss` | `float`, optional | no |  |
| `stand_by_loss_profile_id` | `int`, optional | no |  |
| `minimum_soc` | `float`, optional | no |  |
| `storage_charging_efficiency` | `float` | yes |  |
| `storage_discharging_efficiency` | `float` | yes |  |
| `technology_capacity` | `str` | yes |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `storage_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto) | yes |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto) | yes |  |
| `category` | `str` | yes |  |
| `technology_category` | `str`, optional | no |  |
| `mutually_exclusive_group` | `str`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `technology_optional` | `bool`, optional | no |  |
| `cost_components` | list of [`AdvancedCostComponentResponseDto`](#model-AdvancedCostComponentResponseDto) | yes |  |
| `comes_from_db` | `str`, optional | no |  |
| `stages` | list of `UUID` | yes |  |
| `ev_plug_in_time` | [`LocalTime`](#model-LocalTime), optional | no |  |
| `ev_plug_out_time` | [`LocalTime`](#model-LocalTime), optional | no |  |
| `ev_plug_in_duration_hours` | `float`, optional | no |  |
| `driving_distance_kms` | `float`, optional | no |  |
| `ev_soc_start_percent` | `float`, optional | no |  |
| `ev_battery_size_k_wh` | `float`, optional | no |  |
| `maximum_soc_percent` | `float`, optional | no |  |
| `ev_average_k_wh_per_km` | `float`, optional | no |  |
| `ev_plug_in_power_kw` | `float`, optional | no |  |
| `is_ev_battery` | `bool`, optional | no |  |
| `type_of_charging` | [`TypeOfCharging`](#model-TypeOfCharging), optional | no |  |

## StorageTechnologyListResponseDto { #model-StorageTechnologyListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `storage_technologies` | list of [`StorageTechnologyResponseDto`](#model-StorageTechnologyResponseDto), optional | no |  |

## StorageTechnologyListResponseDtoV2 { #model-StorageTechnologyListResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `storage_technologies` | list of [`StorageTechnologyResponseDtoV2`](#model-StorageTechnologyResponseDtoV2), optional | no |  |

## StorageTechnologyRequestDtoV2 { #model-StorageTechnologyRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `variable_om_cost_percent` | `float`, optional | no |  |
| `variable_om_energy_flow_cost` | `float`, optional | no | (≥ 0.0) |
| `capacity` | `float`, optional | no | (≥ 0.0) |
| `maximum_capacity` | `float`, optional | no | (≥ 0.0) |
| `minimum_capacity` | `float`, optional | no | (≥ 0.0) |
| `fixed_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `variable_om_cost` | `float`, optional | no | (≥ 0.0) |
| `maximum_charging_rate` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `maximum_discharging_rate` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `variable_embodied_co2` | `float`, optional | no | (≥ 0.0) |
| `fixed_replacement_cost` | `float`, optional | no |  |
| `variable_replacement_cost_percent` | `float`, optional | no |  |
| `variable_replacement_cost_chf` | `float`, optional | no |  |
| `fixed_salvage_value` | `float`, optional | no |  |
| `variable_salvage_value_percent` | `float`, optional | no |  |
| `variable_salvage_value_chf` | `float`, optional | no |  |
| `must_be_installed` | `str` | yes |  |
| `storage_name` | `str` | yes | (max length 100, min length 0) |
| `variable_investment_cost` | `float`, optional | no | (≥ 0.0) |
| `fixed_om_cost_chf` | `float`, optional | no | (≥ 0.0) |
| `lifetime` | `int` | yes |  |
| `standby_loss` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `stand_by_loss_profile_id` | `int`, optional | no |  |
| `minimum_soc` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `hub_guids` | list of `str` | yes |  |
| `energy_carrier_guid` | `str` | yes |  |
| `storage_charging_efficiency` | `float` | yes | (≥ 0.0, ≤ 100.0) |
| `storage_discharging_efficiency` | `float` | yes | (≥ 0.0, ≤ 100.0) |
| `technology_capacity` | `str` | yes |  |
| `cost_components` | list of [`AdvancedCostComponentRequestDto`](#model-AdvancedCostComponentRequestDto), optional | no |  |
| `suggested` | `bool`, optional | no |  |
| `technology_category` | `str`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `comes_from_db` | `str`, optional | no |  |
| `exchange_currency` | `str`, optional | no | (max length 3, min length 0) |
| `exchange_rate` | `float`, optional | no | (≥ 0.0) |
| `stages` | list of `UUID` | yes |  |
| `ev_plug_in_time` | [`LocalTime`](#model-LocalTime), optional | no |  |
| `ev_plug_out_time` | [`LocalTime`](#model-LocalTime), optional | no |  |
| `ev_plug_in_duration_hours` | `float`, optional | no |  |
| `driving_distance_kms` | `float`, optional | no |  |
| `ev_soc_start_percent` | `float`, optional | no |  |
| `ev_battery_size_k_wh` | `float`, optional | no |  |
| `maximum_soc_percent` | `float`, optional | no |  |
| `ev_average_k_wh_per_km` | `float`, optional | no |  |
| `ev_plug_in_power_kw` | `float`, optional | no |  |
| `is_ev_battery` | `bool`, optional | no |  |
| `type_of_charging` | [`TypeOfCharging`](#model-TypeOfCharging), optional | no |  |

## StorageTechnologyResponseDto { #model-StorageTechnologyResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `storage_technology_guid` | `str`, optional | no |  |
| `storage_name` | `str`, optional | no |  |
| `lifetime` | `float`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `energy_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto), optional | no |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto), optional | no |  |

## StorageTechnologyResponseDtoV2 { #model-StorageTechnologyResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `storage_technology_guid` | `str`, optional | no |  |
| `storage_name` | `str`, optional | no |  |
| `lifetime` | `int`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `energy_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto), optional | no |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto), optional | no |  |
| `stages` | list of `UUID`, optional | no |  |
| `stand_by_loss_profile_id` | `int`, optional | no |  |

## TechnologyCapacity { #model-TechnologyCapacity }

| Member | Value |
| --- | --- |
| `TechnologyCapacity.optimize` | `'optimize'` |
| `TechnologyCapacity.specify` | `'specify'` |

## TechnologyCapacity2 { #model-TechnologyCapacity2 }

| Member | Value |
| --- | --- |
| `TechnologyCapacity2.optimize` | `'optimize'` |
| `TechnologyCapacity2.specify` | `'specify'` |
| `TechnologyCapacity2.none_type_none` | `None` |

## TechnologyModeRequestDtoV2 { #model-TechnologyModeRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `capacity` | `float`, optional | no | (≥ 0.0) |
| `minimum_annual_output` | `float`, optional | no | (≥ 0.0) |
| `maximum_annual_output` | `float`, optional | no | (≥ 0.0) |
| `curtailment_limitation` | `float`, optional | no | (≥ 0.0) |
| `peak_power` | `float`, optional | no |  |
| `min_part_load` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `minimum_up_time` | `int`, optional | no | (≥ 1, ≤ 8760) |
| `minimum_down_time` | `int`, optional | no | (≥ 1, ≤ 8760) |
| `primary` | `bool`, optional | no |  |
| `seasonal_operation` | [`SeasonalOperation`](#model-SeasonalOperation) | yes |  |
| `allowed_operation_profile_id` | `int`, optional | no |  |
| `energy_carriers` | list of [`ConversionCarrierRequestDtoV2`](#model-ConversionCarrierRequestDtoV2) | yes |  |
| `maximum_capacity` | `float`, optional | no | (≥ 0.0) |
| `minimum_capacity` | `float`, optional | no | (≥ 0.0) |
| `simultaneous_operation` | `bool`, optional | no |  |

## TechnologyModeResponseDtoV2 { #model-TechnologyModeResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `capacity` | `float`, optional | no | (≥ 0.0) |
| `minimum_annual_output` | `float`, optional | no | (≥ 0.0) |
| `maximum_annual_output` | `float`, optional | no | (≥ 0.0) |
| `curtailment_limitation` | `float`, optional | no | (≥ 0.0) |
| `peak_power` | `float`, optional | no |  |
| `min_part_load` | `float`, optional | no | (≥ 0.0, ≤ 100.0) |
| `minimum_up_time` | `int`, optional | no | (≥ 1, ≤ 8760) |
| `minimum_down_time` | `int`, optional | no | (≥ 1, ≤ 8760) |
| `technology_mode_guid` | `str`, optional | no |  |
| `input_energy_carriers` | list of [`EnergyCarrierResponseDtoV2`](#model-EnergyCarrierResponseDtoV2), optional | no |  |
| `output_energy_carriers` | list of [`EnergyCarrierResponseDtoV2`](#model-EnergyCarrierResponseDtoV2), optional | no |  |
| `seasonal_operation_name` | `str`, optional | no |  |
| `seasonal_operation_value` | `str`, optional | no |  |
| `allowed_operation_profile_id` | `int`, optional | no |  |
| `primary` | `bool`, optional | no |  |
| `maximum_capacity` | `float`, optional | no |  |
| `minimum_capacity` | `float`, optional | no |  |
| `simultaneous_operation` | `bool`, optional | no |  |

## TechnologyPackageListResponseDto { #model-TechnologyPackageListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_packages` | list of [`TechnologyPackageResponseDto`](#model-TechnologyPackageResponseDto), optional | no |  |

## TechnologyPackageListResponseDtoV2 { #model-TechnologyPackageListResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_packages` | list of [`TechnologyPackageResponseDtoV2`](#model-TechnologyPackageResponseDtoV2), optional | no |  |

## TechnologyPackageRequestDtoV2 { #model-TechnologyPackageRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `maximum_conversions` | `int`, optional | no | (≥ 1) |
| `maximum_storages` | `int`, optional | no | (≥ 1) |
| `must_be_installed` | [`MustBeInstalled`](#model-MustBeInstalled) | yes |  |
| `mutually_exclusive_group` | `str`, optional | no |  |
| `name` | `str` | yes |  |
| `conversion_technologies` | list of `str` | yes |  |
| `storage_technologies` | list of `str` | yes |  |

## TechnologyPackageResponseDto { #model-TechnologyPackageResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str`, optional | no |  |
| `guid` | `str`, optional | no |  |
| `conversion_technologies` | list of `str`, optional | no |  |
| `storage_technologies` | list of `str`, optional | no |  |
| `db_organization` | `str`, optional | no |  |

## TechnologyPackageResponseDtoV2 { #model-TechnologyPackageResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `maximum_conversions` | `int`, optional | no | (≥ 1) |
| `maximum_storages` | `int`, optional | no | (≥ 1) |
| `must_be_installed` | [`MustBeInstalled`](#model-MustBeInstalled) | yes |  |
| `mutually_exclusive_group` | `str`, optional | no |  |
| `name` | `str` | yes |  |
| `guid` | `str`, optional | no |  |
| `conversion_technologies` | list of [`GuidNameDto`](#model-GuidNameDto) | yes |  |
| `storage_technologies` | list of [`GuidNameDto`](#model-GuidNameDto) | yes |  |

## Type { #model-Type }

| Member | Value |
| --- | --- |
| `Type.input` | `'INPUT'` |
| `Type.output` | `'OUTPUT'` |

## TypeOfCharging { #model-TypeOfCharging }

| Member | Value |
| --- | --- |
| `TypeOfCharging.smart` | `'Smart'` |
| `TypeOfCharging.dump` | `'Dump'` |
| `TypeOfCharging.v2_g` | `'V2G'` |
| `TypeOfCharging.none` | `'None'` |
| `TypeOfCharging.none_type_none` | `None` |
