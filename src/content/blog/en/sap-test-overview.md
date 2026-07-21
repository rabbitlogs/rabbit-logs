---
title: "SAP testing's five stages: the verification journey of opening a new restaurant"
mapTitle: "SAP testing's five stages"
description: "From Fit/Gap and prototype testing through unit, integration, and UAT, here's the full picture of SAP's five testing stages, mapped against the process of opening a new restaurant."
pubDate: "2025-09-10"
category: "project"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPProjects", "SAPTesting", "IntegrationTesting", "UAT"]
---

Hi, this is Rabbit! 🐰

The day finally arrives: after billions spent and countless people spending one to two years on it, the SAP system goes live. Then, on that very day, sales says "orders aren't going through," production says "a bad plan came down and the line stopped," and finance says "revenue numbers don't add up anywhere" — all at once. What then?

Just imagining that disaster is enough to make anyone nervous, and the process that prevents it is **testing**. In an SAP project, "build it rough and just launch" doesn't fly. The principle is "trust, but always verify." Today, let's map out that verification process — the five testing stages — against the process of opening a new restaurant.

> **3-line summary**
> - SAP testing is the essential verification process that prevents disaster after go-live.
> - It flows through five stages: Fit/Gap → prototype → unit → integration → UAT.
> - It's a tightly connected journey — you can't skip a stage or do them out of order.

[[TOC]]

## Why put this much effort into testing

You might think, "if you build it well, isn't that enough? Why make testing this complicated?" The reasons are clear.

First, it reduces risk — heading off business disruption or financial loss from system errors before they happen. Second, it guarantees quality — confirming that the functionality you promised to build actually works as intended. Third, it builds trust — giving the project team confidence that "this is ready to hand over," and giving the business confidence that "this is safe to use."

A new restaurant works the same way. You don't bring in kitchen equipment and start serving customers right away. You check, step by step, whether the gas line works properly, whether the floor plan flows well, whether the POS system talks to the kitchen — and only then do you open the doors.

## The five-stage inspection before opening a new restaurant

Just as a new restaurant goes through concept confirmation, a trial run, ingredient inspection, kitchen-and-floor integration, and a final check before opening, SAP testing flows through five stages as well.

![Flow diagram of SAP's five testing stages: Fit/Gap, prototype, unit, integration, UAT](/images/sap-test-flow.jpg)
*Figure 1. SAP's five testing stages — the verification journey of opening a new restaurant*

### Stage 1: Fit/Gap analysis — does the concept fit our restaurant

This stage checks whether headquarters' standard menu and way of operating actually work for our restaurant. It sorts out how well our desired future way of working (To-Be) matches SAP's standard functionality (Fit), and what's different enough that it needs custom work or adjustment (Gap). Think of it as the final review of the design stage.

### Stage 2: Prototype testing — take a look at the trial store first

Before the real construction begins, this stage sets up a trial version of the store for people to see in advance. Users get to experience firsthand whether the layout is convenient and whether the screens are easy to use. It's a "preview" stage — the development items decided in Fit/Gap get built as a prototype and verified early, with any additional requirements folded back in.

### Stage 3: Unit testing — inspecting each ingredient one by one

This is the process of pulling out each ingredient brought into the restaurant and checking its freshness and condition individually. It's the "component quality check" stage, where the developer or consultant verifies, on their own, that the smallest unit of functionality they built (a program, a function) works flawlessly in isolation.

### Stage 4: Integration testing — do the kitchen and the floor actually connect

With verified ingredients, the kitchen gets set up and connected to the dining floor. This stage checks: "when an order comes in from the floor, does it show up correctly on the kitchen monitor?" It's a "connectivity test" verifying that different modules — sales, purchasing, production, accounting — exchange data properly, and that a single business process flows from start to finish without a hitch.

### Stage 5: UAT — the owner's final walk-through before opening

The store is finally complete. This stage brings in the people who'll actually work there — the business users — to try it out directly: "do orders go in smoothly, does checkout work without a hitch?" — and get their final sign-off. It's the last test, confirming and approving, from the real user's perspective, that "this system is genuinely a good fit for how we work."

## Rabbit's Takeaway

These five stages form a tightly connected journey that can't be skipped or reordered. You can't set up a trial store (prototype) without reviewing the concept first (Fit/Gap), and you can't check how the kitchen connects to the floor (integration) without inspecting the ingredients first (unit).

Starting with the next post, we'll walk through each stage in detail. Keep this overview in your head like a map, and even SAP testing — which looks complicated at first — will start to feel like the natural process of preparing to open a new restaurant. 😎

**Read more**

- [SAP implementation projects: the five hurdles of opening a new store](/en/blog/sap-build-project-difficulty)

<!-- Related posts: prerequisite=sap-build-project-difficulty; related=; deepens= -->
