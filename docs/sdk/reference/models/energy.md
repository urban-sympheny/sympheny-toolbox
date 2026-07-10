<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/models.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Energy models

## AdvancedPriceComponentRequestDtoV2 { #model-AdvancedPriceComponentRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `value` | `float`, optional | no |  |
| `price_category` | [`PriceCategory`](#model-PriceCategory) | yes |  |
| `price_dimension` | [`PriceDimension`](#model-PriceDimension) | yes |  |
| `type` | [`Type2`](#model-Type2), optional | no |  |
| `time_of_uses` | list of `str`, optional | no |  |
| `price_category_id` | [`PriceCategoryId`](#model-PriceCategoryId), optional | no |  |
| `price_dimension_id` | [`PriceDimensionId`](#model-PriceDimensionId), optional | no |  |

## AdvancedPriceComponentResponseDtoV2 { #model-AdvancedPriceComponentResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str`, optional | no |  |
| `guid` | `str`, optional | no |  |
| `value` | `float`, optional | no |  |
| `price_category` | `str`, optional | no |  |
| `price_category_id` | [`PriceCategoryId`](#model-PriceCategoryId), optional | no |  |
| `price_dimension` | `str`, optional | no |  |
| `price_dimension_id` | [`PriceDimensionId`](#model-PriceDimensionId), optional | no |  |
| `type` | [`Type2`](#model-Type2), optional | no |  |
| `time_of_uses` | list of `str`, optional | no |  |

## AvailableResourceType { #model-AvailableResourceType }

| Member | Value |
| --- | --- |
| `AvailableResourceType.area` | `'Area'` |
| `AvailableResourceType.generic` | `'Generic'` |
| `AvailableResourceType.power` | `'Power'` |

## EnergyCarrierRequestDtoV2 { #model-EnergyCarrierRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sub_type` | [`SubType`](#model-SubType) | yes |  |
| `energy_carrier_name` | `str` | yes | (max length 100, min length 0) |
| `color_hex_code` | `str`, optional | no |  |
| `allow_virtual_load` | `bool`, optional | no |  |

## EnergyCarriersListResponseDto { #model-EnergyCarriersListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_carriers` | list of [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto), optional | no |  |

## EnergyDemandDetailResponseDtoV2 { #model-EnergyDemandDetailResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_demand_guid` | `str`, optional | no |  |
| `energy_demand_name` | `str`, optional | no |  |
| `energy_carrier_guid` | `str`, optional | no |  |
| `energy_carrier_name` | `str`, optional | no |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto), optional | no |  |
| `demand_sale_price` | `float`, optional | no |  |
| `stages` | list of `UUID`, optional | no |  |
| `demand_profile_id` | `int`, optional | no |  |
| `demand_scaling_factor` | `float`, optional | no |  |
| `demand_sale_price_profile_id` | `int`, optional | no |  |
| `demand_sale_price_scaling_factor` | `float`, optional | no |  |
| `energy_demand_user_saved_metadata_guid` | `str`, optional | no |  |
| `energy_demand_user_saved_metadata_name` | `str`, optional | no |  |
| `energy_demand_user_saved_metadata_reference_area` | `float`, optional | no |  |
| `scaling_factor` | `float`, optional | no |  |
| `energy_demand_metadata_guid` | `str`, optional | no |  |
| `energy_demand_metadata_name` | `str`, optional | no |  |
| `energy_demand_metadata_db_organization` | `str`, optional | no |  |
| `energy_demand_metadata_type` | [`EnergyDemandMetadataType`](#model-EnergyDemandMetadataType), optional | no |  |
| `energy_demand_metadata_building_type` | [`EnergyDemandMetadataBuildingType`](#model-EnergyDemandMetadataBuildingType), optional | no |  |
| `energy_demand_metadata_building_age` | [`EnergyDemandMetadataBuildingAge`](#model-EnergyDemandMetadataBuildingAge), optional | no |  |
| `energy_demand_metadata_option` | [`EnergyDemandMetadataOption`](#model-EnergyDemandMetadataOption), optional | no |  |
| `energy_demand_metadata_referenced_area_m2` | `float`, optional | no |  |
| `energy_demand_metadata_specific_energy_demand_value_k_wh_m2` | `float`, optional | no |  |
| `energy_demand_metadata_total_annual_demand` | `float`, optional | no |  |
| `multiplication_factor_preview` | `int`, optional | no |  |
| `multiplication_factor` | `int`, optional | no |  |
| `reverse` | `bool`, optional | no |  |

## EnergyDemandListResponseDto { #model-EnergyDemandListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_demands` | list of [`EnergyDemandResponseDto`](#model-EnergyDemandResponseDto), optional | no |  |

## EnergyDemandMetadataBuildingAge { #model-EnergyDemandMetadataBuildingAge }

| Member | Value |
| --- | --- |
| `EnergyDemandMetadataBuildingAge.age_under_1970` | `'AGE_UNDER_1970'` |
| `EnergyDemandMetadataBuildingAge.age_1970_1980` | `'AGE_1970_1980'` |
| `EnergyDemandMetadataBuildingAge.age_1980_1995` | `'AGE_1980_1995'` |
| `EnergyDemandMetadataBuildingAge.age_1995_2005` | `'AGE_1995_2005'` |
| `EnergyDemandMetadataBuildingAge.age_2005_2015` | `'AGE_2005_2015'` |
| `EnergyDemandMetadataBuildingAge.age_over_2015` | `'AGE_OVER_2015'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_mfh` | `'SIA_2024_EXISTING_MFH'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_sfh` | `'SIA_2024_EXISTING_SFH'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_hotel_room` | `'SIA_2024_EXISTING_HOTEL_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_lobby` | `'SIA_2024_EXISTING_LOBBY'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_single_group_office` | `'SIA_2024_EXISTING_SINGLE_GROUP_OFFICE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_open_plan_office` | `'SIA_2024_EXISTING_OPEN_PLAN_OFFICE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_meeting_room` | `'SIA_2024_EXISTING_MEETING_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_counter_hall` | `'SIA_2024_EXISTING_COUNTER_HALL'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_class_room` | `'SIA_2024_EXISTING_CLASS_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_teachers_lounge` | `'SIA_2024_EXISTING_TEACHERS_LOUNGE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_library` | `'SIA_2024_EXISTING_LIBRARY'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_auditorium` | `'SIA_2024_EXISTING_AUDITORIUM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_school_subject_room` | `'SIA_2024_EXISTING_SCHOOL_SUBJECT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_food_sale_store` | `'SIA_2024_EXISTING_FOOD_SALE_STORE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_specialty_store` | `'SIA_2024_EXISTING_SPECIALTY_STORE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_sales_furniture_diy_garden` | `'SIA_2024_EXISTING_SALES_FURNITURE_DIY_GARDEN'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_patient_room` | `'SIA_2024_EXISTING_PATIENT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_ward_room` | `'SIA_2024_EXISTING_WARD_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_treatment_room` | `'SIA_2024_EXISTING_TREATMENT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_warehouse` | `'SIA_2024_EXISTING_WAREHOUSE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_gymnasium` | `'SIA_2024_EXISTING_GYMNASIUM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_fitness_room` | `'SIA_2024_EXISTING_FITNESS_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_existing_indoor_swimming_pool` | `'SIA_2024_EXISTING_INDOOR_SWIMMING_POOL'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_mfh` | `'SIA_2024_STANDARD_MFH'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_sfh` | `'SIA_2024_STANDARD_SFH'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_hotel_room` | `'SIA_2024_STANDARD_HOTEL_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_lobby` | `'SIA_2024_STANDARD_LOBBY'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_single_group_office` | `'SIA_2024_STANDARD_SINGLE_GROUP_OFFICE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_open_plan_office` | `'SIA_2024_STANDARD_OPEN_PLAN_OFFICE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_meeting_room` | `'SIA_2024_STANDARD_MEETING_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_counter_hall` | `'SIA_2024_STANDARD_COUNTER_HALL'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_class_room` | `'SIA_2024_STANDARD_CLASS_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_teachers_lounge` | `'SIA_2024_STANDARD_TEACHERS_LOUNGE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_library` | `'SIA_2024_STANDARD_LIBRARY'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_auditorium` | `'SIA_2024_STANDARD_AUDITORIUM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_school_subject_room` | `'SIA_2024_STANDARD_SCHOOL_SUBJECT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_food_sale_store` | `'SIA_2024_STANDARD_FOOD_SALE_STORE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_specialty_store` | `'SIA_2024_STANDARD_SPECIALTY_STORE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_sales_furniture_diy_garden` | `'SIA_2024_STANDARD_SALES_FURNITURE_DIY_GARDEN'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_patient_room` | `'SIA_2024_STANDARD_PATIENT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_ward_room` | `'SIA_2024_STANDARD_WARD_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_treatment_room` | `'SIA_2024_STANDARD_TREATMENT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_warehouse` | `'SIA_2024_STANDARD_WAREHOUSE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_gymnasium` | `'SIA_2024_STANDARD_GYMNASIUM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_fitness_room` | `'SIA_2024_STANDARD_FITNESS_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_standard_indoor_swimming_pool` | `'SIA_2024_STANDARD_INDOOR_SWIMMING_POOL'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_mfh` | `'SIA_2024_TARGET_MFH'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_sfh` | `'SIA_2024_TARGET_SFH'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_hotel_room` | `'SIA_2024_TARGET_HOTEL_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_lobby` | `'SIA_2024_TARGET_LOBBY'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_single_group_office` | `'SIA_2024_TARGET_SINGLE_GROUP_OFFICE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_open_plan_office` | `'SIA_2024_TARGET_OPEN_PLAN_OFFICE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_meeting_room` | `'SIA_2024_TARGET_MEETING_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_counter_hall` | `'SIA_2024_TARGET_COUNTER_HALL'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_class_room` | `'SIA_2024_TARGET_CLASS_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_teachers_lounge` | `'SIA_2024_TARGET_TEACHERS_LOUNGE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_library` | `'SIA_2024_TARGET_LIBRARY'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_auditorium` | `'SIA_2024_TARGET_AUDITORIUM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_school_subject_room` | `'SIA_2024_TARGET_SCHOOL_SUBJECT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_food_sale_store` | `'SIA_2024_TARGET_FOOD_SALE_STORE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_specialty_store` | `'SIA_2024_TARGET_SPECIALTY_STORE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_sales_furniture_diy_garden` | `'SIA_2024_TARGET_SALES_FURNITURE_DIY_GARDEN'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_patient_room` | `'SIA_2024_TARGET_PATIENT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_ward_room` | `'SIA_2024_TARGET_WARD_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_treatment_room` | `'SIA_2024_TARGET_TREATMENT_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_warehouse` | `'SIA_2024_TARGET_WAREHOUSE'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_gymnasium` | `'SIA_2024_TARGET_GYMNASIUM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_fitness_room` | `'SIA_2024_TARGET_FITNESS_ROOM'` |
| `EnergyDemandMetadataBuildingAge.sia_2024_target_indoor_swimming_pool` | `'SIA_2024_TARGET_INDOOR_SWIMMING_POOL'` |
| `EnergyDemandMetadataBuildingAge.minergie_new_construction` | `'MINERGIE_NEW_CONSTRUCTION'` |
| `EnergyDemandMetadataBuildingAge.minergie_renovation` | `'MINERGIE_RENOVATION'` |
| `EnergyDemandMetadataBuildingAge.minergie_a` | `'MINERGIE_A'` |
| `EnergyDemandMetadataBuildingAge.minergie_p_new_construction` | `'MINERGIE_P_NEW_CONSTRUCTION'` |
| `EnergyDemandMetadataBuildingAge.minergie_p_renovation` | `'MINERGIE_P_RENOVATION'` |
| `EnergyDemandMetadataBuildingAge.others` | `'OTHERS'` |
| `EnergyDemandMetadataBuildingAge.none_type_none` | `None` |

## EnergyDemandMetadataBuildingType { #model-EnergyDemandMetadataBuildingType }

| Member | Value |
| --- | --- |
| `EnergyDemandMetadataBuildingType.residence_mfh` | `'RESIDENCE_MFH'` |
| `EnergyDemandMetadataBuildingType.residence_sfh` | `'RESIDENCE_SFH'` |
| `EnergyDemandMetadataBuildingType.administration` | `'ADMINISTRATION'` |
| `EnergyDemandMetadataBuildingType.offices` | `'OFFICES'` |
| `EnergyDemandMetadataBuildingType.schools` | `'SCHOOLS'` |
| `EnergyDemandMetadataBuildingType.retail` | `'RETAIL'` |
| `EnergyDemandMetadataBuildingType.restaurant` | `'RESTAURANT'` |
| `EnergyDemandMetadataBuildingType.assembly` | `'ASSEMBLY'` |
| `EnergyDemandMetadataBuildingType.hospitals` | `'HOSPITALS'` |
| `EnergyDemandMetadataBuildingType.industry` | `'INDUSTRY'` |
| `EnergyDemandMetadataBuildingType.warehouse` | `'WAREHOUSE'` |
| `EnergyDemandMetadataBuildingType.sports_center` | `'SPORTS_CENTER'` |
| `EnergyDemandMetadataBuildingType.indoor_pool` | `'INDOOR_POOL'` |
| `EnergyDemandMetadataBuildingType.hotel` | `'HOTEL'` |
| `EnergyDemandMetadataBuildingType.industry_1_shift_fabricated_metals` | `'INDUSTRY_1_SHIFT_FABRICATED_METALS'` |
| `EnergyDemandMetadataBuildingType.industry_2_shift_fabricated_metals` | `'INDUSTRY_2_SHIFT_FABRICATED_METALS'` |
| `EnergyDemandMetadataBuildingType.industry_food_processing` | `'INDUSTRY_FOOD_PROCESSING'` |
| `EnergyDemandMetadataBuildingType.industry_general_manufacturer` | `'INDUSTRY_GENERAL_MANUFACTURER'` |
| `EnergyDemandMetadataBuildingType.industry_pharmaceutical` | `'INDUSTRY_PHARMACEUTICAL'` |
| `EnergyDemandMetadataBuildingType.industry_plastic_manufacturer` | `'INDUSTRY_PLASTIC_MANUFACTURER'` |
| `EnergyDemandMetadataBuildingType.industry_services` | `'INDUSTRY_SERVICES'` |
| `EnergyDemandMetadataBuildingType.industry_warehouse` | `'INDUSTRY_WAREHOUSE'` |
| `EnergyDemandMetadataBuildingType.none_type_none` | `None` |

## EnergyDemandMetadataOption { #model-EnergyDemandMetadataOption }

| Member | Value |
| --- | --- |
| `EnergyDemandMetadataOption.option_1` | `'OPTION_1'` |
| `EnergyDemandMetadataOption.option_2` | `'OPTION_2'` |
| `EnergyDemandMetadataOption.option_3` | `'OPTION_3'` |
| `EnergyDemandMetadataOption.none_type_none` | `None` |

## EnergyDemandMetadataType { #model-EnergyDemandMetadataType }

| Member | Value |
| --- | --- |
| `EnergyDemandMetadataType.electricity` | `'ELECTRICITY'` |
| `EnergyDemandMetadataType.space_heating` | `'SPACE_HEATING'` |
| `EnergyDemandMetadataType.hot_water` | `'HOT_WATER'` |
| `EnergyDemandMetadataType.cooling` | `'COOLING'` |
| `EnergyDemandMetadataType.none_type_none` | `None` |

## EnergyDemandRequestDtoV2 { #model-EnergyDemandRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guids` | list of `str` | yes |  |
| `energy_carrier_guid` | `str` | yes |  |
| `demand_profile_id` | `int` | yes |  |
| `demand_scaling_factor` | `float`, optional | no |  |
| `name` | `str` | yes | (max length 100, min length 0) |
| `demand_sale_price` | `float`, optional | no |  |
| `demand_sale_price_profile_id` | `int`, optional | no |  |
| `demand_sale_price_scaling_factor` | `float`, optional | no |  |
| `stages` | list of `UUID` | yes |  |
| `multiplication_factor` | `int`, optional | no |  |
| `reverse` | `bool`, optional | no |  |

## EnergyDemandResponseDto { #model-EnergyDemandResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_demand_guid` | `str`, optional | no |  |
| `energy_carrier_name` | `str`, optional | no |  |
| `hub_name` | `str`, optional | no |  |
| `energy_demand_name` | `str`, optional | no |  |
| `energy_carrier_guid` | `str`, optional | no |  |
| `hub_guid` | `str`, optional | no |  |
| `demand_sale_price` | `float`, optional | no |  |
| `energy_demand_user_saved_metadata_guid` | `str`, optional | no |  |
| `energy_demand_user_saved_metadata_name` | `str`, optional | no |  |
| `energy_demand_user_saved_metadata_reference_area` | `float`, optional | no |  |
| `scaling_factor` | `float`, optional | no |  |
| `energy_demand_metadata_guid` | `str`, optional | no |  |
| `energy_demand_metadata_name` | `str`, optional | no |  |
| `energy_demand_metadata_db_organization` | `str`, optional | no |  |
| `energy_demand_metadata_type` | [`EnergyDemandMetadataType`](#model-EnergyDemandMetadataType), optional | no |  |
| `energy_demand_metadata_building_type` | [`EnergyDemandMetadataBuildingType`](#model-EnergyDemandMetadataBuildingType), optional | no |  |
| `energy_demand_metadata_building_age` | [`EnergyDemandMetadataBuildingAge`](#model-EnergyDemandMetadataBuildingAge), optional | no |  |
| `energy_demand_metadata_option` | [`EnergyDemandMetadataOption`](#model-EnergyDemandMetadataOption), optional | no |  |
| `energy_demand_metadata_referenced_area_m2` | `float`, optional | no |  |
| `energy_demand_metadata_specific_energy_demand_value_k_wh_m2` | `float`, optional | no |  |
| `energy_demand_metadata_total_annual_demand` | `float`, optional | no |  |
| `multiplication_factor_preview` | `int`, optional | no |  |
| `multiplication_factor` | `int`, optional | no |  |

## EnergyDemandResponseDtoV2 { #model-EnergyDemandResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_demand_guid` | `str`, optional | no |  |
| `energy_carrier_name` | `str` | yes |  |
| `hubs` | list of [`HubResponseDto`](common.md#model-HubResponseDto) | yes |  |
| `energy_demand_name` | `str` | yes |  |
| `energy_carrier_guid` | `str` | yes |  |
| `demand_sale_price` | `float`, optional | no |  |
| `stages` | list of `UUID` | yes |  |
| `demand_profile_id` | `int` | yes |  |
| `demand_scaling_factor` | `float`, optional | no |  |
| `demand_sale_price_profile_id` | `int`, optional | no |  |
| `demand_sale_price_scaling_factor` | `float`, optional | no |  |
| `energy_demand_user_saved_metadata_guid` | `str`, optional | no |  |
| `energy_demand_user_saved_metadata_name` | `str`, optional | no |  |
| `energy_demand_user_saved_metadata_reference_area` | `float`, optional | no |  |
| `scaling_factor` | `float`, optional | no |  |
| `energy_demand_metadata_guid` | `str`, optional | no |  |
| `energy_demand_metadata_name` | `str`, optional | no |  |
| `energy_demand_metadata_db_organization` | `str`, optional | no |  |
| `energy_demand_metadata_type` | [`EnergyDemandMetadataType`](#model-EnergyDemandMetadataType), optional | no |  |
| `energy_demand_metadata_building_type` | [`EnergyDemandMetadataBuildingType`](#model-EnergyDemandMetadataBuildingType), optional | no |  |
| `energy_demand_metadata_building_age` | [`EnergyDemandMetadataBuildingAge`](#model-EnergyDemandMetadataBuildingAge), optional | no |  |
| `energy_demand_metadata_option` | [`EnergyDemandMetadataOption`](#model-EnergyDemandMetadataOption), optional | no |  |
| `energy_demand_metadata_referenced_area_m2` | `float`, optional | no |  |
| `energy_demand_metadata_specific_energy_demand_value_k_wh_m2` | `float`, optional | no |  |
| `energy_demand_metadata_total_annual_demand` | `float`, optional | no |  |
| `multiplication_factor_preview` | `int`, optional | no |  |
| `multiplication_factor` | `int`, optional | no |  |
| `reverse` | `bool` | yes |  |

## HubSolarOnSiteResourceResponseDto { #model-HubSolarOnSiteResourceResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_name` | `str`, optional | no |  |
| `hub_guid` | `str`, optional | no |  |
| `available_solar_collector_area` | `float`, optional | no |  |
| `available_resource_type` | `str`, optional | no |  |
| `technology_dimensioning_std_value` | `float`, optional | no |  |

## HubSolarOnSiteResourceResponseDtoV2 { #model-HubSolarOnSiteResourceResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_name` | `str` | yes |  |
| `hub_guid` | `str` | yes |  |
| `available_solar_collector_area` | `float` | yes |  |
| `available_resource_type` | [`AvailableResourceType`](#model-AvailableResourceType) | yes |  |

## ImpexHubRequestDto { #model-ImpexHubRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guid` | `str` | yes |  |

## ImpexHubResponseDto { #model-ImpexHubResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guid` | `str` | yes |  |
| `hub_name` | `str` | yes |  |
| `hub_updated` | `AwareDatetime` | yes |  |
| `hub_created` | `AwareDatetime` | yes |  |
| `impex_guid` | `str`, optional | no |  |

## ImportExportRequestDtoV2 { #model-ImportExportRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_price_ch_fk_wh` | `float`, optional | no |  |
| `max_capacity_kw` | `float`, optional | no |  |
| `total_annual_energy_available_k_wh_a` | `float`, optional | no |  |
| `capacity_price_ch_fk_w_year` | `float`, optional | no |  |
| `name` | `str` | yes |  |
| `hourly_energy_price_profile_id` | `int`, optional | no |  |
| `capacity_price_ch_fk_w_month` | `float`, optional | no |  |
| `fixed_om_price_chf_year` | `float`, optional | no |  |
| `co2_intensity_kg_co2k_wh_co2_compensation_kg_co2k_wh` | `float`, optional | no |  |
| `dynamic_co2_profile_id` | `int`, optional | no |  |
| `maximum_hourly_energy_available_profile_id` | `int`, optional | no |  |
| `energy_carrier_guid` | `str` | yes |  |
| `type` | [`Type1`](#model-Type1) | yes |  |
| `hubs` | list of [`ImpexHubRequestDto`](#model-ImpexHubRequestDto) | yes |  |
| `product` | `str`, optional | no |  |
| `year` | `int`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `suggested` | `bool`, optional | no |  |
| `price_components` | list of [`AdvancedPriceComponentRequestDtoV2`](#model-AdvancedPriceComponentRequestDtoV2), optional | no |  |
| `time_of_uses` | list of [`TimeOfUseRequestDto`](#model-TimeOfUseRequestDto), optional | no |  |
| `stages` | list of `UUID` | yes |  |

## ImportExportResponseDtoV2 { #model-ImportExportResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `energy_price_ch_fk_wh` | `float`, optional | no |  |
| `max_capacity_kw` | `float`, optional | no |  |
| `total_annual_energy_available_k_wh_a` | `float`, optional | no |  |
| `capacity_price_ch_fk_w_year` | `float`, optional | no |  |
| `name` | `str` | yes |  |
| `hourly_energy_price_profile_id` | `int`, optional | no |  |
| `capacity_price_ch_fk_w_month` | `float`, optional | no |  |
| `fixed_om_price_chf_year` | `float`, optional | no |  |
| `co2_intensity_kg_co2k_wh_co2_compensation_kg_co2k_wh` | `float`, optional | no |  |
| `dynamic_co2_profile_id` | `int`, optional | no |  |
| `maximum_hourly_energy_available_profile_id` | `int`, optional | no |  |
| `energy_carrier` | [`EnergyCarrierResponseDto`](common.md#model-EnergyCarrierResponseDto) | yes |  |
| `type` | `str` | yes |  |
| `hubs` | list of [`ImpexHubResponseDto`](#model-ImpexHubResponseDto) | yes |  |
| `guid` | `str`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `price_components` | list of [`AdvancedPriceComponentResponseDtoV2`](#model-AdvancedPriceComponentResponseDtoV2) | yes |  |
| `time_of_uses` | list of [`TimeOfUseResponseDto`](#model-TimeOfUseResponseDto) | yes |  |
| `product` | `str`, optional | no |  |
| `year` | `int`, optional | no |  |
| `notes` | `str`, optional | no |  |
| `source` | `str`, optional | no |  |
| `suggested` | `bool`, optional | no |  |
| `stages` | list of `UUID` | yes |  |

## IrradianceProfileType { #model-IrradianceProfileType }

| Member | Value |
| --- | --- |
| `IrradianceProfileType.generated` | `'GENERATED'` |
| `IrradianceProfileType.uploaded` | `'UPLOADED'` |
| `IrradianceProfileType.saved` | `'SAVED'` |

## IrradianceProfileType1 { #model-IrradianceProfileType1 }

| Member | Value |
| --- | --- |
| `IrradianceProfileType1.generated` | `'GENERATED'` |
| `IrradianceProfileType1.uploaded` | `'UPLOADED'` |
| `IrradianceProfileType1.saved` | `'SAVED'` |
| `IrradianceProfileType1.none_type_none` | `None` |

## PriceCategory { #model-PriceCategory }

| Member | Value |
| --- | --- |
| `PriceCategory.energy_delivery` | `'ENERGY_DELIVERY'` |
| `PriceCategory.network_use` | `'NETWORK_USE'` |
| `PriceCategory.taxes` | `'TAXES'` |
| `PriceCategory.refunds_and_rebates` | `'REFUNDS_AND_REBATES'` |
| `PriceCategory.total` | `'TOTAL'` |

## PriceCategoryId { #model-PriceCategoryId }

| Member | Value |
| --- | --- |
| `PriceCategoryId.energy_delivery` | `'ENERGY_DELIVERY'` |
| `PriceCategoryId.network_use` | `'NETWORK_USE'` |
| `PriceCategoryId.taxes` | `'TAXES'` |
| `PriceCategoryId.refunds_and_rebates` | `'REFUNDS_AND_REBATES'` |
| `PriceCategoryId.total` | `'TOTAL'` |
| `PriceCategoryId.none_type_none` | `None` |

## PriceDimension { #model-PriceDimension }

| Member | Value |
| --- | --- |
| `PriceDimension.energy_price_chf_kwh` | `'ENERGY_PRICE_CHF_KWH'` |
| `PriceDimension.capacity_price_chf_kw_month` | `'CAPACITY_PRICE_CHF_KW_MONTH'` |
| `PriceDimension.capacity_price_chf_kw_year` | `'CAPACITY_PRICE_CHF_KW_YEAR'` |
| `PriceDimension.fixed_om_price_chf_year` | `'FIXED_OM_PRICE_CHF_YEAR'` |

## PriceDimensionId { #model-PriceDimensionId }

| Member | Value |
| --- | --- |
| `PriceDimensionId.energy_price_chf_kwh` | `'ENERGY_PRICE_CHF_KWH'` |
| `PriceDimensionId.capacity_price_chf_kw_month` | `'CAPACITY_PRICE_CHF_KW_MONTH'` |
| `PriceDimensionId.capacity_price_chf_kw_year` | `'CAPACITY_PRICE_CHF_KW_YEAR'` |
| `PriceDimensionId.fixed_om_price_chf_year` | `'FIXED_OM_PRICE_CHF_YEAR'` |
| `PriceDimensionId.none_type_none` | `None` |

## ProfileDetailsResponseDto { #model-ProfileDetailsResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int`, optional | no |  |
| `name` | `str` | yes |  |
| `values` | list of [`ProfilePeriodValueDto`](#model-ProfilePeriodValueDto) | yes |  |

## ProfileJsonRequestDto { #model-ProfileJsonRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `values` | list of [`ProfilePeriodValueDto`](#model-ProfilePeriodValueDto) | yes |  |

## ProfilePeriodValueDto { #model-ProfilePeriodValueDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `period` | `int` | yes |  |
| `demand_value` | `float` | yes |  |

## ProfileResponseDto { #model-ProfileResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `int`, optional | no |  |
| `name` | `str`, optional | no |  |

## SolarOnSiteResourceListResponseDto { #model-SolarOnSiteResourceListResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `solar_resources` | list of [`SolarOnSiteResourceResponseDto`](#model-SolarOnSiteResourceResponseDto), optional | no |  |

## SolarOnSiteResourceRequestDtoV2 { #model-SolarOnSiteResourceRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `energy_carrier_guid` | `str` | yes |  |
| `hubs` | list of [`SolarOnSiteResourcesHubRequestDtoV2`](#model-SolarOnSiteResourcesHubRequestDtoV2) | yes |  |
| `profile_id` | `int` | yes |  |
| `stages` | list of `UUID` | yes |  |

## SolarOnSiteResourceResponseDto { #model-SolarOnSiteResourceResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `solar_resource_guid` | `str`, optional | no |  |
| `energy_carrier_guid` | `str`, optional | no |  |
| `energy_carrier_name` | `str`, optional | no |  |
| `hubs` | list of [`HubSolarOnSiteResourceResponseDto`](#model-HubSolarOnSiteResourceResponseDto), optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `irradiance_profile_type` | [`IrradianceProfileType1`](#model-IrradianceProfileType1), optional | no |  |
| `solar_resource_metadata_name` | `str`, optional | no |  |
| `solar_resource_metadata_db_organization` | `str`, optional | no |  |
| `solar_resource_metadata_guid` | `str`, optional | no |  |
| `solar_resource_metadata_location` | `str`, optional | no |  |
| `solar_resource_metadata_type` | `str`, optional | no |  |
| `solar_resource_metadata_slope` | `float`, optional | no |  |
| `solar_resource_metadata_orientation` | `str`, optional | no |  |

## SolarOnSiteResourceResponseDtoV2 { #model-SolarOnSiteResourceResponseDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `solar_resource_guid` | `str`, optional | no |  |
| `energy_carrier_guid` | `str` | yes |  |
| `energy_carrier_name` | `str` | yes |  |
| `hubs` | list of [`HubSolarOnSiteResourceResponseDtoV2`](#model-HubSolarOnSiteResourceResponseDtoV2) | yes |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `irradiance_profile_type` | [`IrradianceProfileType`](#model-IrradianceProfileType) | yes |  |
| `solar_resource_metadata_name` | `str`, optional | no |  |
| `solar_resource_metadata_db_organization` | `str`, optional | no |  |
| `solar_resource_metadata_guid` | `str`, optional | no |  |
| `solar_resource_metadata_location` | `str`, optional | no |  |
| `solar_resource_metadata_type` | `str`, optional | no |  |
| `solar_resource_metadata_slope` | `float`, optional | no |  |
| `solar_resource_metadata_orientation` | `str`, optional | no |  |
| `stages` | list of `UUID` | yes |  |
| `profile_id` | `int` | yes |  |

## SolarOnSiteResourcesHubRequestDtoV2 { #model-SolarOnSiteResourcesHubRequestDtoV2 }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_guid` | `str` | yes |  |
| `available_solar_collector_area` | `float` | yes | (> 0.0) |
| `available_resource_type` | [`AvailableResourceType`](#model-AvailableResourceType) | yes |  |

## SubType { #model-SubType }

| Member | Value |
| --- | --- |
| `SubType.electricity` | `'ELECTRICITY'` |
| `SubType.electricity_renewable` | `'ELECTRICITY_RENEWABLE'` |
| `SubType.wood_chips` | `'WOOD_CHIPS'` |
| `SubType.wood_pellets` | `'WOOD_PELLETS'` |
| `SubType.coal` | `'COAL'` |
| `SubType.oil` | `'OIL'` |
| `SubType.gas` | `'GAS'` |
| `SubType.biogas` | `'BIOGAS'` |
| `SubType.hydrogen` | `'HYDROGEN'` |
| `SubType.hydrogen_pressurized` | `'HYDROGEN_PRESSURIZED'` |
| `SubType.cooling_1` | `'COOLING_1'` |
| `SubType.cooling_2` | `'COOLING_2'` |
| `SubType.cooling_3` | `'COOLING_3'` |
| `SubType.cooling_4` | `'COOLING_4'` |
| `SubType.ice` | `'ICE'` |
| `SubType.heat_1` | `'HEAT_1'` |
| `SubType.heat_2` | `'HEAT_2'` |
| `SubType.heat_3` | `'HEAT_3'` |
| `SubType.heat_4` | `'HEAT_4'` |
| `SubType.heat_5` | `'HEAT_5'` |
| `SubType.heat_6` | `'HEAT_6'` |
| `SubType.heat_7` | `'HEAT_7'` |
| `SubType.heat_8` | `'HEAT_8'` |
| `SubType.heat_9` | `'HEAT_9'` |
| `SubType.heat_ambient` | `'HEAT_AMBIENT'` |
| `SubType.steam_low_pressure` | `'STEAM_LOW_PRESSURE'` |
| `SubType.solar_roof` | `'SOLAR_ROOF'` |
| `SubType.solar_facade` | `'SOLAR_FACADE'` |
| `SubType.solar_parapet` | `'SOLAR_PARAPET'` |
| `SubType.wind` | `'WIND'` |
| `SubType.hydro` | `'HYDRO'` |
| `SubType.biomass` | `'BIOMASS'` |
| `SubType.geothermal` | `'GEOTHERMAL'` |
| `SubType.tidal` | `'TIDAL'` |
| `SubType.process_waste_heat` | `'PROCESS_WASTE_HEAT'` |
| `SubType.custom` | `'CUSTOM'` |

## TimeOfUseRequestDto { #model-TimeOfUseRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str`, optional | no |  |
| `months` | list of `str`, optional | no |  |
| `days` | list of `str`, optional | no |  |
| `start_time` | `str`, optional | no |  |
| `end_time` | `str`, optional | no |  |

## TimeOfUseResponseDto { #model-TimeOfUseResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str`, optional | no |  |
| `months` | list of `str`, optional | no |  |
| `days` | list of `str`, optional | no |  |
| `start_time` | `str`, optional | no |  |
| `end_time` | `str`, optional | no |  |

## Type1 { #model-Type1 }

| Member | Value |
| --- | --- |
| `Type1.import_` | `'IMPORT'` |
| `Type1.export` | `'EXPORT'` |

## Type2 { #model-Type2 }

| Member | Value |
| --- | --- |
| `Type2.time_of_use` | `'TIME_OF_USE'` |
| `Type2.fixed` | `'FIXED'` |
| `Type2.none_type_none` | `None` |
