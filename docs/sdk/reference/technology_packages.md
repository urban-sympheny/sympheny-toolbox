<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/technologies.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Technology packages

Operations on technology packages. Available on the client as `client.technology_packages`.

## technology_packages.create { #method-technology_packages-create }

```python
async def create(
    scenario_guid: str,
    request: TechnologyPackageRequestDtoV2,
) -> TechnologyPackageResponseDtoV2
```

Create a technology package in a scenario.

REST operation: [`POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages`](../../api/reference/technology-packages.md#operation-specifyTechnologyPackageV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`TechnologyPackageRequestDtoV2`](models/technologies.md#model-TechnologyPackageRequestDtoV2) | yes | Request body. |

**Returns:** [`TechnologyPackageResponseDtoV2`](models/technologies.md#model-TechnologyPackageResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        package = await client.technology_packages.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        package = client.technology_packages.create(scenario_guid, request)
    ```

## technology_packages.list { #method-technology_packages-list }

```python
async def list(scenario_guid: str) -> TechnologyPackageListResponseDtoV2
```

List the technology packages of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages`](../../api/reference/technology-packages.md#operation-getAllTechnologyPackagesByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** [`TechnologyPackageListResponseDtoV2`](models/technologies.md#model-TechnologyPackageListResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        packages = await client.technology_packages.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        packages = client.technology_packages.list(scenario_guid)
    ```

## technology_packages.get { #method-technology_packages-get }

```python
async def get(scenario_guid: str, package_guid: str) -> TechnologyPackageResponseDtoV2
```

Get technology package details.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/technology-packages/{guid}`](../../api/reference/technology-packages.md#operation-getTechnologyPackageByGuidV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `package_guid` | `str` | yes | GUID of the package. |

**Returns:** [`TechnologyPackageResponseDtoV2`](models/technologies.md#model-TechnologyPackageResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        package = await client.technology_packages.get(scenario_guid, package_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        package = client.technology_packages.get(scenario_guid, package_guid)
    ```

## technology_packages.update { #method-technology_packages-update }

```python
async def update(
    scenario_guid: str,
    package_guid: str,
    request: TechnologyPackageResponseDtoV2,
) -> TechnologyPackageResponseDtoV2
```

Update a technology package.

REST operation: [`PUT /sympheny-app/v2_1/scenarios/{scenarioGuid}/technology-packages/{guid}`](../../api/reference/technology-packages.md#operation-updateTechnologyPackageV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `package_guid` | `str` | yes | GUID of the package. |
| `request` | [`TechnologyPackageResponseDtoV2`](models/technologies.md#model-TechnologyPackageResponseDtoV2) | yes | Request body. |

**Returns:** [`TechnologyPackageResponseDtoV2`](models/technologies.md#model-TechnologyPackageResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        package = await client.technology_packages.update(scenario_guid, package_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        package = client.technology_packages.update(scenario_guid, package_guid, request)
    ```

## technology_packages.delete { #method-technology_packages-delete }

```python
async def delete(
    scenario_guid: str,
    package_guid: str,
    *,
    delete_techs: bool | None = None,
) -> TechnologyPackageListResponseDto
```

Delete a technology package.

REST operation: [`DELETE /sympheny-app/scenarios/{scenarioGuid}/technology-packages/{guid}`](../../api/reference/technology-packages.md#operation-deleteTechnologyPackage)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `package_guid` | `str` | yes | GUID of the package. |
| `delete_techs` | `bool`, optional | no | Also delete the technologies contained in the package. |

**Returns:** [`TechnologyPackageListResponseDto`](models/technologies.md#model-TechnologyPackageListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        status = await client.technology_packages.delete(scenario_guid, package_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        status = client.technology_packages.delete(scenario_guid, package_guid)
    ```
