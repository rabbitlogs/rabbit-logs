---
title: "SAP and MES: the perfect division of labor between the head chef and the kitchen team"
mapTitle: "SAP and MES"
description: "SAP is the head chef planning production, MES is the kitchen team executing it. When the two systems split roles and mesh together, that's the foundation of a smart factory."
pubDate: "2025-07-23"
category: "study"
series: "SAP MES series"
level: "beginner"
tags: ["SAPLearning", "SAPMES", "SAPProductionPlanning", "SAPPP"]
---

Hi, this is Rabbit! 🐰

The head chef hands over an instruction sheet: "50 servings of steak tonight, 10kg of beef tenderloin, prep sequence goes like this." The kitchen team takes that sheet and steps up to the stove. The chef starts thinking about the next menu, while the kitchen team focuses on the dish in front of them right now. Take either one away, and the restaurant stops running.

The relationship between SAP and MES is exactly this. That's why "SAP-MES integration is the key to this project" keeps coming up on the shop floor.

> **3-line summary**
> - SAP (ERP) is the center of planning. It decides and instructs "what, how much, and when" to produce.
> - MES is the center of execution. It takes those instructions and manages production on the floor down to the second.
> - The two aren't in competition — they split planning and execution, each covering the other's gaps.

[[TOC]]

## SAP: the head chef who sets the plan

<strong class="key">SAP</strong>, and especially the PP (Production Planning) module, plays the head chef's role in a factory — stepping back from the heat of the kitchen floor to sketch out the bigger picture.

Following what a head chef actually does makes it easy to see what SAP is doing.

- "Get 50 servings of steak ready this week. We need 10kg of beef tenderloin — check if it's in stock." → **Material Requirements Planning (MRP)**
- "Chef A starts in kitchen 1 at 6 PM." → **Production order creation, process assignment**
- "Here's the recipe for this dish. Prep goes sear → finish → plate." → **BOM (Bill of Materials) and routing (process sequence) management**

==SAP decides "what, how much, and when," and sends it down to MES as an official instruction sheet: the production order.==

Another role the SAP PP module plays is MRP (Material Requirements Planning). To make 50 servings of steak, it automatically calculates how much beef is needed, how much is currently in the warehouse, and, if there's a shortfall, by when it needs to be ordered. It's the equivalent of a head chef looking at today's menu count and automatically generating an ingredient order list.

That said, SAP is a system built for planning. It was never designed to track a kitchen floor that changes second by second — that's exactly why MES is needed.

## MES: the kitchen team that runs the floor

<strong class="key">MES (Manufacturing Execution System)</strong> is, true to its name, all about execution. It takes the instructions handed down from SAP, carries them out on the floor, and records that process in real time.

Watching what the kitchen team actually does makes it clear what MES is.

- "Starting the steak sear as instructed. Grill temp currently 220°C." → **Equipment monitoring**
- "Steak 1 is medium, steak 2 is well-done, in progress." → **Real-time WIP (work-in-process) tracking**
- "Just burned one. Marking it defective." → **Quality management, defect logging**
- "Used 500g of beef tenderloin from the fridge." → **Actual material consumption tracking**

If SAP's plan is the "ideal," MES deals with "reality" itself. It collects data down to the minute and second, guides workers, and responds instantly to anything unexpected.

With MES in place, you can tell in real time that "the defect rate on line 3 is spiking right now." In an environment with only SAP, you'd only find that out once the day ends and a worker manually enters the results. That time gap translates directly into production loss.

## The four-step collaboration between the two systems

Let's trace how SAP and MES actually mesh together, following the flow of producing 50 servings of steak.

![Diagram showing the roles and data flow between SAP (head chef) and MES (kitchen team)](/images/sap-mes-role-01.png)
*Figure 1. How SAP (planning) and MES (execution) divide roles and collaborate*

**① Work instruction (SAP → MES)**
SAP creates a production order and sends it down to MES: "50 servings of steak, 10kg of beef tenderloin, prep sequence like this, due by tomorrow." It's an instruction sheet that carries the recipe (BOM) and the process sequence (routing) with it.

**② Production execution and real-time monitoring (MES)**
MES puts the order up on the floor screen, and workers start production against it. Completed quantity, equipment status, defects, and material consumption are all logged in real time. Where SAP said "make this by then," MES tracks, second by second, "here's how many are done, equipment is normal, no defects yet."

**③ Results reporting (MES → SAP)**
MES rolls up the results and sends them to SAP: "48 servings completed, 2 servings scrapped as defective, beef used ran 5% over plan." This data has to flow into SAP for inventory to stay accurate and for cost calculations to reflect reality.

**④ Analysis and settlement (SAP)**
SAP takes the reported results and analyzes the gap against plan: "planned 50 servings, completed 48 — what caused the difference?" This result becomes feedback that sharpens the next round of planning, and it also flows into the financial statements as accurate cost.

## SAP vs. MES at a glance

| | SAP (ERP) | MES |
|------|-----------|-----|
| **Core role** | Setting the plan — "what, how much, when" | Executing the plan — "how" |
| **Time unit** | Month / week / day | Minute / second (real time) |
| **Key data** | Finance, sales, inventory | Equipment, quality, work results |
| **Users** | Planning, finance, purchasing staff | Production managers, floor workers |
| **Restaurant analogy** | Head chef | Kitchen team |

*Table 1. Comparing the roles of SAP (ERP) and MES*

## Rabbit's Takeaway

==MES without SAP is execution without a goal, and SAP without MES is a plan detached from reality.==

That's exactly why "SAP-MES integration is the key" keeps coming up on the shop floor. The wider the gap between plan and actuals, the bigger the cost variance and the shakier inventory accuracy gets. Only when the two systems mesh properly does data actually flow, and the factory becomes visible.

Getting into the habit of thinking about MES as a package deal whenever you're learning SAP pays off quite a bit on the ground. 😎

**Read more**

- [SAP MES interfaces: the waiter's craft of connecting floor and kitchen](/en/blog/sap-mes-interface)
- [SAP Activity and CNF: reporting the kitchen log back to the head chef](/en/blog/sap-activity-cnf)

<!-- Related posts: prerequisite=; related=sap-mes-interface,sap-activity-cnf; deepens= -->
