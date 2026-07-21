---
title: "SAP Best Practice: why you'd want to use a proven recipe"
mapTitle: "SAP Best Practice"
description: "Explains what SAP Best Practice is, why SAP builds start from standard processes, and why following the standard 100% is a mistake — using a meal-kit analogy."
pubDate: "2025-08-27"
category: "project"
series: "SAP project basics"
level: "beginner"
tags: ["SAPProjects", "SAPBestPractice", "SAPImplementation", "SAPStandards"]
---

Hi, this is Rabbit! 🐰

Imagine you're opening a new restaurant. Menu development, kitchen layout, how you'll order ingredients — designing all of it from scratch feels overwhelming. But then you come across a "proven recipe meal kit" put together by a consultant who's helped hundreds of restaurants succeed nationwide over decades. The kit includes ingredient composition, cooking sequence, even staffing. The moment you see it, you think: "Starting from this would cut our chance of failure dramatically."

In an SAP implementation project, <strong class="key">Best Practice</strong> is exactly that meal kit.

> **3-line summary**
> - SAP Best Practice is a set of global standard processes distilled from the success patterns of thousands of companies.
> - Starting from Best Practice instead of designing everything from scratch reduces time, cost, and risk.
> - But the standard isn't automatically the right answer — adjustments that preserve your company's strengths are essential.

[[TOC]]

## What Best Practice is

**SAP Best Practice** is a set of industry-specific standard processes SAP has built by analyzing decades of implementation cases across companies worldwide. It packages the conclusion of "this is the most efficient way to run this industry" into system configuration, process flows, and document templates all at once.

Like a restaurant meal kit, you don't have to source every ingredient and build a recipe from nothing — you can start from an already-proven composition. That shortens project timelines and reduces unexpected design errors.

In manufacturing, Best Practice is especially well developed for the SAP PP (Production Planning) module. The entire production process — from planning to execution to results confirmation to cost calculation — is provided as a standardized flow.

> 💡 **Key point**: Best Practice is the starting point SAP provides. Without it, every company reinvents the wheel; but if you follow it blindly, your company loses its distinct characteristics.

## Why start from Best Practice

What happens if you design every process from scratch on your own? It can take months just to arrive at the optimal design for your company, and the trial and error along the way translates directly into project cost and schedule overruns.

Starting from Best Practice, on the other hand, lets discussion begin on an already-proven foundation. You can approach it by checking "here's how the standard works — where does our company differ?" — a much more efficient way in.

This process is called [SAP Fit/Gap analysis](/en/blog/sap-fit-gap). You map your operations to the standard (Fit), and handle only the truly necessary exceptions separately (Gap).

How you adopt Best Practice also affects project duration. Designing everything from scratch alone can take months of design work, but starting from Best Practice lets you begin at the verification stage. For companies whose processes don't deviate much from the standard, this can shorten the implementation timeline considerably.

## Why you shouldn't follow Best Practice 100%

==No matter how good a meal kit is, it can't fully match your family's exact taste. SAP Best Practice is the same.==

Global standards are designed for broad applicability. A company's unique production method, long-standing contract terms with vendors, or local tax handling requirements may not be captured in the standard.

Ignoring these gaps and following Best Practice as-is creates two problems. First, business users have to tolerate inconvenience while adapting to the system. Second, your company's core competitive strengths don't get reflected in the system, cutting the value of the whole implementation in half.

Best Practice isn't "the answer" — it's "a good starting point." The wise approach is to understand the standard thoroughly, then apply adjustments only where your company genuinely needs them.

![SAP Best Practice flow — starting from the global standard process, going through Fit/Gap analysis, and arriving at company-specific configuration](/images/sap-best-practice-01.jpg)
*Figure 1. The flow from Best Practice through Fit/Gap analysis to your company's final configuration*

## Where to find it and how to use it

SAP provides Best Practice packages by industry, and you can review process documentation and configuration guides on the [SAP Business Accelerator Hub](https://hub.sap.com).

Early in an implementation project, consultants conduct business interviews based on this Best Practice documentation. "Here's how the standard process works — how does your company currently handle this?" is the opening question of Fit/Gap analysis.

> ⚠️ **Note**: Even when building on Best Practice, the project fails without active participation from business users. Just because the system follows the standard doesn't mean the floor automatically follows along. [SAP change management](/en/blog/sap-change-management) has to happen alongside it for the implementation to take root on the ground.

## Rabbit's Takeaway

There are two common misconceptions about Best Practice on the ground.

One is the overconfidence that "following Best Practice is automatically good." The other is excessive resistance: "our company is too unique for the standard to fit."

Reality sits in between. Follow the standard as closely as possible where it fits well, and modify carefully only where your company's competitive edge is at stake. Development that departs from the standard ([Z-code](/en/blog/sap-cbo-z-program)) comes with a maintenance burden, so it should only be used where truly necessary.

Respecting the meal-kit recipe while adding only the seasoning your family really needs — that's the best way to make the most of Best Practice. 😎

**Read more**

- [SAP Fit/Gap analysis: measuring the gap between the standard and your store](/en/blog/sap-fit-gap)
- [SAP implementation projects: the five hurdles of opening a new store](/en/blog/sap-build-project-difficulty)

<!-- Related posts: prerequisite=; related=sap-fit-gap,sap-build-project-difficulty; deepens= -->
