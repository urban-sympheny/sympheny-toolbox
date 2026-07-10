---
tags:
  - web-app
  - concepts
---

# Optimization model

Sympheny models an energy system as a network of hubs connected by energy flows. The
optimizer decides which technologies to install, how to operate them, and how energy
moves between hubs and over time, to meet demand at the lowest cost (or another
objective you choose) across one or more stages.

This section explains the concepts you'll configure when building a scenario, and the
methodology behind the optimizer.

## Core building blocks

- [Stages](stages.md) — the phases of investment and operation in a project's lifetime.
- [Hubs](hubs.md) — the geographic areas or sites in your project.
- [Energy carriers](energy-carriers.md) — the substances or media that carry energy
  through the system.
- [Energy demands](energy-demands.md) — the energy use that the system must satisfy.
- [Imports](imports.md) — energy purchased from outside the system.
- [Exports](exports.md) — energy sold or sent outside the system.
- [On-site resources](on-site-resources.md) — intermittent renewable resources
  available on site.
- [Conversion technologies](conversion-technologies.md) — systems that transform one
  energy carrier into another.
- [Storage technologies](storage-technologies.md) — systems that store energy for
  later use.
- [Technology packages](technology-packages.md) — bundles of technologies considered
  together.
- [Network technologies](network-technologies.md) — connections that move energy
  between hubs.
- [Intra-hub networks](intra-hub-networks.md) — connections that move energy within a
  hub.

## Methodology

- [Clustered profiles](clustered-profiles.md) — how Sympheny reduces solving time by
  clustering hourly profiles into typical days.
- [Demand profiles methodology](demand-profiles-methodology.md) — how Sympheny's
  built-in demand profiles are generated.
- [Discounted cash flow analysis](discounted-cash-flow-analysis.md) — how Sympheny
  converts future cash flows into present value.
- [Capital recovery factor](capital-recovery-factor.md) — how Sympheny converts total
  cost into an equivalent annual cost.

## Reference

- [Glossary](glossary.md) — definitions of terms used throughout the model.
- [Parameters](parameters/index.md) — the full list of input and output parameters for
  each concept.
