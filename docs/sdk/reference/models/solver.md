<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/models.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Solver job and user models

## AwsRegion { #model-AwsRegion }

| Member | Value |
| --- | --- |
| `AwsRegion.eu_north_1` | `'eu-north-1'` |
| `AwsRegion.eu_central_2` | `'eu-central-2'` |

## BillingCycle { #model-BillingCycle }

| Member | Value |
| --- | --- |
| `BillingCycle.monthly` | `'MONTHLY'` |
| `BillingCycle.quarterly` | `'QUARTERLY'` |
| `BillingCycle.annually` | `'ANNUALLY'` |

## GetOrganizationExt { #model-GetOrganizationExt }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `gis_on` | `bool`, optional | no |  |
| `sep_on` | `bool`, optional | no |  |
| `sep_buildings_limit` | `int`, optional | no |  |
| `execution_slots` | `int`, optional | no |  |
| `variable_billing` | `bool`, optional | no |  |
| `max_executions` | `int`, optional | no |  |
| `max_simultaneous_executions` | `int`, optional | no |  |
| `max_execution_time` | `int`, optional | no |  |
| `max_execution_time_week` | `int`, optional | no |  |
| `number_of_executions_left` | `int`, optional | no |  |
| `execution_time_week_left` | `int`, optional | no |  |
| `id` | `UUID4` | yes |  |
| `created` | `AwareDatetime` | yes |  |
| `updated` | `AwareDatetime` | yes |  |
| `sep_buildings_consumed` | `int`, optional | no |  |

## GetPlanExt { #model-GetPlanExt }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `intra_hub_network` | `bool`, optional | no |  |
| `advanced_cost_components` | `bool`, optional | no |  |
| `unit_commitment` | `bool`, optional | no |  |
| `max_energy_carriers_per_hub` | `int`, optional | no |  |
| `max_energy_demands` | `int`, optional | no |  |
| `max_hubs` | `int`, optional | no |  |
| `max_stages` | `int`, optional | no | (≤ 8) |
| `max_solar_resources` | `int`, optional | no |  |
| `max_other_resources` | `int`, optional | no |  |
| `max_imports` | `int`, optional | no |  |
| `max_exports` | `int`, optional | no |  |
| `max_conversion_techs` | `int`, optional | no |  |
| `max_conversion_modes` | `int`, optional | no |  |
| `max_storage_techs` | `int`, optional | no |  |
| `max_network_techs` | `int`, optional | no |  |
| `max_network_links` | `int`, optional | no |  |
| `max_executions` | `int`, optional | no |  |
| `max_simultaneous_executions` | `int`, optional | no |  |
| `max_execution_time` | `int`, optional | no |  |
| `max_execution_time_week` | `int`, optional | no |  |
| `max_execution_history` | `int`, optional | no | (≤ 500) |
| `max_pareto_points` | `int`, optional | no | (≤ 9) |
| `full_temporal_resolution` | `bool`, optional | no |  |
| `max_projects` | `int`, optional | no |  |
| `max_analyses` | `int`, optional | no |  |
| `max_scenarios` | `int`, optional | no |  |
| `share_project` | `bool`, optional | no |  |
| `organization_db` | `bool`, optional | no |  |
| `scenario_variants` | `bool`, optional | no |  |
| `max_scenario_variants` | `int`, optional | no |  |
| `name` | `str` | yes |  |
| `id` | `UUID4` | yes |  |
| `created` | `AwareDatetime` | yes |  |
| `updated` | `AwareDatetime`, optional | yes |  |
| `sagemaker_on` | `bool` | yes |  |
| `sagemaker_regions` | list of [`AwsRegion`](#model-AwsRegion) | yes |  |

## GetSolverJobExt { #model-GetSolverJobExt }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | [`JobStatus`](#model-JobStatus), optional | no |  |
| `status_msg` | `str`, optional | no |  |
| `batch_id` | `str`, optional | no |  |
| `points_completed` | `int`, optional | no |  |
| `started` | `AwareDatetime`, optional | no |  |
| `terminated` | `AwareDatetime`, optional | no |  |
| `infeasibility_info` | `str`, optional | no |  |
| `name` | `str` | yes |  |
| `objective1` | [`ObjectiveFunction`](#model-ObjectiveFunction) | yes |  |
| `objective2` | [`ObjectiveFunction`](#model-ObjectiveFunction), optional | no |  |
| `scenario_guid` | `str`, optional | no |  |
| `scenario_name` | `str`, optional | no |  |
| `temporal_resolution` | [`TemporalResolution`](#model-TemporalResolution) | yes |  |
| `points` | `int` | yes | (≥ 1, ≤ 10) |
| `time_limit` | `int` | yes | (≥ 1, ≤ 18720) |
| `mip_gap` | `float` | yes | (≥ 0.1, < 100.0) |
| `account_guid` | `str` | yes |  |
| `organization_id` | `UUID4` | yes |  |
| `subscription_id` | `UUID4` | yes |  |
| `id` | `UUID4` | yes |  |
| `created` | `AwareDatetime` | yes |  |
| `input_file` | [`InputFile`](#model-InputFile), optional | no |  |
| `output_file` | [`OutputFile`](#model-OutputFile), optional | no |  |

## GetSubscriptionExt { #model-GetSubscriptionExt }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `organization_id` | `UUID4` | yes |  |
| `start_date` | `date` | yes |  |
| `end_date` | `date`, optional | no |  |
| `billing_cycle` | [`BillingCycle`](#model-BillingCycle), optional | no |  |
| `next_billing_date` | `date`, optional | no |  |
| `variable_billing` | `bool`, optional | no |  |
| `execution_priority` | `int`, optional | no |  |
| `max_simultaneous_executions` | `int`, optional | no |  |
| `max_executions_per_cycle` | `int`, optional | no |  |
| `max_execution_time_per_cycle` | `int`, optional | no |  |
| `max_executions_per_week` | `int`, optional | no |  |
| `max_execution_time_per_week` | `int`, optional | no |  |
| `user_max_executions_per_cycle` | `int`, optional | no |  |
| `user_max_execution_time_per_cycle` | `int`, optional | no |  |
| `user_max_executions_per_week` | `int`, optional | no |  |
| `user_max_execution_time_per_week` | `int`, optional | no |  |
| `id` | `UUID4` | yes |  |
| `created` | `AwareDatetime` | yes |  |
| `updated` | `AwareDatetime` | yes |  |

## GetUsageExt { #model-GetUsageExt }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `subscription` | [`SubscriptionUsage`](#model-SubscriptionUsage) | yes |  |
| `user` | [`UserUsage`](#model-UserUsage) | yes |  |

## GetUserProfileExt { #model-GetUserProfileExt }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `account` | [`User`](#model-User) | yes |  |
| `preferences` | [`Preferences`](#model-Preferences) | yes |  |
| `plan_limitation` | [`GetPlanExt`](#model-GetPlanExt) | yes |  |
| `organization` | [`GetOrganizationExt`](#model-GetOrganizationExt) | yes |  |
| `subscription` | [`GetSubscriptionExt`](#model-GetSubscriptionExt) | yes |  |
| `profile_picture` | `str`, optional | no |  |
| `organization_picture` | `str`, optional | no |  |

## InputFile { #model-InputFile }

Root model wrapping `AnyUrl`.

## JobStatus { #model-JobStatus }

| Member | Value |
| --- | --- |
| `JobStatus.validating` | `'VALIDATING'` |
| `JobStatus.valid` | `'VALID'` |
| `JobStatus.pending` | `'PENDING'` |
| `JobStatus.queued` | `'QUEUED'` |
| `JobStatus.running` | `'RUNNING'` |
| `JobStatus.done` | `'DONE'` |
| `JobStatus.stopped` | `'STOPPED'` |
| `JobStatus.failed` | `'FAILED'` |
| `JobStatus.invalid` | `'INVALID'` |

## Language { #model-Language }

| Member | Value |
| --- | --- |
| `Language.english` | `'English'` |
| `Language.german` | `'German'` |

## ObjectiveFunction { #model-ObjectiveFunction }

| Member | Value |
| --- | --- |
| `ObjectiveFunction.min_life_cycle_cost` | `'MIN_LIFE_CYCLE_COST'` |
| `ObjectiveFunction.min_annualized_cost` | `'MIN_ANNUALIZED_COST'` |
| `ObjectiveFunction.min_co2_emissions` | `'MIN_CO2_EMISSIONS'` |
| `ObjectiveFunction.min_investment` | `'MIN_INVESTMENT'` |
| `ObjectiveFunction.min_om` | `'MIN_OM'` |
| `ObjectiveFunction.min_fuel_imports` | `'MIN_FUEL_IMPORTS'` |
| `ObjectiveFunction.min_replacement` | `'MIN_REPLACEMENT'` |
| `ObjectiveFunction.max_exports` | `'MAX_EXPORTS'` |
| `ObjectiveFunction.max_salvage` | `'MAX_SALVAGE'` |

## OutputFile { #model-OutputFile }

Root model wrapping `AnyUrl`.

## PostSolverJobExt { #model-PostSolverJobExt }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `objective1` | [`ObjectiveFunction`](#model-ObjectiveFunction) | yes |  |
| `objective2` | [`ObjectiveFunction`](#model-ObjectiveFunction), optional | no |  |
| `scenario_guid` | `str`, optional | no |  |
| `scenario_name` | `str`, optional | no |  |
| `temporal_resolution` | [`TemporalResolution`](#model-TemporalResolution) | yes |  |
| `points` | `int` | yes | (≥ 1, ≤ 10) |
| `time_limit` | `int` | yes | (≥ 1, ≤ 18720) |
| `mip_gap` | `float` | yes | (≥ 0.1, < 100.0) |
| `input_file_id` | `UUID4`, optional | no |  |

## Preferences { #model-Preferences }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `exchange_currency_default` | `str` | yes |  |
| `unit_system_default` | `str` | yes |  |
| `language_default` | [`Language`](#model-Language) | yes |  |
| `interest_rate_default` | `float`, optional | no |  |
| `first_name` | `str`, optional | no |  |
| `last_name` | `str`, optional | no |  |
| `created` | `AwareDatetime` | yes |  |
| `updated` | `AwareDatetime` | yes |  |

## SolverJob { #model-SolverJob }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | [`JobStatus`](#model-JobStatus), optional | no |  |
| `status_msg` | `str`, optional | no |  |
| `batch_id` | `str`, optional | no |  |
| `points_completed` | `int`, optional | no |  |
| `started` | `AwareDatetime`, optional | no |  |
| `terminated` | `AwareDatetime`, optional | no |  |
| `infeasibility_info` | `str`, optional | no |  |
| `name` | `str` | yes |  |
| `objective1` | [`ObjectiveFunction`](#model-ObjectiveFunction) | yes |  |
| `objective2` | [`ObjectiveFunction`](#model-ObjectiveFunction), optional | no |  |
| `scenario_guid` | `str`, optional | no |  |
| `scenario_name` | `str`, optional | no |  |
| `temporal_resolution` | [`TemporalResolution`](#model-TemporalResolution) | yes |  |
| `points` | `int` | yes | (≥ 1, ≤ 10) |
| `time_limit` | `int` | yes | (≥ 1, ≤ 18720) |
| `mip_gap` | `float` | yes | (≥ 0.1, < 100.0) |
| `account_guid` | `str` | yes |  |
| `organization_id` | `UUID4` | yes |  |
| `subscription_id` | `UUID4` | yes |  |
| `id` | `UUID4` | yes |  |
| `created` | `AwareDatetime` | yes |  |

## SubscriptionUsage { #model-SubscriptionUsage }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total_count_overage` | `int` | yes |  |
| `total_minutes_overage` | `int` | yes |  |
| `weekly_count_overage` | `int` | yes |  |
| `weekly_minutes_overage` | `int` | yes |  |
| `total_count` | `int` | yes |  |
| `total_minutes` | `int` | yes |  |
| `current_week_count` | `int` | yes |  |
| `current_week_minutes` | `int` | yes |  |

## TemporalResolution { #model-TemporalResolution }

| Member | Value |
| --- | --- |
| `TemporalResolution.low` | `'LOW'` |
| `TemporalResolution.medium` | `'MEDIUM'` |
| `TemporalResolution.high` | `'HIGH'` |
| `TemporalResolution.full` | `'FULL'` |

## User { #model-User }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `str` | yes |  |
| `plan_limitation_id` | `UUID4` | yes |  |
| `organization_id` | `UUID4` | yes |  |
| `subscription_id` | `UUID4` | yes |  |
| `plan_expiry` | `date`, optional | no |  |
| `number_of_executions_left` | `int`, optional | no |  |
| `execution_time_week_left` | `int`, optional | no |  |
| `mfa` | `bool`, optional | no |  |
| `deactivated` | `bool`, optional | no |  |
| `superuser` | `bool`, optional | no |  |
| `admin` | `bool`, optional | no |  |
| `show_maintenance_info` | `bool`, optional | no |  |
| `show_gtc` | `bool`, optional | no |  |
| `show_user_guide` | `bool`, optional | no |  |
| `account_guid` | `str` | yes |  |
| `created` | `AwareDatetime` | yes |  |
| `updated` | `AwareDatetime` | yes |  |

## UserUsage { #model-UserUsage }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total_count` | `int` | yes |  |
| `total_minutes` | `int` | yes |  |
| `current_week_count` | `int` | yes |  |
| `current_week_minutes` | `int` | yes |  |
| `history_count` | `int`, optional | no |  |
