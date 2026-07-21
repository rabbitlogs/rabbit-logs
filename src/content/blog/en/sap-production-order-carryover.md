---
title: "SAP production order carryover: handling half-finished food at month-end close"
mapTitle: "SAP production order carryover"
description: "Two ways to carry an incomplete SAP production order into the next month — order carryover and WIP cost carryover — compared through the analogy of closing out a large restaurant catering order."
pubDate: "2026-03-30"
category: "operations"
series: ""
level: "intermediate"
tags: ["SAPOperations", "SAPProductionOrder", "SAPCarryover", "SAPWIP"]
---

Hi, this is Rabbit! 🐰

At month-end, restaurant kitchens run into an annoying situation. There was a big catering order meant to be finished today, and by closing time, only half of it is done.

The finished food can go into the fridge and be delivered tomorrow. The problem is the "half-cooked food." The ingredients have already been pulled and prepped, and some of it is already partway through cooking. How do you record this state in the books, and how do you hand it off to the chef picking it up tomorrow?

This is the heart of SAP <strong class="key">production order carryover</strong>.

> **3-line summary**
> - An incomplete production order at month-end can be handled in two ways.
> - **Order carryover**: close the existing order with TECO, and create a new order for the remaining quantity.
> - **WIP carryover**: leave the existing order open, and post only the incomplete cost to a work-in-process (WIP) account.

[[TOC]]

## Setting the scene: 30 servings of half-finished food

A large catering order comes in. You need to make 100 lunch boxes today. You pull ingredients for the full 100 servings (goods issue, GI) and work hard through the evening, but by the end of the day only 70 are actually finished (goods receipt, GR).

30 of them are partway through — ingredients prepped, cooking half done — when closing time arrives. Those "30 half-finished lunch boxes" are the **incomplete remainder**.

==Leave this as-is, and inventory and cost figures in SAP fall out of sync. Materials for 100 servings were issued, but only 70 finished units were received, so the system has no way to track where the remaining 30 servings' worth of material actually is.==

Carryover processing is how you sort this out.

What happens if you skip it? In SAP, materials for 100 servings went out, but only 70 finished units came in, and it just stays that way. MRP mistakenly assumes the remaining 30 servings' worth of material is still sitting in the warehouse and generates the wrong purchasing plan. Cost calculations get distorted too. This is often where the numbers stop adding up at month-end financial close.

## Method 1: order carryover (close existing + create new)

The first approach is to cleanly wrap up today's work as today's work.

"Today's ticket (the existing production order) closes out as 70 completed." The existing order gets closed with **TECO** (Technical Completion). Once TECO'd, no more materials can be issued to this order and no more finished goods can be received against it.

Then tomorrow morning, a "new ticket for the remaining 30" gets issued. A new production order is created, and the work continues there.

**Advantages of this approach:**
- The order that made 70 and the order that finished the remaining 30 are clearly separated.
- Production history, results, and quality data stay cleanly split by order.
- Monthly production performance analysis stays clean.

**Disadvantages of this approach:**
- The number of orders grows. If remainders happen often, orders pile up and become a management burden.
- You need to accurately calculate how much cost carries over from the old order to the new one. Figuring out "how much material actually went into those 30" is trickier than it sounds.

## Method 2: WIP carryover (keep the order open, carry only the cost)

The second approach leaves the order as-is and only handles the cost through accounting.

"The 100-unit ticket keeps running into tomorrow." The existing production order stays in **REL** (Released) status. It doesn't get closed.

Instead, at month-end close, the cost that's already gone into this order but hasn't yet come out as finished goods gets posted to a **WIP** (Work In Process) account. This records in the books, essentially, "this much value currently sits inside the lunch boxes still being made." When the remaining 30 are finished next month, the WIP gets cleared at that point.

**Advantages of this approach:**
- No need to create a new order, so there's less operational overhead.
- Cost flow stays consistent within a single order.

**Disadvantages of this approach:**
- If an order stays open too long, incomplete orders pile up. Eventually you run into situations like "wait, is this order still not done?"
- Real-time traceability suffers. It becomes harder to tell exactly how many units are currently in progress.

## Comparing the two approaches

| Category | Order carryover | WIP carryover |
|---|---|---|
| Handling of existing order | Closed with TECO | Kept open |
| Handling of remainder | New order created | Posted to WIP account |
| History management | Cleanly split by order | Accumulates in a single order |
| Operational burden | More orders | Accumulating incomplete orders |
| Cost accuracy | Requires calculating remainder cost | Handled at close via WIP |

> 💡 **Key point**: Which approach is right depends on the company's cost accounting policy and ERP design. Companies with a defined close policy often lean toward WIP carryover; environments where quality tracking and history matter tend to prefer order carryover. This decision should always be made together with accounting.

![Comparison of SAP production order carryover methods — showing the processing flow of order carryover and WIP carryover side by side](/images/sap-production-order-carryover-01.jpg)
*Figure 1. Comparing the two production order carryover methods*

## Common problems in practice

Carryover processing gets difficult mainly because the state of the "half-finished 30" is often messy.

Say all 100 servings' worth of ingredients were pulled, 70 finished units came out, and 5 defects showed up along the way. Now normal completed output is 65, and you need to handle the 5 defects and separate out the cost of the remaining 30 at the same time.

Or, when order carryover is chosen, it's sometimes unclear how to load the remainder's cost onto the new order. Precisely calculating the value of already-prepped ingredients or partly cooked food turns out to be trickier than expected.

> ⚠️ **Note**: Month-end carryover processing needs to be completed before the accounting close cutoff. Doing it right before the deadline leaves no time to fix errors if something goes wrong. Where possible, check for incomplete orders mid-month and identify carryover candidates ahead of time.

## Rabbit's Takeaway

Production order carryover looks complicated at first, but it really comes down to one question: "does the cost of what's half-finished belong to this month, or next month?"

It's the same as deciding whether to book today's half-cooked food's ingredient cost today, or when it's finished tomorrow. There's no universally correct answer — only company policy.

What matters is applying whichever method you choose consistently. Mixing methods — WIP carryover this month, order carryover next month — makes cost analysis meaningless. 😎

**Read more**

- [SAP WIP, the value of a dish not yet on the plate](/en/blog/sap-wip)
- [SAP Activity and CNF, the moment the kitchen log gets reported to the head chef](/en/blog/sap-activity-cnf)
- [SAP production order status codes, the sequence behind a finished dish](/en/blog/sap-production-order-status)

<!-- Related posts: prerequisite=sap-wip,sap-activity-cnf; related=sap-production-order-status; deepens= -->
