<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/energy.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Solar resources

Operations on solar on-site resources. Available on the client as `client.solar_resources`.

## solar_resources.create { #method-solar_resources-create }

```python
async def create(
    scenario_guid: str,
    request: SolarOnSiteResourceRequestDtoV2,
) -> SolarOnSiteResourceResponseDtoV2
```

Create a new solar on-site resource in a scenario.

REST operation: [`POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/solar-on-site-resource`](../../api/reference/solar-resources.md#operation-uploadNewSolarOnSiteResourceV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`SolarOnSiteResourceRequestDtoV2`](models/energy.md#model-SolarOnSiteResourceRequestDtoV2) | yes | Request body. |

**Returns:** [`SolarOnSiteResourceResponseDtoV2`](models/energy.md#model-SolarOnSiteResourceResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        resource = await client.solar_resources.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        resource = client.solar_resources.create(scenario_guid, request)
    ```

## solar_resources.list { #method-solar_resources-list }

```python
async def list(scenario_guid: str) -> list[SolarOnSiteResourceResponseDtoV2]
```

List the solar on-site resources of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/solar-on-site-resource`](../../api/reference/solar-resources.md#operation-getAllSolarOnSiteResourcesByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** list of [`SolarOnSiteResourceResponseDtoV2`](models/energy.md#model-SolarOnSiteResourceResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        resources = await client.solar_resources.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        resources = client.solar_resources.list(scenario_guid)
    ```

## solar_resources.get { #method-solar_resources-get }

```python
async def get(resource_guid: str) -> SolarOnSiteResourceResponseDtoV2
```

Get solar on-site resource details.

REST operation: [`GET /sympheny-app/v2/scenarios/solar-on-site-resource/{guid}`](../../api/reference/solar-resources.md#operation-getSolarOnSiteResourcesV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource_guid` | `str` | yes | GUID of the resource. |

**Returns:** [`SolarOnSiteResourceResponseDtoV2`](models/energy.md#model-SolarOnSiteResourceResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        resource = await client.solar_resources.get(resource_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        resource = client.solar_resources.get(resource_guid)
    ```

## solar_resources.update { #method-solar_resources-update }

```python
async def update(
    resource_guid: str,
    request: SolarOnSiteResourceResponseDtoV2,
) -> SolarOnSiteResourceResponseDtoV2
```

Update a solar on-site resource.

REST operation: [`PUT /sympheny-app/v2_2/scenarios/solar-on-site-resource/{guid}`](../../api/reference/solar-resources.md#operation-editSolarOnSiteResourceV2_2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource_guid` | `str` | yes | GUID of the resource. |
| `request` | [`SolarOnSiteResourceResponseDtoV2`](models/energy.md#model-SolarOnSiteResourceResponseDtoV2) | yes | Request body. |

**Returns:** [`SolarOnSiteResourceResponseDtoV2`](models/energy.md#model-SolarOnSiteResourceResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        resource = await client.solar_resources.update(resource_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        resource = client.solar_resources.update(resource_guid, request)
    ```

## solar_resources.delete { #method-solar_resources-delete }

```python
async def delete(resource_guid: str) -> SolarOnSiteResourceListResponseDto
```

Delete a solar on-site resource; returns the remaining resources.

REST operation: [`DELETE /sympheny-app/scenarios/solar-on-site-resource/{guid}`](../../api/reference/solar-resources.md#operation-deleteSolarOnSiteResource)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `resource_guid` | `str` | yes | GUID of the resource. |

**Returns:** [`SolarOnSiteResourceListResponseDto`](models/energy.md#model-SolarOnSiteResourceListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.solar_resources.delete(resource_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.solar_resources.delete(resource_guid)
    ```
