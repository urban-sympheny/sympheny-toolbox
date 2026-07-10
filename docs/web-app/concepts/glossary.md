---
tags:
  - web-app
  - concepts
---

# Glossary

Short definitions of the terms used throughout the Sympheny optimization model.
Each term links to its concept page — read those for the full explanation and
parameters.

| Term | Definition | Read more |
| --- | --- | --- |
| Hub | A geographic area or site in your project — an individual building or a group of buildings treated as a single unit — for which you define demands, supply options, and connections. | [Hubs](hubs.md) |
| Energy carrier | Any substance or medium that contains energy and can be converted, stored, or delivered — a fuel, electricity, thermal energy, solar irradiance, and so on. | [Energy carriers](energy-carriers.md) |
| Energy demand | An hourly profile (8,760 values, in kWh) of energy use that the system must satisfy at every time step. | [Energy demands](energy-demands.md) |
| Stage | A phase of investment and operation in a project's lifetime; technologies can be installed at a stage's start and reused or salvaged at its end. | [Stages](stages.md) |
| Import | Energy purchased from outside the system, such as grid electricity or natural gas. | [Imports](imports.md) |
| Export | Energy sold or sent outside the system. | [Exports](exports.md) |
| On-site resource | A renewable resource with intermittent availability — such as solar irradiance or wind — described by an hourly profile. | [On-site resources](on-site-resources.md) |
| Conversion technology | A system that transforms one or more energy carriers into different ones — for example, a gas boiler converting natural gas to heat. | [Conversion technologies](conversion-technologies.md) |
| Storage technology | A system that stores energy for later use. | [Storage technologies](storage-technologies.md) |
| Network technology | A connection that moves energy between hubs. | [Network technologies](network-technologies.md) |
| Technology package | A bundle of technologies considered together in the optimization. | [Technology packages](technology-packages.md) |
| Intra-hub network | A connection that moves energy within a single hub. | [Intra-hub networks](intra-hub-networks.md) |
| Clustered profiles | Machine-learning-generated representative days that stand in for the full year of hourly input data, reducing solving time while preserving hourly variation within each day. | [Clustered profiles](clustered-profiles.md) |
| Discounted cash flow (DCF) analysis | The method Sympheny uses to convert expected future cash flows into present value, accounting for the cost of capital, loan structures, and risk premiums. | [Discounted cash flow analysis](discounted-cash-flow-analysis.md) |
| Capital recovery factor (CRF) | The factor Sympheny uses to convert a present cost into an equivalent annual cost, making investments with different lifespans comparable. | [Capital recovery factor](capital-recovery-factor.md) |

For the full list of input and output parameters for each concept, see
[Parameters](parameters/index.md).
