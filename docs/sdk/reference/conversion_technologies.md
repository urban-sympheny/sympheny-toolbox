<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/technologies.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Conversion technologies

Operations on conversion technologies. Available on the client as `client.conversion_technologies`.

## conversion_technologies.create { #method-conversion_technologies-create }

```python
async def create(
    scenario_guid: str,
    request: ConversionTechnologyRequestDtoV2,
) -> ConversionTechnologyResponseDtoV2
```

Create a conversion technology in a scenario.

REST operation: [`POST /sympheny-app/v2_2/scenarios/{scenarioGuid}/conversion-technologies`](../../api/reference/conversion-technologies.md#operation-specifyConversionTechnologyV2_2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`ConversionTechnologyRequestDtoV2`](models/technologies.md#model-ConversionTechnologyRequestDtoV2) | yes | Request body. |

**Returns:** [`ConversionTechnologyResponseDtoV2`](models/technologies.md#model-ConversionTechnologyResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.conversion_technologies.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.conversion_technologies.create(scenario_guid, request)
    ```

## conversion_technologies.list { #method-conversion_technologies-list }

```python
async def list(scenario_guid: str) -> ConversionTechnologyListResponseDtoV2
```

List the conversion technologies of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/conversion-technologies`](../../api/reference/conversion-technologies.md#operation-getAllConversionTechnologiesByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`ConversionTechnologyListResponseDtoV2`](models/technologies.md#model-ConversionTechnologyListResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technologies = await client.conversion_technologies.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technologies = client.conversion_technologies.list(scenario_guid)
    ```

## conversion_technologies.get { #method-conversion_technologies-get }

```python
async def get(technology_guid: str) -> ConversionTechnologyDetailResponseDtoV2
```

Get conversion technology details.

REST operation: [`GET /sympheny-app/v2/scenarios/conversion-technologies/{guid}`](../../api/reference/conversion-technologies.md#operation-getConversionTechDetailsV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |

**Returns:** [`ConversionTechnologyDetailResponseDtoV2`](models/technologies.md#model-ConversionTechnologyDetailResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.conversion_technologies.get(technology_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.conversion_technologies.get(technology_guid)
    ```

## conversion_technologies.update { #method-conversion_technologies-update }

```python
async def update(
    technology_guid: str,
    request: ConversionTechnologyDetailResponseDtoV2,
) -> ConversionTechnologyResponseDtoV2
```

Update a conversion technology.

REST operation: [`PUT /sympheny-app/v2_1/scenarios/conversion-technologies/{guid}`](../../api/reference/conversion-technologies.md#operation-updateConversionTechnology)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |
| `request` | [`ConversionTechnologyDetailResponseDtoV2`](models/technologies.md#model-ConversionTechnologyDetailResponseDtoV2) | yes | Request body. |

**Returns:** [`ConversionTechnologyResponseDtoV2`](models/technologies.md#model-ConversionTechnologyResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        technology = await client.conversion_technologies.update(technology_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        technology = client.conversion_technologies.update(technology_guid, request)
    ```

## conversion_technologies.delete { #method-conversion_technologies-delete }

```python
async def delete(technology_guid: str) -> None
```

Delete a conversion technology.

REST operation: [`DELETE /sympheny-app/v2/scenarios/conversion-technologies/{guid}`](../../api/reference/conversion-technologies.md#operation-deleteConversionTechnologyV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `technology_guid` | `str` | yes | GUID of the technology. |

**Returns:** `None`

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        await client.conversion_technologies.delete(technology_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        client.conversion_technologies.delete(technology_guid)
    ```
