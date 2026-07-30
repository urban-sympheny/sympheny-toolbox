---
tags:
  - web-app
  - concepts
---

# Storage technologies

Storage technologies can store an energy carrier for later use. For example, batteries store electricity and a hot water buffer stores heat at a certain temperature level.

The capacity and operation of a storage technology are defined by these parameters:

- **Capacity**: the maximum amount of energy that can be accumulated, expressed in kWh
- **Discharge rate**: how fast the energy can be delivered, expressed in kW
- **State of charge (SoC)**: quantifies the remaining capacity available at a given time, expressed as a percentage of the capacity

Like [conversion technologies](conversion-technologies.md), each candidate is defined by technical, financial, and environmental parameters.

## Capacity

You can choose different sizing methods. The size of the storage technology is expressed in kWh:

- **Optimize capacity**: Sympheny finds the optimal capacity.
- **Minimum and Maximum capacity**: You can enter a minimum and/or maximum capacity bound.
- **Can be installed and Minimum capacity**: If a minimum capacity is specified and the default option ![Default option toggle](img/conversion-technologies-2.png) is toggled, the installed capacity can either be 0 or greater than the minimum.
- **Must be installed and Minimum capacity**: The capacity must be greater than or equal to the minimum capacity.
- **Specify capacity**: The installed capacity is fixed. If the default "can be installed" option is toggled, the capacity will be either 0 or the specified capacity.

!!! tip
    For more advanced users, specifying a minimum and maximum capacity is good practice and often reduces computation time.

## Maximum discharge rate

The discharge rate is modeled as a %/h of the capacity. For a 10 kWh battery, a discharge rate of 100%/h means the battery can deliver 100% of its capacity in one hour, equivalent to a power of 10 kW.

## Efficiency

Losses can occur continuously or during charging and discharging. Standby losses are applied every hour relative to the state of charge. Charging and discharging losses are applied as a percentage of charge and discharge.

The minimum SoC (State of Charge) limits how much the storage can be discharged, effectively reducing the available capacity.

## Costs and CO2

The installed capacity is used to calculate the investment, maintenance costs, and embodied emissions.
