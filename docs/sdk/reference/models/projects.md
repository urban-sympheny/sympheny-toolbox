<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/models.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Project and analysis models

## AnalysisDetailsResponseDto { #model-AnalysisDetailsResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str`, optional | no |  |
| `analysis_name` | `str`, optional | no |  |
| `execution_status` | [`ExecutionStatus`](#model-ExecutionStatus), optional | no |  |
| `execution_in_progress` | `bool`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `cover_image` | `str`, optional | no |  |
| `project_name` | `str`, optional | no |  |
| `scenarios` | list of [`ScenarioResponseDto`](common.md#model-ScenarioResponseDto), optional | no |  |
| `execution_options` | [`ExecutionOptionsResponseDto`](#model-ExecutionOptionsResponseDto), optional | no |  |
| `results` | [`ResultsResponseDto`](#model-ResultsResponseDto), optional | no |  |
| `project_guid` | `str`, optional | no |  |

## AnalysisRequestDto { #model-AnalysisRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_name` | `str` | yes | (max length 100, min length 0) |

## AnalysisResponseDto { #model-AnalysisResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `analysis_guid` | `str`, optional | no |  |
| `analysis_name` | `str`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `scenarios` | list of [`ScenarioResponseDto`](common.md#model-ScenarioResponseDto), optional | no |  |

## ExecutionOptionsResponseDto { #model-ExecutionOptionsResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `objective1` | `str`, optional | no |  |
| `objective2` | `str`, optional | no |  |
| `number_of_pareto_points` | `int`, optional | no |  |
| `scenarios` | list of `str`, optional | no |  |

## ExecutionStatus { #model-ExecutionStatus }

| Member | Value |
| --- | --- |
| `ExecutionStatus.in_specification` | `'IN_SPECIFICATION'` |
| `ExecutionStatus.ready_to_submit` | `'READY_TO_SUBMIT'` |
| `ExecutionStatus.picked` | `'PICKED'` |
| `ExecutionStatus.failed` | `'FAILED'` |
| `ExecutionStatus.aborted` | `'ABORTED'` |
| `ExecutionStatus.running` | `'RUNNING'` |
| `ExecutionStatus.done` | `'DONE'` |
| `ExecutionStatus.none_type_none` | `None` |

## ImageResponseDto { #model-ImageResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `str`, optional | no |  |
| `guid` | `str`, optional | no |  |
| `cover` | `bool`, optional | no |  |

## ProjectDetailResponseDto { #model-ProjectDetailResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `images` | list of [`ImageResponseDto`](#model-ImageResponseDto), optional | no |  |
| `project_name` | `str`, optional | no |  |
| `project_guid` | `str`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `project_owner` | `str`, optional | no |  |
| `project_owner_email` | `str`, optional | no |  |
| `secondary_owners` | list of [`SecondaryOwnerDto`](#model-SecondaryOwnerDto), optional | no |  |
| `lock_user_email` | `str`, optional | no |  |
| `lock` | `bool`, optional | no |  |
| `lock_time` | `AwareDatetime`, optional | no |  |
| `owned_by_current_user` | `bool`, optional | no |  |
| `editable_by_current_user` | `bool`, optional | no |  |
| `owner_history` | list of [`ProjectOwnerHistoryResponseDto`](#model-ProjectOwnerHistoryResponseDto), optional | no |  |
| `analyses` | list of [`AnalysisResponseDto`](#model-AnalysisResponseDto), optional | no |  |
| `cover_image` | `str`, optional | no |  |
| `original_default_project_guid` | `str`, optional | no |  |
| `version` | [`Version1`](#model-Version1), optional | no |  |
| `webhook_url` | `str`, optional | no |  |
| `favorite` | `bool`, optional | no |  |
| `gis_centroid_x` | `float`, optional | no |  |
| `gis_centroid_y` | `float`, optional | no |  |
| `zoom_extent_xmin` | `float`, optional | no |  |
| `zoom_extent_ymin` | `float`, optional | no |  |
| `zoom_extent_xmax` | `float`, optional | no |  |
| `zoom_extent_ymax` | `float`, optional | no |  |

## ProjectOwnerHistoryResponseDto { #model-ProjectOwnerHistoryResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `owned_at` | `AwareDatetime`, optional | no |  |
| `owner_email` | `str`, optional | no |  |

## ProjectRequestDto { #model-ProjectRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `project_name` | `str` | yes | (max length 100, min length 0) |
| `version` | [`Version`](#model-Version) | yes |  |
| `webhook_url` | `str`, optional | no |  |
| `favorite` | `bool`, optional | no |  |
| `gis_centroid_x` | `float`, optional | no |  |
| `gis_centroid_y` | `float`, optional | no |  |
| `zoom_extent_xmin` | `float`, optional | no |  |
| `zoom_extent_ymin` | `float`, optional | no |  |
| `zoom_extent_xmax` | `float`, optional | no |  |
| `zoom_extent_ymax` | `float`, optional | no |  |

## ProjectResponseDto { #model-ProjectResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `project_name` | `str`, optional | no |  |
| `project_guid` | `str`, optional | no |  |
| `created` | `AwareDatetime`, optional | no |  |
| `updated` | `AwareDatetime`, optional | no |  |
| `cover_image` | `str`, optional | no |  |
| `project_owner_email` | `str`, optional | no |  |
| `secondary_owners` | list of [`SecondaryOwnerDto`](#model-SecondaryOwnerDto), optional | no |  |
| `lock_user_email` | `str`, optional | no |  |
| `lock` | `bool`, optional | no |  |
| `lock_time` | `AwareDatetime`, optional | no |  |
| `owned_by_current_user` | `bool`, optional | no |  |
| `editable_by_current_user` | `bool`, optional | no |  |
| `original_default_project_guid` | `str`, optional | no |  |
| `version` | [`Version1`](#model-Version1), optional | no |  |
| `favorite` | `bool`, optional | no |  |
| `gis_centroid_x` | `float`, optional | no |  |
| `gis_centroid_y` | `float`, optional | no |  |
| `zoom_extent_xmin` | `float`, optional | no |  |
| `zoom_extent_ymin` | `float`, optional | no |  |
| `zoom_extent_xmax` | `float`, optional | no |  |
| `zoom_extent_ymax` | `float`, optional | no |  |
| `processing` | `bool`, optional | no |  |

## ProjectSummaryResponseDto { #model-ProjectSummaryResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `projects` | list of [`ProjectResponseDto`](#model-ProjectResponseDto), optional | no |  |

## ResultsResponseDto { #model-ResultsResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `execution_submitted` | `AwareDatetime`, optional | no |  |
| `scenarios` | list of [`ResultsScenarioResponseDto`](#model-ResultsScenarioResponseDto), optional | no |  |
| `dashboard_url` | `str`, optional | no |  |

## ResultsScenarioResponseDto { #model-ResultsScenarioResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_name` | `str`, optional | no |  |
| `status` | [`Status1`](#model-Status1), optional | no |  |
| `status_message` | `str`, optional | no |  |
| `pareto_points_completed` | `str`, optional | no |  |
| `input_filepath` | `str`, optional | no |  |
| `output_filepath` | `str`, optional | no |  |

## SecondaryOwnerDto { #model-SecondaryOwnerDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `str` | yes |  |
| `can_edit` | `bool`, optional | no |  |
| `favorite` | `bool`, optional | no |  |

## Status1 { #model-Status1 }

| Member | Value |
| --- | --- |
| `Status1.in_specification` | `'IN_SPECIFICATION'` |
| `Status1.submitted` | `'SUBMITTED'` |
| `Status1.aborted` | `'ABORTED'` |
| `Status1.validating` | `'VALIDATING'` |
| `Status1.valid` | `'VALID'` |
| `Status1.invalid` | `'INVALID'` |
| `Status1.pending` | `'PENDING'` |
| `Status1.running` | `'RUNNING'` |
| `Status1.done_optimization` | `'DONE_OPTIMIZATION'` |
| `Status1.generating_results` | `'GENERATING_RESULTS'` |
| `Status1.done` | `'DONE'` |
| `Status1.failed` | `'FAILED'` |
| `Status1.stopped` | `'STOPPED'` |
| `Status1.none_type_none` | `None` |

## Version { #model-Version }

| Member | Value |
| --- | --- |
| `Version.v1` | `'V1'` |
| `Version.v2` | `'V2'` |

## Version1 { #model-Version1 }

| Member | Value |
| --- | --- |
| `Version1.v1` | `'V1'` |
| `Version1.v2` | `'V2'` |
| `Version1.none_type_none` | `None` |
