---
title: "SAP PI: renovating the dining room doesn't change the recipes"
mapTitle: "SAP PI"
description: "What SAP PI (Process Innovation) is, and why operations need to change before a new system goes in, explained through the analogy of a restaurant renovation."
pubDate: "2025-08-13"
category: "project"
series: "SAP implementation projects"
level: "beginner"
tags: ["SAPProjects", "SAPPI", "SAPImplementation", "SAPProcessInnovation"]
---

Hi, this is Rabbit! 🐰

A restaurant does a complete renovation. New interior, a new POS system at the counter, even the kitchen equipment gets replaced. But something's off. The restaurant looks brand new, but operations run exactly like before.

Customer orders still get scribbled on paper notes. Ingredient orders still depend on a manager's notebook. Daily sales still get closed out on a spreadsheet by the owner every night.

The old way of working is still running on top of the new space.

This is the most common failure pattern in SAP rollouts. The system changed, but "how the work gets done" didn't. <strong class="key">SAP PI (Process Innovation)</strong> is the work that solves exactly this problem.

> **3-line summary**
>
> - SAP PI is the activity of fundamentally redesigning business processes before a system goes live.
> - Changing the system without changing the process just buys you a very expensive spreadsheet.
> - PI isn't IT's job. Business users have to be the ones driving it.

[[TOC]]

## What happens without PI

Say a restaurant decides on a full renovation. Before construction starts, there's one question worth asking: "What's actually broken about how we operate right now?" What happens if construction finishes without ever really answering that?

There's a new dining room, but servers still write orders by hand and carry them to the kitchen. There's a new POS system, but the owner still closes out the books by hand every night. The space changed, but the workflow stayed exactly the same.

==This is the textbook SAP failure pattern. Process has to come before system.==

Roll out SAP without PI, and SAP genuinely becomes "an expensive spreadsheet." It's just one more place to enter data, while all the existing manual work stays exactly as it was.

## What PI actually does: rewriting the recipes and the kitchen flow

**PI (Process Innovation)** starts with the question, "Is this really the best way to do this?" If a better way exists, the old process gets thrown out and redesigned from scratch.

In restaurant terms, before changing any equipment, you ask questions like these:

- Are there unnecessary steps in how an order travels from the dining room to the kitchen?
- Is writing ingredient orders by hand in a notebook really the best approach?
- Does someone really need to manually collect and enter all the performance numbers?

These questions surface which steps should be eliminated, which should be automated, and which need to be reordered. The result is a new process blueprint. SAP is the vessel that holds that blueprint.

> 💡 **Key point**: PI and automation (like RPA) are different concepts. Automation makes an existing process run faster. PI eliminates or redesigns the process itself. Automating a step that should be eliminated just makes the waste happen faster.

## A site without PI vs. a site that went through PI

Let's compare through restaurant operations.

**Before PI — a broken chain**

When a customer order comes in, the server writes it by hand and hands it to the kitchen. The kitchen starts cooking off that note, but there's no real-time way to know how many tables are waiting or how much ingredient stock is left. At the end of the day, the owner gathers up receipts and tallies everything by hand.

The problem with this flow is obvious. Information breaks at every step, human error piles up, and getting a clear picture requires someone to manually pull it all together.

**After PI — a connected chain**

The moment a customer order is entered at the dining room POS, it appears automatically on the kitchen monitor. Ingredient stock updates in real time, and when it drops below a threshold, a reorder alert fires automatically. Daily sales close out with a single button.

**PI is what creates this difference. SAP is just the tool that executes the flow that PI designed.**

Same restaurant, same SAP system — but whether PI happened or not completely changes how the floor experiences it.

![Comparison of restaurant operations before and after SAP PI — showing the broken manual workflow side by side with the SAP-integrated flow](/images/sap-pi-overview-01.jpg)
*Figure 1. Restaurant operations before and after PI*

## How PI actually runs

A PI project typically runs in three phases.

**Phase 1: Current-state diagnosis (As-Is analysis)**

"How does our restaurant actually operate right now?" Through interviews and direct observation of the work, the real workflow gets documented. Where the bottlenecks are, which tasks are duplicated, where data breaks down.

**Phase 2: Target design (To-Be design)**

"How do we ideally want to work?" Based on the problems identified, the improved direction gets designed. This is where SAP's Best Practices or industry-standard processes come into play as reference points. The blueprint that comes out of this phase becomes the basis for the SAP build.

**Phase 3: Execution design**

This phase gets concrete about how the To-Be process will actually be implemented inside SAP — which T-codes to use, what screen sequence the work will follow, and who holds which authorizations.

> ⚠️ **Note**: PI isn't work that belongs only to IT or consultants. The business users who know the actual work best need to be at the center of it. A process designed without them won't work on the floor.

## If you've been assigned as a PI lead

If you're a business user assigned as the "PI lead" on an SAP implementation project, it can feel overwhelming at first. It's common to not even know what you're supposed to do, since you're not the one building the system.

There's really one core question. **"Why do we do this task the way we currently do it?"** Asking that question about every piece of daily work is the most important role a PI lead plays. Among the things that feel obvious just because they've always been done that way, there are almost always some that could be eliminated or changed.

Consultants can't answer that question for you. Only the business side knows.

## Rabbit's Takeaway

SAP PI and the SAP build can feel like separate projects, but they're really one continuous flow. PI designs "how we're going to work," and the build turns that design into an actual system.

Get the order wrong and problems follow. Build the system first and force the work to fit around it, and business users end up feeling like the system made their job harder. Where PI is done well, SAP genuinely reduces the workload.

==The recipes and the kitchen flow have to change first for the new equipment to mean anything.== The success of a system rollout is decided by design, not technology. 😎

**Read more**

- [What is SAP? Understanding it as an integrated kitchen brain](/en/blog/sap-what-is-sap)
- [SAP cutover, moving day from the old kitchen to the new one](/en/blog/sap-cutover)
- [SAP implementation projects, the five hurdles of opening a new store](/en/blog/sap-build-project-difficulty)

<!-- Related posts: prerequisite=sap-what-is-sap; related=sap-build-project-difficulty,sap-fit-gap; deepens=sap-cutover -->
