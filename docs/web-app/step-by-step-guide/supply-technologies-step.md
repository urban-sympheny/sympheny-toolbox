---
tags:
  - web-app
  - how-to
---

# Supply technologies step

In this step you define the technology candidates the optimizer can install: conversion technologies that turn one energy carrier into another, and storage technologies that hold an energy carrier for later use.

![Supply technologies step in the scenario editor](img/supply-technologies-step-1.png)

## Conversion technologies

There are two ways to add a conversion technology candidate to your scenario: **Add from Database** and **Create Custom**. For background, see the [Conversion technologies](../concepts/conversion-technologies.md) concept page.

### Add from Database

In the dialog that appears, follow these steps:

1. Select the database to load your data from. In most cases, the options are:
   1. Sympheny Global database
   2. Organization database (linked to your organization)
   3. My User database (linked to your personal account)
2. Choose a technology category.
3. Select the specific technology you want to load into your scenario. Clicking a technology displays a summary of its key parameters (see figure below).

   ![Technology summary panel](img/supply-technologies-step-2.png)

4. Click **Select**. A window opens where you can view and further edit the technology model, with parameters from the database pre-filled into the corresponding fields.
5. Assign the technology to one or more hubs and stages in the **Optimization Options** section. This defines where and when the technology can be installed. Click **Add** at the bottom of the dialog to add the technology candidate to your scenario. It appears in the energy hub diagram at the bottom of the page.

   ![Optimization options and Add button](img/supply-technologies-step-3.png)

!!! tip
    You can also build a customized technology database for the Sympheny web app. See [Database Center](../advanced-workflows/database-center.md).

### Create Custom

Clicking **Create Custom** opens a dialog where you assign parameters for the specific technology. It's the same window as step 4 of **Add from Database**, but the fields aren't pre-filled with any values.

## Storage technologies

Storage technology candidates are the systems that store an energy carrier for later use, such as batteries or thermal storage. For background, see the [Storage technologies](../concepts/storage-technologies.md) concept page.

!!! info "Coming soon"
    A step-by-step guide for this part of the step is in preparation.
