---
tags:
  - web-app
  - concepts
---

# Network technologies

![Network technologies](img/network-technologies-1.png)

Networks transport energy between [hubs](hubs.md). For example, a network may represent a section of a district heating network. They are modelled in two parts:

- **Network technology**: Defines the kind of energy transported, costs and embodied emissions.
- **Network link**: Defines the length, capacity, losses and connected hubs of a single network segment.

As for [conversion technologies](conversion-technologies.md), you can model multiple network link candidates and different network technologies and let Sympheny identify which are the better options. You can also specify the capacity, for example when modelling existing network links. The cost of a network link is a function of the network technology investment costs applied to the network link length and capacity.

You can draw network links on the map, where they will appear as dotted lines with the colour of their energy carrier.

![Network technologies](img/network-map.png)
