<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/energy.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Energy demands

Operations on energy demands. Available on the client as `client.energy_demands`.

## energy_demands.create { #method-energy_demands-create }

```python
async def create(scenario_guid: str, request: EnergyDemandRequestDtoV2) -> EnergyDemandResponseDtoV2
```

Create a new energy demand in a scenario.

REST operation: [`POST /sympheny-app/v2_1/scenarios/{scenarioGuid}/energy-demands`](../../api/reference/energy-demands.md#operation-uploadNewEnergyDemandProfileV2_1)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `request` | [`EnergyDemandRequestDtoV2`](models/energy.md#model-EnergyDemandRequestDtoV2) | yes | Request body. |

**Returns:** [`EnergyDemandResponseDtoV2`](models/energy.md#model-EnergyDemandResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        demand = await client.energy_demands.create(scenario_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        demand = client.energy_demands.create(scenario_guid, request)
    ```

## energy_demands.list { #method-energy_demands-list }

```python
async def list(scenario_guid: str) -> list[EnergyDemandResponseDtoV2]
```

List the energy demands of a scenario.

REST operation: [`GET /sympheny-app/v2/scenarios/{scenarioGuid}/energy-demands`](../../api/reference/energy-demands.md#operation-getAllEnergyDemandsByScenarioV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |

**Returns:** list of [`EnergyDemandResponseDtoV2`](models/energy.md#model-EnergyDemandResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        demands = await client.energy_demands.list(scenario_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        demands = client.energy_demands.list(scenario_guid)
    ```

## energy_demands.get { #method-energy_demands-get }

```python
async def get(
    demand_guid: str,
    *,
    scenario_variant_guid: str | None = None,
) -> EnergyDemandDetailResponseDtoV2
```

Get energy demand details.

REST operation: [`GET /sympheny-app/v2/energy-demands/{guid}`](../../api/reference/energy-demands.md#operation-getEnergyDemandDetailsByGuidV2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `demand_guid` | `str` | yes | GUID of the demand. |
| `scenario_variant_guid` | `str`, optional | no | GUID of the scenario variant to read from. |

**Returns:** [`EnergyDemandDetailResponseDtoV2`](models/energy.md#model-EnergyDemandDetailResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        demand = await client.energy_demands.get(demand_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        demand = client.energy_demands.get(demand_guid)
    ```

## energy_demands.update { #method-energy_demands-update }

```python
async def update(
    scenario_guid: str,
    demand_guid: str,
    request: EnergyDemandResponseDtoV2,
) -> EnergyDemandResponseDtoV2
```

Update an energy demand.

REST operation: [`PUT /sympheny-app/v2_2/scenarios/{scenarioGuid}/energy-demands/{demand-guid}`](../../api/reference/energy-demands.md#operation-updateEnergyDemandV2_2)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scenario_guid` | `str` | yes | GUID of the scenario. |
| `demand_guid` | `str` | yes | GUID of the demand. |
| `request` | [`EnergyDemandResponseDtoV2`](models/energy.md#model-EnergyDemandResponseDtoV2) | yes | Request body. |

**Returns:** [`EnergyDemandResponseDtoV2`](models/energy.md#model-EnergyDemandResponseDtoV2)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        demand = await client.energy_demands.update(scenario_guid, demand_guid, request)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        demand = client.energy_demands.update(scenario_guid, demand_guid, request)
    ```

## energy_demands.delete { #method-energy_demands-delete }

```python
async def delete(demand_guid: str) -> EnergyDemandListResponseDto
```

Delete an energy demand; returns the remaining demands.

REST operation: [`DELETE /sympheny-app/scenarios/energy-demands/{guid}`](../../api/reference/energy-demands.md#operation-deleteEnergyDemandProfile)

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `demand_guid` | `str` | yes | GUID of the demand. |

**Returns:** [`EnergyDemandListResponseDto`](models/energy.md#model-EnergyDemandListResponseDto)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        remaining = await client.energy_demands.delete(demand_guid)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        remaining = client.energy_demands.delete(demand_guid)
    ```
