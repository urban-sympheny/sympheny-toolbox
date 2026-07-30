---
tags:
  - web-app
  - release-notes
---

# April 2024

**Exciting news: Sympheny's web app Version 3 is here!**

We are thrilled to announce the release of the latest version of our web app! This release is packed with exciting features and improvements that will enhance your experience and empower you to achieve even more with our platform.

Here are some highlights of what you can expect from this new release:

1. **Enhanced optimization engine**: Sense, the energy hub solver engine
2. **New multi-stage interface**
3. **New dashboard interface**

In addition to these new features, we have made several performance enhancements and bug fixes to ensure a smoother and more reliable user experience.

We have prepared detailed documentation and resources to help you familiarize yourself with the new features and get the most out of them. Our customer support team is also available to assist you with any questions or concerns you may have.

**What does this mean for you?**

- Existing projects:

  - Your current projects in Version 2 remain available with the known interface.
  - To upgrade an existing project into Version 3 to leverage its benefits, you have to actively migrate the project.
- New projects:

  - When creating a new project, you can currently choose whether to use the existing version (V2) or the new Version 3 (labeled as beta until 31 May). V2 will only receive bug fixes and no further development. We recommend adopting V3 for its ongoing support and access to all-new functionalities.
  - As of 1 June 2024, V3 is the default for any new project.

**Summary of timeline:**

- **29 April 2024**: V2 and V3 are available. You may migrate existing projects to V3 or continue working in the current V2 version.
- **17 June 2024**: V3 becomes the default version for new projects.
- **30 June 2024**: V2 is no longer supported.

**How can I learn more about Sympheny Version 3?**

- In June/July 2024, Sympheny hosted tutorials on the new version and its benefits. Contact us to register for specific training sessions.

**So what is new, and does it change the way we model?**

- The modeling and parameters remain the same. Additional features available in V3 are listed below.

## User experience

These new features are available for projects in both V2 (previous default version) and V3:

- Download input files for previously executed scenarios
- Compare multiple input files via API
- Satellite map layer

## New optimization engine: Sense (available as Sympheny V3)

The following new features are available for projects in V3:

- **User experience enhancements**

  - **Performance boost:** achieve up to 5x faster executions for a smoother user experience
  - **Infeasible model insights:** clearer infeasibility messages provide insight into model limitations
  - **Enhanced readability:** input and output Excel sheets are now more user-friendly
  - **Execution history:** access past executions effortlessly, with options to download or delete
  - **Hourly clustered profiles:** hourly profiles clustered from user input data are now available for reference
  - **Editable energy carriers:** personalize colors for energy carriers, reflected in the results dashboard for easier identification
- **Modeling multiple stages**

  - **Long-term planning:** multi-stage technology deployment enables strategic long-term planning
  - **Technology reusability:** deployed technologies can be reused across planning stages, optimizing resource utilization and cost-efficiency
  - **Cost considerations:** calculate replacement costs and salvage values, enhancing financial planning
- **Optimization objectives**

  - Choose from various new objectives including NPV, CAPEX, OPEX, import energy minimization, and more
- **New results dashboard**

  - **Usability enhancements:** navigate scenarios seamlessly, download high-resolution graphs, and access specific data effortlessly
  - **Interactive energy diagrams:** engage with dynamic energy diagrams for intuitive visualization
- **New modeling features**

  - **Imports and exports**

    - Allow multiple energy carriers per hub
    - Specify hourly max capacities, energy prices, and CO2 intensity
    - Support negative energy prices
  - **Demands**

    - Allow multiple energy carriers per hub
    - Define hourly demand sale prices
    - Enable reversing demand energy flow (energy extraction demand)
  - **On-site resources**

    - Allow multiple energy carriers per hub
  - **Conversion Technologies**

    - Specify multiple primary modes and outputs to make cost calculations and operational limits more flexible
    - Set design and operational parameters per mode
    - Define hourly efficiency, input shares, and allowed operation as a percentage of capacity
    - Specify peak power to allow technologies to operate above or below the design capacity
  - **Network Technologies**

    - Define maximum and minimum capacities per link
    - Specify hourly network losses
  - **Storage Technologies**

    - Specify hourly standby losses
    - Define variable O&M costs per total charging and discharging energy
- **Execution parameters**

  - Set maximum execution time per job
  - Control resolution of hourly clustered profiles
