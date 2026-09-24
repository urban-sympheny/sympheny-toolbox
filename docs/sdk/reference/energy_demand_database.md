<!-- GENERATED — do not edit by hand. Source: src/sympheny_toolbox/_async/energy_demand_database.py.
     Regenerate: .agents/skills/docs/SKILL.md → task regen-sdk-reference. -->

# Energy demand database

Operations on the energy demand database. Available on the client as `client.energy_demand_database`.

## energy_demand_database.list { #method-energy_demand_database-list }

```python
async def list() -> list[EnergyDemandDBResponse]
```

List the specific energy demands of the database.

REST operation: [`GET /sympheny-app/database-energy-demand-table`](../../api/reference/energy-demand-database.md#operation-getDatabaseEnergyDemandTable)

**Returns:** list of [`EnergyDemandDBResponse`](models/energy.md#model-EnergyDemandDBResponse)

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        entries = await client.energy_demand_database.list()
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        entries = client.energy_demand_database.list()
    ```

## energy_demand_database.calculate { #method-energy_demand_database-calculate }

```python
async def calculate(demand_type: DemandType, requests: list[EnergyDemandDBRequest]) -> list[float]
```

Calculate a demand profile from the database.

REST operation: [`POST /sympheny-app/database-energy-demand-profile/{demandType}/calculate`](../../api/reference/energy-demand-database.md#operation-getDatabaseEnergyProfile)

Each request needs `area_m2` or `annual_kwh`.

**Parameters**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `demand_type` | [`DemandType`](models/energy.md#model-DemandType) | yes | Demand type of the profile. |
| `requests` | list of [`EnergyDemandDBRequest`](models/energy.md#model-EnergyDemandDBRequest) | yes | Request body. |

**Returns:** list of `float`, the demand profile.

=== "Async"

    ```python
    async with AsyncSympheny(username, password) as client:
        profile = await client.energy_demand_database.calculate(DemandType.space_heating, requests)
    ```

=== "Sync"

    ```python
    with Sympheny(username, password) as client:
        profile = client.energy_demand_database.calculate(DemandType.space_heating, requests)
    ```
