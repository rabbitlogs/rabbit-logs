---
title: "SAP circular BOM: the kitchen logic behind reintroducing reworked ingredients"
mapTitle: "SAP circular BOM"
description: "Explains what an SAP circular BOM is, how to set it up for a rework scenario, and how it affects cost calculation, using a kalguksu broth analogy."
pubDate: "2026-03-12"
category: "operations"
series: ""
level: "intermediate"
tags: ["SAPOperations", "SAPBOM", "SAPPP", "SAPRework"]
---

Hi, this is Rabbit! 🐰

Picture a broth that's been simmering in the kitchen for a long time. When making today's kalguksu (knife-cut noodle) broth, you ladle in some of yesterday's leftover broth to deepen the flavor. But something odd happens in that moment: "kalguksu broth" becomes an ingredient in making "kalguksu broth."

In SAP, this structure is called a <strong class="key">circular BOM (recursive BOM)</strong> — a structure where the finished product itself is included again as a component within its own BOM. In theory it looks like an infinite loop, but in practice it's actually used to represent rework scenarios.

> **3-line summary**
> - A circular BOM is a structure where a finished product is included as a component within its own BOM.
> - It's used in rework scenarios, where a defective finished product is reintroduced to produce a good one.
> - To avoid an infinite-loop error, you must check "Allow cycles" on the BOM item detail screen.

[[TOC]]

## When a circular BOM comes up

A BOM is the list of materials needed to make a finished product. A typical BOM runs in one direction — making kimchi jjigae requires pork, kimchi, and tofu, for instance.

But in a rework process, the direction gets tangled.

Say finished product F was produced and received into the warehouse, but a quality inspection found it defective. That defective F needs to go into rework process H to be turned back into a good F.

Expressed as a BOM, the flow looks like this.

- Making F requires H
- Making H requires F (the defective unit)

F → H → F. A structure where each needs the other. When the system tries to explode the BOM to calculate material requirements, it falls into an endless loop.

Handling this circular structure correctly is what resolves this logical contradiction.

## The "Allow cycles" setting

You need to tell SAP, "this loop isn't an error — it's an intentional structure." When registering F (the defective unit) as a component in H's BOM, check the **"Allow cycles"** checkbox on the item detail screen.

This single checkbox is the safeguard that stops the system from calculating an infinite loop.

> ⚠️ **Note**: If you forget to check "Allow cycles," either the BOM won't save at all, or an error occurs when running MRP. This setting is easy to miss when building a rework BOM, so be sure to check it.

![SAP circular BOM rework flow — diagram showing the F→H→F cycle and where the "Allow cycles" checkbox sits](/images/sap-circular-bom-01.jpg)
*Figure 1. The F→H→F circular BOM structure in a rework scenario, and the "Allow cycles" setting*

## Viewing a circular BOM at multiple levels

Once the setup is complete, checking the structure with T-code CS12 (multi-level BOM display) shows something like this.

```
F (top-level material)
└─ .1  H (rework process)
       └─ ..2  F (defective unit reintroduced ← cycle occurs here)
```

You can see the system recognize the circular structure and stop the explosion at level .2 — successfully representing the structure without an infinite loop.

This display is useful for confirming that a rework BOM was registered correctly. Making it a habit to verify the structure with CS12 after setup helps prevent MRP errors down the line.

## Circular BOM and cost calculation

=="Doesn't a circular structure mean cost keeps adding up infinitely?"==

No. SAP doesn't perform infinite recursive calculation when costing a circular structure. Instead, it breaks the calculation loop by referencing the **current standard cost** already calculated in the material master.

When a single material has multiple BOMs (for normal production, for rework, etc.), which BOM serves as the basis for standard cost calculation is determined by the **production version**. The BOM tied to the production version with the highest priority, as set in the material master's Costing 1 view, is used for standard cost calculation.

> 💡 **Key point**: For the rework BOM to not affect standard cost, the normal production BOM needs to be given higher priority. You can find more detail on the production version concept in [SAP PP master data](/en/blog/sap-pp-master-data).

## When circular BOMs are used

Here are three common real-world situations where circular BOMs come into play.

**Rework**: reintroducing a defective finished product to turn it back into a good one — the most common use case.

**Byproduct recycling**: feeding a byproduct from the production process back into the same process. Common in chemical and food industries.

**Catalyst reuse**: a catalyst introduced into a process is recovered after the reaction and fed back into the same process.

What these situations have in common is a structure where "something already made, or something that came out of it" gets reintroduced.

There are also cases where a circular BOM isn't needed. If the rework process is managed under a completely separate material code, it can be handled without a circular structure. Which approach to use should be decided during project design, based on cost accounting policy and traceability requirements.

## What to check before setting up a circular BOM

Check three things before setting up a circular BOM.

First, confirm that the rework material codes are registered in the system. Both the F code (finished product) and H code (rework process) must exist in the material master before you can build the BOM.

Second, decide whether the finished product after rework will be managed under the same material code as normal product, or a separate code. This decision affects the circular BOM structure.

Third, coordinate with the costing team in advance. You need to jointly determine production version priority so the circular BOM doesn't affect standard cost calculation.

## Rabbit's Takeaway

A circular BOM looks theoretically impossible at first glance. But rework happens routinely on real production floors.

SAP supports this structure precisely so it can accurately capture the complex reality of production flows inside the system. A small setting like the "Allow cycles" checkbox is what makes an entire complicated rework flow traceable within the system.

If you're running SAP somewhere rework happens, and this setting isn't configured properly, both inventory and cost can end up diverging from reality. Get the concept down once, and you won't be caught off guard when you run into it in practice. 😎

**Read more**

- [SAP PP master data: understanding the four essentials](/en/blog/sap-pp-master-data)
- [SAP movement types: the stamp ingredients get every time they go in and out of the fridge](/en/blog/sap-movement-type)

<!-- Related posts: prerequisite=sap-pp-master-data; related=sap-movement-type; deepens= -->
