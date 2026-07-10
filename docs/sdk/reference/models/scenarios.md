<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/models.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Scenario, stage, and hub models

## HubRequestDto { #model-HubRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `hub_name` | `str` | yes | (max length 100, min length 0) |

## ScenarioRequestDto { #model-ScenarioRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_name` | `str` | yes | (max length 100, min length 0) |

## StageRequestDto { #model-StageRequestDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `length` | `int` | yes |  |
| `interest_rate` | `float`, optional | no |  |
| `inflation_rate` | `float`, optional | no |  |
| `index` | `int` | yes |  |

## StageResponseDto { #model-StageResponseDto }

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `str` | yes |  |
| `length` | `int` | yes |  |
| `interest_rate` | `float`, optional | no |  |
| `inflation_rate` | `float`, optional | no |  |
| `index` | `int` | yes |  |
| `guid` | `UUID`, optional | no |  |
