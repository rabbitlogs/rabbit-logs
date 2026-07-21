---
title: "SAP production order status codes: the order in which a dish comes together"
mapTitle: "Production order status codes"
description: "SAP production order status codes like CRTD, REL, CNF, DLV, and TECO, explained through the order in which a dish comes together in the kitchen."
pubDate: "2026-02-12"
category: "operations"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPOperations", "ProductionOrder", "StatusCode", "SAPPP"]
---

Hi, this is Rabbit! 🐰

Open a production order in SAP, and you'll see a string of status codes — CRTD, REL, TECO, and so on. At first they look like cryptic passwords, but they actually mirror the order in which a single dish comes together in the kitchen.

Today, let's map these production order status codes against the cooking process, from prepping ingredients all the way to closing out the kitchen.

> **3-line summary**
> - Production order status codes are markers that tell you exactly what stage an order is currently at.
> - They flow in this order: CRTD (prep) → REL (start) → CNF (process done) → DLV (received into stock) → TECO (closed out).
> - Each stage has to reach the right status before the next action is allowed (for example, you need REL status before materials can be issued).

[[TOC]]

## Why the "order" matters

Cooking has a sequence. Pour the sauce before the noodles are boiled, or turn on the burner before the ingredients are prepped, and the dish falls apart. Production order status codes work the same way. Only once an order reaches the right status for a given stage does the system allow the next action.

For instance, you can't pull materials from the warehouse (issue materials) unless the order is in "cooking started" (REL) status, and once it hits "kitchen closed" (TECO), that order gets locked so nobody can touch it anymore. That's why the status code is such important information — it tells you exactly where a production order currently stands.

You can check an order's current status at a glance in the "Status" field on the CO03 (display production order) screen.

## The five core status codes

![Flow diagram of the five production order status stages: CRTD, REL, CNF, DLV, TECO](/images/sap-production-order-status-flow.jpg)
*Figure 1. Production order status flowing like the sequence of preparing a dish*

Let's walk through the five stages you'll run into most often in practice, mapped to the cooking process.

**CRTD (Created) — ingredient prep stage.** This is the status when a production order is first created in the system. It's the very first step — laying out the ingredients you'll need on the counter and checking the recipe. Full-scale production hasn't started yet, so the order can still be edited or deleted at this point.

**REL (Released) — cooking starts.** This is the "okay, now we're really starting" moment — turning on the burner. It means official approval has been given to start production. Only once an order reaches this status can you actually pull ingredients (issue materials) and start the real work of stir-frying or boiling (process confirmation). It's one of the most important statuses in day-to-day work.

**CNF (Confirmed) — process complete.** This is the worker stamping the system to confirm that each production process finished as planned — similar to checking whether the noodles are cooked through and the seasoning is right. Once every process is confirmed, the order reaches final CNF status.

**DLV (Delivered) — finished, plated.** This status means production for the ordered quantity is complete and the goods have been received into stock. It's like transferring the finished dish onto a plate, ready to serve to the customer.

**TECO (Technically Completed) — kitchen closed.** This status declares that all technical activity related to production has finished — like putting away the cooking tools and shutting off the gas valve. Once TECO is set, that order gets locked and no more production activity can happen against it. It's typically used for final closeout after DLV.

## Additional statuses worth knowing

Beyond the five above, there are a few secondary statuses you'll occasionally run into on screen.

| Abbreviation | Meaning | Description |
|---|---|---|
| PCNF | Partially Confirmed | Only some processes are complete |
| PDLV | Partially Delivered | Only part of the ordered quantity has been received so far |
| GMPS | Goods Movement Posted | A material movement has been reflected in the system |
| BCRQ | Backflush Required | Includes materials that get automatically deducted (backflush) |
| SETC | Settlement Completed | Cost settlement is complete |

*Table 1. Common secondary production order status codes*

## Rabbit's Takeaway

Production order status codes are easier to understand as a cooking process than as something you memorize by rote. It's a natural flow — from CRTD (ingredient prep), through REL (cooking starts), to TECO (kitchen closed) — the sequence a single dish naturally follows on its way to completion.

Once you know this sequence, you can look at the status code on any production order and instantly tell "ah, this one's at this stage right now." From there, things like why material issue is blocked, or why you can't edit an order, start to make sense naturally. 😎

**Read more**

- [SAP planned order vs. production order: the meal plan and the actual cooking ticket](/en/blog/sap-planned-vs-production-order)
- [SAP movement types: the stamp every ingredient gets each time it crosses the fridge door](/en/blog/sap-movement-type)

<!-- Related posts: prerequisite=sap-planned-vs-production-order; related=sap-movement-type; deepens= -->
