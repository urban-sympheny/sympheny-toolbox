---
tags:
  - web-app
  - getting-started
---

# Quick start

In this example, you simulate a **data center**. The goal is to walk you through your first steps in the Sympheny web app, covering the mandatory features and some *optional* ones along the way. In the following steps you:

- Create a scenario to size a solar PV installation.
- Evaluate the cost and performance of a 100 kWh battery.

## Create a project

Specify the location by searching for an address.

![Creating a project by searching for its address](img/quick-start-1.png)

## Create a scenario

Analyses can be used as an archive: create different scenarios to compare against each other. Click a scenario to work with it.

Optional, while creating the project:

- Send a copy of the project to, or share the project with, other Sympheny users.
- Upload an image to illustrate your project, using a low-resolution image.

![Creating a scenario within a project](img/quick-start-2.png)

## General

You can change the currency; press **Save** after changing it. Add a stage. Multiple stages can be used to plan an optimal energy system over decades, although this adds complexity to the modeling process. To get started on a project, simulate a single stage. An interest rate of 0% will help you interpret the results as a new user.

![General scenario settings, including currency and stages](img/quick-start-3.png)

## Hubs

Click **Add new** to add a hub. Multiple hubs are used to simulate energy networks, such as district heating. More hubs add complexity, so to get started, simulate a single hub.

Optional, while adding a hub:

- Research the hub's location by address.
- Change the map overlay.
- Draw an outline of the building or group of buildings to illustrate and locate them. You can activate add-ons for extracting geodata from the map.

![Adding a hub and setting its location](img/quick-start-4.png)

You can skip ahead to **Supply Technologies**, where energy carriers will be defined automatically.

![Skipping ahead to the Supply Technologies step](img/quick-start-5.png)

## Supply technologies

Add a technology from the database.

![Adding a supply technology from the database](img/quick-start-6.png)

Select a large solar field, since the price per kW will be lower. Once selected, information on the source is available.

![Selecting a large solar field technology](img/quick-start-7.png)

Click **Yes** to add the energy carriers.

![Confirming to add the associated energy carriers](img/quick-start-8.png)

You can edit all of the parameters of a technology from the database. Check **Primary Mode**. Every technology needs at least one primary mode. Multi-mode technologies can, for example, represent a reversible heat pump.

![Editing technology parameters and primary mode](img/quick-start-9.png)

The efficiency of this default solar PV is 18%, relative to the solar irradiance caught by the panels. Leave the sizing as **Optimize**, so Sympheny fixes the optimal size to reach the objective, usually minimum ROI.

![Setting solar PV efficiency and sizing to Optimize](img/quick-start-10.png)

Unit commitment parameters are advanced parameters used for specific industrial equipment. You can edit parameters related to investment cost, maintenance, and embedded emissions.

![Advanced unit commitment and cost parameters](img/quick-start-11.png)

Now that the technologies and associated energy carriers are created, head back to the **Energy Carriers** step.

![Returning to the Energy Carriers step](img/quick-start-12.png)

## Energy carriers

You can edit or create more energy carriers to distinguish all of the different energy flows. This example uses the defaults.

![Default energy carriers list](img/quick-start-13.png)

## Energy demands

In all sections, a map view represents hubs and networks. Close it to view the technology diagram below. This diagram is dynamic. For now, only the solar panels appear.

![Technology diagram with solar panels](img/quick-start-14.png)

Create a new **Energy Demand**. Select the energy carrier; you can edit the name. Try generating a profile for a data center using the available profiles.

![Creating a new energy demand](img/quick-start-15.png)

Even if there is no profile called "datacenter," you can explore the available building profiles and see if Industry Warehouse fits the project's needs.

![Browsing available building profiles](img/quick-start-16.png)

In this case, you have the annual electricity consumption, and can specify 1.2 GWh/year.

![Specifying annual electricity consumption](img/quick-start-17.png)

Information on the source of the profile is displayed.

![Profile source information](img/quick-start-18.png)

Save and close to add the profile.

![Saving the energy demand profile](img/quick-start-19.png)

This button lets you view the profile you generated.

![Button to view the generated profile](img/quick-start-20.png)

This is the resulting hourly profile. You can see large drops in consumption over weekends. You can download and edit the profile and re-upload it. You can also use the Sympheny peak shaving function.

![Hourly energy demand profile showing weekend drops](img/quick-start-21.png)

To upload a custom profile, edit the energy demand.

![Editing an energy demand to upload a custom profile](img/quick-start-22.png)

Select upload profile. The info button describes the format, and downloading the profile also reveals the format template.

![Uploading a custom profile with format template](img/quick-start-23.png)

An hourly profile is an XLSX file with 8760 values in kW.

![Example hourly profile spreadsheet with 8760 values](img/quick-start-24.png)

The uploaded profile better represents the electricity demand of a data center.

![Energy demand using the uploaded custom profile](img/quick-start-25.png)

## On-site resources

In this section you generate the hourly profile of the irradiance hitting the solar panels.

![The on-site resources step](img/quick-start-26.png)

Select the energy carrier; you can edit the name. Set 10,000 m² of available solar-panel surface and generate the profile from a location, inclination, and orientation combination in the database. This is the *maximum* available surface. Sympheny chooses the optimal size relative to the electricity consumption, price, and resale value. You can also generate the hourly solar profile for any location, orientation, and inclination combination using the **Add from map** workflow.

![Setting the available solar surface and generating a profile](img/quick-start-27.png)

This example uses Geneva, roof-mounted, at 15° facing east.

![Selecting location, inclination, and orientation](img/quick-start-28.png)

This is the resulting hourly solar-irradiance profile, per m².

![Resulting hourly solar irradiance profile](img/quick-start-29.png)

The energy diagram updates to include the on-site resource.

![Energy diagram updated with the on-site resource](img/quick-start-30.png)

## Imports and exports

You still need to add the electric grid. Otherwise there is a deficit of electricity at night, and a daytime surplus may limit the size of the solar field.

![The imports and exports step](img/quick-start-31.png)

Add the option to purchase electricity from the grid and set the electricity price.

![Adding a grid import and its price](img/quick-start-32.png)

Adding a capacity price and a CO₂-emissions value per kWh is optional but recommended.

![Optional capacity price and CO2 emissions per kWh](img/quick-start-33.png)

Also add an export, with a revenue of 0.08 EUR/kWh.

![Adding an electricity export](img/quick-start-34.png)

![Setting the export revenue value](img/quick-start-35.png)

## Review the energy diagram

Before executing the model, review the energy diagram. Confirm that every technology and link is fully connected, with no dead ends.

![Fully connected energy diagram before execution](img/quick-start-36.png)

## Execute the scenario

Give the execution a name. The **Updated** indicator means the scenario has changed since it was last executed. By default Sympheny generates two solutions: Solution 1 minimizes total cost (operating + maintenance + annualized investment costs); Solution 2 minimizes CO₂ emissions.

![Naming an execution and its two default solutions](img/quick-start-37.png)

Execution takes a few seconds. Open the interactive dashboard to review the results. You can also explore the input file (all parameters) and the output files (all results). Both are Excel files.

![Opening the interactive results dashboard](img/quick-start-38.png)

## Review the results

First, select **All stages** to view the Pareto front.

![Selecting All stages to view the Pareto front](img/quick-start-39.png)

The Pareto front shows Solutions 1 and 2, with the total cost and emissions of each.

![Pareto front comparing the two solutions](img/quick-start-40.png)

Select Solution 1, the stage, and the hub to view the detailed solution.

![Selecting a solution, stage, and hub](img/quick-start-41.png)

The Sankey diagram shows every energy flow in kWh. As with all diagrams, you can filter its content and download the data and images. A Sankey is also available for each month.

![Sankey diagram of the energy flows](img/quick-start-42.png)

The energy diagram shows the capacity of each technology, along with each technology's investment. Here the optimal PV field is 1,760 kW of electric output. Use the navigation bar at the top to return to the scenarios.

![Energy diagram with optimized technology capacities](img/quick-start-43.png)

## Evaluate a 100 kWh battery

Copy the scenario you just created to add one with a battery.

![Copying the scenario](img/quick-start-44.png)

![Confirming the scenario copy](img/quick-start-45.png)

In the new scenario every parameter is preserved, so you only need to add a battery.

![The copied scenario with parameters preserved](img/quick-start-46.png)

![Adding a battery storage technology](img/quick-start-47.png)

Set the battery to **Must install** and specify a capacity of 100 kWh. Sympheny respects this constraint while optimizing the battery's operation and the size of the solar field.

![Setting the battery to must-install at 100 kWh](img/quick-start-48.png)

Storage technologies expose a different set of parameters.

![Storage technology parameters](img/quick-start-49.png)

Once the battery is added, execute the scenario with the same objectives and view the results.

![Executing the scenario with the battery](img/quick-start-50.png)

Under **All stages**, the cost and emissions are slightly better with the battery.

![All-stages results improved by the battery](img/quick-start-51.png)

In the detailed results you can see the battery's hourly state of charge. This view is zoomed in on a single month.

![Hourly state of charge of the battery](img/quick-start-52.png)

## What's next?

Ready to model your own site? The [Step-by-step guide](../step-by-step-guide/index.md) walks through the whole process in detail: creating a project and an analysis, each of the eight scenario steps, running the optimization, and reading the results dashboard.
