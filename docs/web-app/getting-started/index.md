---
tags:
  - web-app
  - getting-started
---

# Getting started

## What is Sympheny?

Sympheny is a toolset for integrated energy system planning, suitable for scales ranging from buildings to cities. You can model energy systems with basic site details, quickly evaluate various supply options, and identify the most suitable ones. Its dashboards provide in-depth insights into the technology and performance of each solution. You can also run multiple scenarios simultaneously, to understand the impact of factors like energy prices and site configurations.

![Sympheny web app overview](img/introduction-1.png)

## What makes it unique?

Sympheny supports you from initial data gathering to execution and detailed results, identifying optimal energy supply solutions with speed and precision. Advanced optimization algorithms analyze thousands of potential solutions, pinpointing the best options based on the planner's objectives. These algorithms solve energy balances for every hour of the year, considering complex site-specific supply and demand dynamics, interactions between various energy vectors, and the detailed techno-economic specifications of available technologies.

## What can Sympheny be used for?

The Sympheny web app can be used to identify the optimal energy supply solution for a given site or to assess the expected performance of user-defined supply solutions. You can use it to:

- **Optimize production technologies:** Determine the most suitable energy production technologies for a site, how they should be dimensioned, and whether to use a centralized, decentralized, or hybrid solution for heating and/or cooling.
- **Optimize renewables integration:** Assess the potential to cover on-site energy demands with on-site renewable energy sources (e.g., solar, groundwater heat) and identify the optimal mix of renewable resources and technologies for a site.
- **Optimize energy storage:** Identify the most suitable storage technologies for a site, evaluate the cost-effectiveness of batteries, and consider options for seasonal (e.g., geothermal) and hydrogen storage.
- **Optimize thermal networks:** Determine if a thermal network is viable, identify the most efficient network type (e.g., low-temperature, high-temperature), decide which buildings or sectors to connect, and choose the appropriate production technologies for heating or cooling the network.
- **Optimize grid interactions:** Decide which energy vectors to import based on cost and CO2 intensity, evaluate the possibility of operating the site autonomously from the electricity grid, and analyze peak electricity withdrawals and feed-ins.

Sympheny allows for the combination of these optimizations and more, providing a comprehensive tool for energy system planning.

## What can't Sympheny be used for?

- Building-level high-resolution optimization of sites larger than 15-20 buildings. Larger sites may require aggregation of buildings into nodes/hubs.
- Detailed hydraulic optimization of thermal networks or detailed optimization of electrical networks.
- Optimizing the control or operational management of energy systems.
- Sympheny is best suited for engineering problems in early phases of planning (SIA 1 and 2), but it can still be used as a digital twin, carried over to later planning stages.

## Where should I start?

The recommended starting point is the Example case, which is installed in every user's account upon first sign-in. From there, follow the steps below to sign in and complete your first walkthrough. Once you're familiar with the basics, explore the [how-to guides](../how-to/index.md) to learn the various features of the software and how to use them effectively.

1. [Sign up and log in](sign-up-and-login.md)
2. [Follow the quick start walkthrough](quickstart.md)

For programmatic access, see the [REST API documentation](../../api/index.md).

## What if I run into problems?

You can reach out to us for support via the Help button located at the bottom-right corner of our website, or drop us an email at [support@sympheny.com](mailto:support@sympheny.com). Additionally, feel free to check out our [Troubleshooting and FAQs](../troubleshooting/index.md) sections for handy solutions.
