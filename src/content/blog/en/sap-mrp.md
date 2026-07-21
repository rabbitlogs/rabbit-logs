---
title: "SAP MRP: planning materials like a restaurant prepping a big group order"
mapTitle: "SAP MRP"
description: "MRP is the core brain of SAP PP. This post explains how it automatically calculates what's needed, how much, and when, through the lens of a restaurant preparing for a large group reservation."
pubDate: "2026-01-22"
category: "operations"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPOperations", "MRP", "SAPPP", "ProductionPlanning"]
---

Hi, this is Rabbit! 🐰

Tonight, our restaurant just got a group reservation. "100 servings of kimchi stew, by Saturday." The head chef's mind immediately starts racing: is there enough of everything, and if not, when does it need to be ordered to make Saturday's deadline? Do this math by hand and by gut every time, and you end up with some ingredients running short mid-cook and others sitting around long enough to spoil.

The system that automates this headache-inducing calculation is **MRP** (Material Requirements Planning) — the core brain of the SAP PP module. Today, let's walk through how MRP actually works, using a restaurant prepping for a large group order as the guide.

> **3-line summary**
> - MRP automatically calculates what materials are needed, how much, and when, based on the production plan.
> - The calculation needs three inputs: the production target (MPS), the recipe (BOM), and current inventory.
> - It works through total requirements → net requirements → order timing, in that order, to generate a "planned order."

[[TOC]]

## What exactly is MRP

In one sentence, MRP is "the system that calculates what materials are needed, when, and how much, based on the production plan."

Like a capable kitchen manager, MRP works backward from the final goal we set — "100 servings of kimchi stew by Saturday" — and builds out a plan covering every ingredient needed to get there. At its core, it's answering three questions: what's needed, how much is needed, and by when. Get these answers right, and you avoid both production stoppages from running short and waste from over-ordering.

## The three things MRP needs before it can start

Even a sharp manager needs information to build a plan. MRP needs exactly three inputs before it can start calculating. Let's walk through it using the group-order example. The mission: "100 servings of kimchi stew, done by Saturday."

**1. Production target (MPS, Master Production Schedule).** The first thing needed is "what to make, by when, and how many." Our target is "100 servings of kimchi stew, by Saturday" — that's the Master Production Schedule (MPS). Without this target, MRP doesn't even know what it's supposed to be planning for.

**2. Recipe (BOM, Bill of Materials).** Once the target is set, you need the recipe — a list of exactly which ingredients go into one serving, and how much of each. This is the BOM. With the BOM in hand, MRP can start calculating: "100 servings means we'll need 100 heads of napa cabbage, 20kg of chili powder."

**3. Inventory information.** Finally, you need to know what's currently in the storeroom, and how many days it takes to get more if you order (lead time). You can't just buy everything blindly.

| Ingredient | Needed per serving | Current stock | Lead time |
|---|---|---|---|
| Napa cabbage | 1 head | 20 heads | 2 days |
| Chili powder | 0.2kg | 0kg | 3 days |
| Radish | 0.3 each | 10 each | 1 day |

*Table 1. Example ingredient information needed for an MRP calculation*

With this, MRP has everything it needs: the target (MPS), the recipe (BOM), and the current state (inventory).

## How MRP calculates

![Four-step flow diagram showing MRP calculating total requirements, net requirements, order timing, and the planned order](/images/sap-mrp-flow.jpg)
*Figure 1. MRP's four-step calculation, using the big kimchi-prep example*


Now let's follow how MRP builds an "order list" (the planned order). The goal: 100 servings of kimchi stew.

**Step 1, calculate total requirements.** Using the target and the recipe, work out the total amount of each ingredient needed. Napa cabbage: 1 head × 100 = 100 heads. Chili powder: 0.2kg × 100 = 20kg. Radish: 0.3 × 100 = 30 pieces.

**Step 2, calculate net requirements.** Subtract current inventory from the total requirement to find what's actually still needed. Cabbage: 100 minus 20 = 80 more heads. Chili powder: 20 minus 0 = 20kg more. Radish: 30 minus 10 = 20 more pieces.

**Step 3, calculate order timing.** With the net requirement set, work backward using lead time to determine when to place each order. Cooking starts Saturday. Cabbage (2-day lead time) needs to be ordered Thursday, radish (1 day) on Friday, and chili powder (3 days) on Wednesday to make it in time.

**Step 4, generate the planned order.** Putting it all together, MRP reports the final order list: chili powder, 20kg, ordered Wednesday; cabbage, 80 heads, ordered Thursday; radish, 20 pieces, ordered Friday. This is the core principle behind how MRP works.

> 💡 **Note**: The "planned order" MRP produces isn't final yet — it's a proposal. Converting it into an actual purchase requisition or production order is the next step. The difference between a planned order and a production order is a topic for another post.

## The faster option: MRP Live (MD01N)

The method described so far is called "classic MRP." It typically ran overnight as a batch job, when system load was low — much like a manager writing up a report overnight and leaving it on the desk for the next morning.

But with the move to [S/4HANA](https://www.sap.com/products/erp/s4hana.html), **MRP Live** (T-code: `MD01N`) arrived. It runs MRP in real time, very fast, using HANA's in-memory technology. No more waiting overnight — material plans can be run instantly, whenever needed. If classic MRP is "an assistant who calculates overnight and reports back in the morning," MRP Live is "an assistant who answers the moment you ask." That makes it far more agile for handling urgent orders or sudden plan changes.

## Rabbit's Takeaway

MRP looks complicated, but underneath, it's just a logical process: set the target, use the recipe to figure out the requirement, subtract inventory, and work backward by the lead time to set the order timing. It's the same calculation we run in our heads when prepping for a group order — the system just does it for thousands of materials at once.

That's why what really drives MRP isn't fancy functionality — it's accurate input. The target (MPS), recipe (BOM), and inventory all need to be correct for MRP to be correct. It's the same as needing good ingredients to make a good dish. Next time, let's look at the PP master data that forms the foundation of this whole calculation. 😎

**Read more**

- [SAP PP master data: the 4 essentials to know](/en/blog/sap-pp-master-data)

<!-- Related posts: prerequisite=sap-pp-master-data; related=; deepens= -->
