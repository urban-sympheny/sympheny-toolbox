---
tags:
  - web-app
  - how-to
---

# EnyTool

Sympheny EnyTool is a software package that provides direct access to services and data from the Sympheny ecosystem. It connects with tools and datasets developed by:

- Sympheny partners
- Research projects
- Open-source tools and public data platforms

This integration lets planners, researchers, and decision-makers access consistent, high-quality data and services for building, district, and city-scale energy planning.

EnyTool acts as a gateway, linking simulation, optimization, and data layers across partners such as GeoImpact, Esri, Gilytics, Empa, Planeto, Ramp, JRC Solar, and [geo.admin.ch](https://www.geo.admin.ch/) (GWR).

## Ecosystem overview

| Partner / source | Type | Main contribution / service | Example use in EnyTool | Website |
| --- | --- | --- | --- | --- |
| Esri | Commercial partner | GIS and spatial analytics (ArcGIS platform) | Mapping, geospatial data integration | [esri.com](https://www.esri.com/) |
| GeoImpact | Partner / data provider | Swiss building energy & geospatial database | Access building data, retrofit potential, local energy insights | [geoimpact.ch](https://www.geoimpact.ch/) |
| Gilytics | Partner / infrastructure planning | Cloud GIS for infrastructure routing & siting | Network routing, cable/pipe siting in energy scenarios | [gilytics.com](https://gilytics.com/) |
| Empa | R&D partner | Research & development in digital twins, energy systems | Integration of R&D data models (for example, Digicities, GOES) | [empa.ch](https://www.empa.ch/) |
| Planeto SA | Partner / software platform | District heating & cooling network design | Scenario generation for thermal networks | [planeto-energy.ch](https://planeto-energy.ch/) |
| Ramp | Open-source tool | Synthetic multi-energy demand generation | Generate demand profiles where measured data is missing | [rampdemand.org](https://rampdemand.org/) |
| Ramp Mobility | Open-source extension | Mobility & EV demand modelling | Integrate EV loads and transport demand | [rampdemand.org/mobility](https://rampdemand.org/) |
| JRC Solar (PVGIS) | Open data / research | Solar irradiation & PV potential data | Assess renewable generation potential | [joint-research-centre.ec.europa.eu](https://joint-research-centre.ec.europa.eu/) |
| GeoAdmin (GWR data) | Open government data | Swiss federal geo & building data | Geospatial base data for Swiss projects | [data.geo.admin.ch](https://data.geo.admin.ch/) |

## EnyTool resource architecture

EnyTool integrates external services through standardized API connections and data connectors. These resources fall into three categories:

### Data resources

- **GeoImpact**: building energy and geospatial data (Switzerland)
- **GeoAdmin / GWR**: official geodata, cadastral and building registers
- **JRC Solar**: European solar potential datasets

### Modelling & simulation tools

- **Ramp / Ramp Mobility**: energy and mobility demand generation. See [RAMP tool suite](ramp-tool-suite.md).
- **Planeto**: district heating & cooling network simulation
- **Gilytics**: energy infrastructure routing and optimization

### Research & GIS frameworks

- **Esri (ArcGIS)**: mapping and geospatial layer integration
- **Empa**: research collaboration (for example, Digicities, GOES) for digital twin data exchange

## Use cases

| Use case | Involved services | Description |
| --- | --- | --- |
| Building energy retrofit planning | GeoImpact, GeoAdmin, Ramp | Combine building data with synthetic energy demand to identify retrofit potential |
| District heating network design | Planeto, GeoImpact, GeoAdmin | Use building data and network simulation to optimize district systems |
| Mobility integration in energy planning | Ramp Mobility, Gilytics | Model EV charging demand and assess grid or infrastructure impact |
| Solar potential assessment | JRC Solar, Esri | Use PVGIS data with spatial layers for renewable potential mapping |
| Digital twin research integration | Empa (Digicities, GOES) | Apply Empa-developed semantic and digital twin data models |
