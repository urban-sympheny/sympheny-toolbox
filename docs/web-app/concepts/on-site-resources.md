---
tags:
  - web-app
  - concepts
---

# On-site resources

![On-site resources step in the scenario editor](../step-by-step-guide/img/on-site-resources-step-1.png)

On-site resources are renewable resources with intermittent (temporally varying) availability. In Sympheny, you can quickly generate solar irradiance profiles and wind profiles of 8,760 time steps using several methods.

On-site resources are functionally identical to imports, with fewer available parameters. For resources with constant availability, like geothermal energy or air used in a heat pump, create an import with a fixed maximum capacity (kW) and without an energy price (CHF/kWh), instead of creating an on-site resource.

Energy produced from on-site resources can be curtailed. Curtailment occurs when the available on-site resource leads to more energy than is needed to meet demand and exports (see the diagram below) at any given time.

![Curtailment of on-site resource production above demand and export](img/on-site-resources-curtailment.png)
