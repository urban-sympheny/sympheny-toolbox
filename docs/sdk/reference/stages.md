<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/scenarios.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Stages

Operations on stages. Available on the client as `client.stages`.

## stages.list { #method-stages-list }

```python
async def list(scenario_guid: str) -> list[StageResponseDto]
```

List the stages of a scenario.

REST operation: [`GET /sympheny-app/scenarios/{scenarioGuid}/stages`](../../api/reference/stages.md#operation-list)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** list of [`StageResponseDto`](models/scenarios.md#model-StageResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        stages = await client.stages.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        stages = client.stages.list(scenario_guid)
    ```

## stages.create { #method-stages-create }

```python
async def create(scenario_guid: str, request: StageRequestDto) -> StageResponseDto
```

Create a new stage in a scenario.

REST operation: [`POST /sympheny-app/scenarios/{scenarioGuid}/stages`](../../api/reference/stages.md#operation-create)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`StageRequestDto`](models/scenarios.md#model-StageRequestDto) | yes | Request body. |

**Returns:** [`StageResponseDto`](models/scenarios.md#model-StageResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        stage = await client.stages.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        stage = client.stages.create(scenario_guid, request)
    ```

## stages.get { #method-stages-get }

```python
async def get(stage_guid: str) -> StageResponseDto
```

Get stage details.

REST operation: [`GET /sympheny-app/scenarios/stages/{guid}`](../../api/reference/stages.md#operation-get_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `stage_guid` | `str` | yes | GUID of the stage. |

**Returns:** [`StageResponseDto`](models/scenarios.md#model-StageResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        stage = await client.stages.get(stage_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        stage = client.stages.get(stage_guid)
    ```

## stages.update { #method-stages-update }

```python
async def update(scenario_guid: str, stage_guid: str, request: StageResponseDto) -> StageResponseDto
```

Update a stage.

REST operation: [`PUT /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}`](../../api/reference/stages.md#operation-update)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `stage_guid` | `str` | yes | GUID of the stage. |
| `request` | [`StageResponseDto`](models/scenarios.md#model-StageResponseDto) | yes | Request body. |

**Returns:** [`StageResponseDto`](models/scenarios.md#model-StageResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        stage = await client.stages.update(scenario_guid, stage_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        stage = client.stages.update(scenario_guid, stage_guid, request)
    ```

## stages.delete { #method-stages-delete }

```python
async def delete(scenario_guid: str, stage_guid: str) -> None
```

Delete a stage.

REST operation: [`DELETE /sympheny-app/scenarios/{scenarioGuid}/stages/{stageGuid}`](../../api/reference/stages.md#operation-delete)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `stage_guid` | `str` | yes | GUID of the stage. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.stages.delete(scenario_guid, stage_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.stages.delete(scenario_guid, stage_guid)
    ```
