---
tags:
  - web-app
  - concepts
---

# Conversion technologies

| Parameter | Definition | Unit | Default |
| --- | --- | --- | --- |
| Technology Name | The name of the technology; must be unique within the scenario. | n/a | n/a |
| Virtual Technology | A virtual technology is a technology used purely for accounting purposes in the optimisation. It converts one energy carrier to another at zero cost and with 100% efficiency. If set to true, the efficiency, costs, and other values are automatically fixed to these values. | n/a | n/a |
| Stages | List of stages where the installation and operation of this technology are permitted. | n/a | n/a |
| Hubs | List of hubs where the installation and operation of this technology are permitted. | n/a | n/a |
| Installation Options | These options are mutually exclusive, meaning only one can be selected at a time. Options: Can be installed, Must be installed, Must be installed in at least one hub. | n/a | Can be installed |
| Primary Modes | At least one primary mode must be selected. The primary modes of a technology define which modes are used to calculate costs that depend on capacity. | n/a | n/a |
| Seasonal & Hourly Operation | Specifies the allowed seasons for the technology's operation. If hourly operation is selected, you can upload a profile of the maximum operation of the mode in each hour, as a percentage of installed capacity (multiplied by peak power). Allowed values: 0% to 100%. In an hour where allowed operation × peak power is below the minimum part load, the mode is off. If no hour of the profile can reach the minimum part load, the scenario is rejected (a profile that is 0 in every hour is allowed and switches the mode off). | % (profile values) | n/a |
| Input Energy Carriers | The input energy carriers of a technology mode; you can select multiple. | n/a | n/a |
| Output Energy Carriers | The output energy carriers of a technology mode; you can select multiple. | n/a | n/a |
| Input EC Share | For multi-input technologies, defines the ratio between inputs, representing the share of energy contributed by each energy carrier (EC). Values are absolute and can exceed 100. | n/a | n/a |
| Output EC Efficiency | The conversion efficiency for producing a specific energy carrier in a mode relative to total inputs. | % | n/a |
| Primary Output | Each technology mode must have a primary output energy carrier defining the mode's capacity for capacity-dependent cost calculations. | n/a | n/a |
| Technology Capacity | Select whether to optimize capacity or specify capacity manually. | n/a | n/a |
| Capacity | The fixed installed capacity of the mode; visible only if Specify Capacity is selected. Applies to primary and non-primary modes. For primary modes, also sets the technology capacity bounds (see [Technology capacity](../concepts/conversion-technologies.md#technology-capacity)). | kW | n/a |
| Maximum Capacity | The upper bound of the mode's installed capacity; visible only if the Optimize option is selected. Applies to primary and non-primary modes. For primary modes, also sets the technology capacity bounds (see [Technology capacity](../concepts/conversion-technologies.md#technology-capacity)). | kW | n/a |
| Minimum Capacity | The lower bound of the mode's installed capacity; visible only if the Optimize option is selected. Applies to primary and non-primary modes. For primary modes, also sets the technology capacity bounds (see [Technology capacity](../concepts/conversion-technologies.md#technology-capacity)). | kW | n/a |
| Maximum Annual Output | The maximum allowable annual energy output of the technology mode, determined by primary output energy carriers. | kWh/year | n/a |
| Minimum Annual Output | The minimum allowable annual energy output of the technology mode, determined by primary output energy carriers. | kWh/year | n/a |
| Curtailment Limitation | The percentage of the mode's installed capacity that cannot be curtailed in any hour. For example, 100% means no curtailment is possible; 90% allows curtailing up to 10% of the installed capacity per hour. | % | 100% |
| Peak Power | Ratio of the maximum output to the installed (paid) capacity. A peak power of 1.2 lets a 100 kW mode produce up to 120 kW without increasing its installed capacity or costs. Allowed values: 0.1 to 10. | kWmax/kW | 1 |
| Minimum Part Load | If greater than 0%, the mode's lower operational limit when running, as a percentage of the mode's installed capacity. Output plus curtailment must be at least this value in every hour the mode runs; otherwise the mode is off. The limit is independent of the peak power ratio, so it may not exceed peak power × 100%. Allowed values: 0% to 100%. If a minimum up or down time is set without a minimum part load, a minimum part load of 1% applies. | % | n/a |
| Minimum Up Time | Constrains the mode to remain operational for a minimum number of hours once started. | Hours | n/a |
| Minimum Down Time | Constrains the mode to remain non-operational for a minimum number of hours once shut down. | Hours | n/a |
| Simultaneous Operation | If False, prevents this mode from operating simultaneously with other modes within this technology. | n/a | True |
| Lifetime | The technical lifetime of the technology in years, used for calculating replacement costs and salvage value. | Years | n/a |
| Fixed Investment Cost | Fixed investment costs incurred upon installation regardless of size. | Currency | n/a |
| Variable Investment Cost | Variable investment costs per kW of installed capacity, determined by primary output energy carriers of primary modes. | Currency/kW | n/a |
| Fixed O&M Cost | Fixed operation and maintenance costs incurred annually. | Currency/year | n/a |
| Variable O&M Cost | Variable operation and maintenance costs incurred annually, based on: percentage of total investment, per installed kW, or per total production. | %/year, Currency/kW/year, Currency/kWh/year | n/a |
| Fixed Replacement Cost | Fixed replacement costs incurred when the technology is replaced at end of technical lifetime, regardless of size. | Currency/year | n/a |
| Variable Replacement Cost | Variable replacement costs incurred when the technology is replaced at end of lifetime, based on percentage of total investment or per installed kW. | %, Currency/kW | n/a |
| Fixed Salvage Value | Fixed salvage value incurred when the technology is salvaged at end of an investment stage, regardless of size. | Currency/year | n/a |
| Variable Salvage Value | Variable salvage value incurred when the technology is salvaged at end of an investment stage, based on percentage of total investment or per installed kW. | %, Currency/kW | n/a |
| Fixed Embodied CO2 | Fixed embodied CO2 emitted when the technology is installed, regardless of size. | kg-CO2 | n/a |
| Variable Embodied CO2 | Variable embodied CO2 emitted, based on installed kW or total production. | kg-CO2/kW, kg-CO2/kWh/year | n/a |
| Variable Captured CO2 | CO2 captured during operation, expressed per kWh of total input energy carrier of primary modes. | kg-CO2/kWh/year | n/a |

Certain **advanced parameters** are not available to users on all plans, but can be added through our add-on options. Contact our customer support team for a demo and to discuss how we could customise these options to your needs.
