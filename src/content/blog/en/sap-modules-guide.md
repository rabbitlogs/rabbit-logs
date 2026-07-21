---
title: "SAP's 10 core modules: the whole restaurant at a glance"
mapTitle: "SAP's 10 core modules"
description: "SAP's core modules (FI, CO, SD, MM, PP, QM, PM, PS, HR, LE) mapped to the different stations in a restaurant — floor, storeroom, kitchen, register, and more — explained for beginners."
pubDate: "2025-07-09"
category: "project"
series: "Learning SAP through a restaurant"
level: "beginner"
tags: ["SAPProjects", "SAPModules", "ERP", "SAPBasics"]
---

Hi, this is Rabbit! 🐰

In [SAP for beginners: the integrated brain behind a restaurant kitchen](/en/blog/sap-what-is-sap), we compared SAP to a "restaurant kitchen" and took a quick look at five core modules. I promised the rest would come in a separate post — today, I'm keeping that promise.

SAP's biggest defining trait is that it delivers functionality in blocks called "modules." Like Lego, you pick only the pieces you need and expand later without much trouble. Today, let's walk through 10 commonly used core modules and see which station of the restaurant each one maps to.

> **3-line summary**
> - SAP modules correspond to different stations in a restaurant — floor, storeroom, kitchen, accounting, and more.
> - The 10 core modules are FI, CO, SD, MM, PP, QM, PM, PS, HR, and LE.
> - The modules aren't isolated — they're connected as one, so an input in one place flows through the whole system.

[[TOC]]

## Modules are the "stations" of the kitchen

No single person runs a large restaurant alone. It splits into the floor that takes orders, the storeroom that manages ingredients, the kitchen that cooks, and the register that handles money — each covering its own specialty. SAP modules work exactly the same way. A company's work is divided by area, and each module owns one specialized station.

What matters is that these stations don't operate in isolation. Just as an order on the floor sets the kitchen moving and pulls ingredients from the storeroom, ==the input from one module automatically flows into the others.== That's exactly why SAP is called an "integrated" system.

## The 10 core modules at a glance

Here's the full picture in table form first.

| Abbreviation | Name | Role in the restaurant |
|---|---|---|
| SD | Sales and Distribution | Taking customer orders on the floor |
| MM | Materials Management | Purchasing ingredients, managing the storeroom |
| PP | Production Planning | Cooking in the kitchen |
| QM | Quality Management | Checking taste and hygiene |
| PM | Plant Maintenance | Inspecting and repairing kitchen equipment |
| LE | Logistics Execution | Serving and delivering the finished dish |
| CO | Controlling | Calculating cost per menu item |
| FI | Financial Accounting | The store's overall ledger |
| PS | Project System | Managing a new store opening as a project |
| HR | Human Resources | Hiring, payroll, attendance |

*Table 1. SAP's 10 core modules, mapped to a restaurant*

![Diagram of a restaurant kitchen layout showing SAP's 10 core modules connected around the central SAP system](/images/sap-modules-map.jpg)
*Figure 1. The 10 modules connect as one, centered on SAP*

Now let's go a bit deeper, station by station.

## The stations that greet the customer: SD, MM, PP

**SD** (Sales and Distribution) is the floor. It takes the customer's order, sets the price, and issues the bill. In business terms, this is where sales orders, quotes, shipments, and billing happen.

**MM** (Materials Management) is the storeroom and purchasing desk. It buys ingredients, manages inventory, and reorders when supplies run low. This module covers a company's purchasing, goods receipt, and inventory management.

**PP** (Production Planning) is the kitchen. It takes the order and the ingredients and turns them into an actual dish. Planning what to make, when, and how much, then issuing production instructions — this is the heart of manufacturing.

## Quality and equipment: QM, PM

**QM** (Quality Management) is the inspector responsible for taste and hygiene. It checks whether incoming ingredients are fresh and whether the finished dish meets standard. In a company, this covers incoming inspection, in-process inspection, and outgoing inspection.

**PM** (Plant Maintenance) is the technician who inspects and repairs kitchen equipment. Just as a broken oven means no cooking, stopped equipment means stopped production. This module covers equipment inspection, breakdown repair, and preventive maintenance.

## The stations that connect the flow and do the math: LE, CO, FI

**LE** (Logistics Execution) is the process of getting the finished dish out to the customer — pulling it from storage (picking), packaging it, and handling shipment and delivery.

**CO** (Controlling) is the station that works out cost per menu item — how much ingredients and labor cost for a given dish, and what margin is left. It handles internal cost management and the numbers behind business decisions.

**FI** (Financial Accounting) is the store's official, overall ledger. It produces the financial statements reported externally — revenue, expenses, taxes. If CO is "internal calculation," FI is "the official external record." The two are usually referred to together as "FICO."

## People and projects: HR, PS

**HR** (Human Resources) covers hiring staff, paying them, and managing attendance. Just as a good restaurant needs good staff, this module handles a company's people management. More recently, it's also referred to as HCM or [SuccessFactors](https://www.sap.com/products/hcm/what-is-sap-successfactors.html).

**PS** (Project System) manages "one-off big undertakings," like opening a new location. It ties together schedule, budget, and resources under a single project. This module sees especially heavy use in construction, engineering, and large-scale implementation projects.

## Rabbit's Takeaway

You don't need to memorize all 10. What matters is the picture: SAP divides a company's work into "stations of a kitchen," and those stations connect as one.

So it's enough to have a feel for the fact that touching one station ripples into the others. An order on the floor (SD) sets the kitchen (PP) moving, pulls ingredients from the storeroom (MM), and lands in the ledger (FI) — that connection is the essence of SAP. As we look at each station more closely going forward, this whole kitchen will come into sharper focus. 😎

**Read more**

- [SAP for beginners: the integrated brain behind a restaurant kitchen](/en/blog/sap-what-is-sap)

<!-- Related posts: prerequisite=sap-what-is-sap; related=; deepens= -->
