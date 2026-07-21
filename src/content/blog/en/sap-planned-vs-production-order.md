---
title: "SAP planned order vs. production order: the meal plan and the actual cooking ticket"
mapTitle: "SAP planned vs. production order"
description: "How does a planned order created by MRP turn into a confirmed production order? The key difference between the two, explained through how a restaurant prepares and finalizes a large group order."
pubDate: "2026-02-05"
category: "operations"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPOperations", "SAPPP", "ProductionOrder", "PlannedOrder"]
---

Hi, this is Rabbit! 🐰

In the [MRP post](/en/blog/sap-mrp), I mentioned that MRP calculates "what to make, how much, and when" and proposes a "planned order." But that planned order isn't final yet. To actually go into production, it has to turn into a "production order."

The difference between the two is one of the most confusing parts for PP beginners. Today, using how a restaurant prepares for a large group order as the analogy, let's sort out exactly how planned orders and production orders differ.

> **3-line summary**
> - A planned order is a flexible "proposal" that MRP raises automatically.
> - A production order is a confirmed "execution instruction" from a planner, one that reserves materials and equipment.
> - Plan as a flexible proposal, execute as a firm command — that distinction is the whole point.

[[TOC]]

## Planned order — a flexible "prep draft"

Say you're prepping for a big group order coming in this Saturday. The first thing you do is sketch a rough draft. "Do we need about 80 more heads of napa cabbage? Chili powder can wait until Wednesday, where are we getting the pork from?" Nothing is confirmed yet — it's just a memo-level plan.

That "prep draft" is exactly what a **planned order** is. MRP calculates "to make 1,000 units of this product, we'll need 1,000 units of part A and 1,000 units of part B," and posts that as a proposal in the system. In short, it's a tentative suggestion: "what if we produced or purchased this?"

Here's what characterizes a planned order. It's a proposal MRP generates automatically, and it doesn't reserve any materials or equipment (it's just a note saying "we'll probably need this much"). So if plans change, the content can shift — or disappear entirely — the next time MRP runs. If the item is made in-house, it becomes a planned order for production; if it's a part bought externally, it becomes a purchase requisition instead.

## Production order — a confirmed "execution instruction"

After reviewing the draft, the decision finally gets made: "alright, let's go with this." The ingredients get actually ordered, burners and staff get assigned, and cooking gets underway. This is no longer a draft — it's a confirmed commitment. Changing it now takes more effort, but in exchange, you get real execution power.

That "confirmed instruction" is the **production order**. Once the production planner reviews the draft planned orders and decides "let's proceed with this," the planned order gets converted into a production order. A production order is a firm instruction: "produce this item, on this date, in this quantity, using this method."

A production order's characteristics are the exact opposite of a planned order's. It's confirmed by a person (the planner), and the moment it's created, the materials needed get reserved specifically for this order (essentially claimed so nobody else can use them). Work center capacity for the relevant process gets booked for this order too. And all the actual material cost, labor, and overhead incurred get tallied against this specific production order — it becomes the anchor point for cost calculation.

## The key differences at a glance

![Diagram comparing planned orders and production orders](/images/sap-planned-vs-production-order.jpg)
*Figure 1. The difference between a planned order (prep draft) and a production order (execution instruction)*


| Category | Planned order (prep draft) | Production order (confirmed instruction) |
|---|---|---|
| Purpose | Proposal for production/purchasing | Instruction and control of production activity |
| Created by | System (MRP) | Person (production planner) |
| Status | Fluid, tentative plan | Confirmed execution plan |
| Resource reservation | None | Yes (materials, equipment reserved) |
| Flexibility | Very high (can be changed or deleted) | Low (changes require history tracking) |

*Table 1. Differences between planned orders and production orders*

Splitting things clearly into a "planning" stage and an "execution" stage lets you stay flexible about an uncertain future while still driving confirmed production forward without wavering.

## Practical tips: conversion and lookup

In practice, many companies build custom Z-code to convert large batches of planned orders in a way that fits their own process. Standard conversion functionality exists, but companies often build their own tool tailored to their workflow.

When you want a quick overview across multiple orders, the production order information system (T-code `COOIS`) is the go-to. Like browsing a library by "new arrivals" only, "coming soon" only, or everything, COOIS lets you filter by production orders only, planned orders only, or both by condition — it's the all-purpose report PP practitioners use every day.

> 💡 **Note**: A production order moves through several statuses: created (CRTD) → released (REL) → goods issue → confirmation (CNF) → goods receipt (DLV) → closed (CLSD). This lifecycle deserves its own post, and I'll cover it in detail separately.

## Rabbit's Takeaway

The difference between a planned order and a production order boils down to one line: "plan as a flexible proposal, execute as a firm command."

MRP sketches the big picture and proposes it as a planned order; a person reviews it and confirms it as a production order. Once you get a feel for that distinction, the backbone of PP production instructions becomes clear. It's exactly like drafting a rough plan ahead of a big group order, then locking it in, reserving the ingredients, and giving the kitchen the go-ahead. 😎

**Read more**

- [SAP MRP, planning materials like a restaurant preparing for a large order](/en/blog/sap-mrp)

<!-- Related posts: prerequisite=sap-mrp; related=; deepens= -->
