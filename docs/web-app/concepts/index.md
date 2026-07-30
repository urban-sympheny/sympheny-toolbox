---
tags:
  - web-app
  - concepts
---

# Concepts

Sympheny models an energy system as a network of hubs connected by energy flows. The optimizer decides which technologies to install, how to operate them, and how energy moves between hubs and over time, to meet demand at the lowest cost (or another objective you choose) across one or more stages.

This section explains the concepts you'll configure when building a scenario, and the methodology behind the optimizer. The first table below lists the concepts that are specific to Sympheny: the building blocks you create and configure in the scenario editor. The second table lists general concepts and methodological terms used within Sympheny: the established methods the optimizer applies to your model rather than things you build yourself.

## Sympheny concepts

| Term | Definition | Read more |
| --- | --- | --- |
| Hub | A geographic area that can be defined on the map. It can represent a single building, a group of buildings, an entire area, or a network node. Every hub has one energy system. Multiple hubs may be connected to each other using networks. | [Hubs](hubs.md) |
| Energy carrier | Any substance or medium that contains energy and can be converted, stored, or delivered: a fuel, electricity, thermal energy, solar irradiance, and so on. | [Energy carriers](energy-carriers.md) |
| Energy demand | Energy use that the system must satisfy at every time step, like building heating or electricity consumption, represented by an hourly profile. | [Energy demands](energy-demands.md) |
| Stage | A phase of investment and operation in a project's lifetime. Technologies can be installed at the start of a stage and salvaged at the end of the stage, or reused in the next stage. | [Stages](stages.md) |
| Import | Energy purchased from outside the system, such as grid electricity or natural gas. | [Imports](imports.md) |
| Export | Energy sold or sent outside the system. | [Exports](exports.md) |
| On-site resource | A renewable resource with intermittent availability, such as solar irradiance or wind, represented by an hourly profile. | [On-site resources](on-site-resources.md) |
| Conversion technology | A system that transforms one or more energy carriers into different ones, for example a gas boiler converting natural gas to heat. | [Conversion technologies](conversion-technologies.md) |
| Storage technology | A technology that stores energy for later use, such as a battery. | [Storage technologies](storage-technologies.md) |
| Network technology | A technology that transports energy between two hubs. | [Network technologies](network-technologies.md) |
| Technology package | A bundle of technologies considered together in the optimization. | [Technology packages](technology-packages.md) |
| Intra-hub network | A network technology that transports energy within a hub. | [Intra-hub networks](intra-hub-networks.md) |

## General concepts and methodology

| Term | Definition | Read more |
| --- | --- | --- |
| Clustered profiles | Machine-learning-generated representative days that stand in for the full year of hourly input data, reducing solving time while preserving hourly variation within each day. | [Clustered profiles](clustered-profiles.md) |
| Demand profiles methodology | How the demand profiles shipped in the Sympheny database are generated, from the demand type, building use, and building age or standard, and which data sources each profile comes from. | [Demand profiles methodology](demand-profiles-methodology.md) |
| Discounted cash flow (DCF) analysis | The method Sympheny uses to convert expected future cash flows into present value, accounting for the cost of capital, loan structures, and risk premiums. | [Discounted cash flow analysis](discounted-cash-flow-analysis.md) |
| Capital recovery factor (CRF) | The factor Sympheny uses to convert a present cost into an equivalent annual cost, making investments with different lifespans comparable. | [Capital recovery factor](capital-recovery-factor.md) |

For the full list of input parameters, see [Parameters](../parameters/index.md).
