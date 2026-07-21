---
title: "SAP WIP: the value of a dish that hasn't hit the plate yet"
mapTitle: "SAP WIP"
description: "Why work-in-progress (WIP) matters from a production, cost, and inventory perspective, explained through the lens of a dish still cooking, from the vantage point of three different experts."
pubDate: "2026-02-26"
category: "operations"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPOperations", "WIP", "WorkInProgress", "CostManagement"]
---

Hi, this is Rabbit! 🐰

Picture a pot of stew simmering away in the kitchen. It isn't a finished dish yet, but it's not just a pile of raw ingredients either. The accounting concept that captures this "in the middle of being made" state is called **WIP** (Work In Progress).

Today, let's untangle WIP — a concept a lot of people find confusing — through the lens of a dish still cooking, and look at why it matters from three angles: production, cost, and inventory.

> **3-line summary**
> - WIP is the value of something that sits between raw material and finished product — still "in the making."
> - For production (PP), it's a signal that flags bottlenecks; for cost (CO), it's the basis for asset value.
> - For inventory (MM), it represents "supply that's about to be finished," a key input for accurate inventory planning.

[[TOC]]

## What is WIP

Look inside a kitchen and ingredients fall into roughly three categories.

Raw materials sit in the storeroom — individual ingredients like onions, meat, and seasoning that haven't been processed at all. Finished products are the final dishes, plated and ready to go out to a customer. And in between sits **WIP**: a stew that just started simmering, or one that's fully cooked but not yet plated. It can't be served to a customer yet, but the ingredients have already combined to create new value.

WIP sits right in the middle of the production process. It's a living asset — raw material with labor and skill already being added to it.

![Diagram showing the flow from raw material through WIP to finished product, and the three perspectives of PP, CO, and MM](/images/sap-wip-overview.jpg)
*Figure 1. Where WIP sits, and the three perspectives on it*

## The production (PP) perspective — a stethoscope for the line

To a production planner, WIP is a diagnostic tool for reading the health of a production line.

If the amount of stew simmering in the kitchen (WIP) stays steady and reasonable, that means the line is running smoothly. But if WIP piles up in front of a particular step, that's a signal something's bottlenecked there — like when there's only one person doing the plating, so finished stew keeps backing up.

That signal lets a planner go beyond "something's wrong" to "which step needs what kind of fix" — adding more staff, or changing how a task is done. That's why accurate WIP data is a key metric for boosting production efficiency and preventing delivery delays.

## The cost (CO) perspective — the paperwork behind a hidden asset

To a cost accountant, WIP is the accounting information that puts a number on value you can't see.

Suppose, at month-end close, the value of 100 servings of stew simmering in the kitchen never makes it onto the books. Without running the WIP settlement process, the system has no automatic way to capture that value as an asset.

The system has already recorded both the money spent on ingredients (material cost) and the wages paid to the cook (labor cost) as "expenses." WIP settlement is the step that tells the system: "these costs didn't vanish — they turned into an asset called 'a dish that's cooking.'" Skip this step, and it looks like money went out with nothing to show for it, understating the company's assets.

This isn't just a numbers issue — it can distort how the company's profitability is judged, which can work against you in investment or loan reviews. That's why, to a CO accountant, WIP is a line item that underpins the reliability of the financial statements.

## The inventory (MM) perspective — a compass for forecasting

To an inventory planner, WIP is information needed to build an accurate future inventory plan.

The heart of inventory management is having "what's needed, when it's needed, in the amount needed." WIP sends the system (MRP) a signal: "supply is about to be finished."

If the system has no idea that 100 servings of stew are already cooking, it'll conclude stew is running short and request extra ingredients that aren't actually needed — which turns straight into storage and handling costs. Flip it around: if WIP exists but the system thinks it doesn't, sales might assume there's nothing to sell and miss an opportunity. That's why WIP is a decisive variable in optimizing both inventory cost and opportunity cost.

## Rabbit's Takeaway

WIP is the same "dish still cooking" seen through three different sets of eyes. For production (PP), it's a productivity gauge and a clue for troubleshooting. For cost (CO), it's the basis for accurate asset value. For inventory (MM), it's a benchmark for future planning.

Only when you understand all three perspectives can you accurately read the invisible flow of assets inside a plant. The dish hasn't hit the plate yet — but it's already carrying clear value. 😎

**Read more**

- [SAP GI, GR, CNF: the three moments inventory leaves, arrives, and gets made](/en/blog/sap-gi-gr-cnf)
- [SAP production order status codes: the order in which a dish comes together](/en/blog/sap-production-order-status)
- [SAP MRP: planning materials like a restaurant prepping a big group order](/en/blog/sap-mrp)

<!-- Related posts: prerequisite=; related=sap-production-order-status,sap-mrp; deepens=sap-gi-gr-cnf -->
