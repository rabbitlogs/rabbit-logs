---
title: "SAP integration testing: do the kitchen and the floor actually work as one"
mapTitle: "SAP integration testing"
description: "Integration testing gathers modules that already passed unit testing and verifies they connect seamlessly along the real business flow, start to finish — explained through how a kitchen and dining floor link up."
pubDate: "2025-10-08"
category: "project"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPProjects", "IntegrationTesting", "SAPTesting", "Implementation"]
---

Hi, this is Rabbit! 🐰

We're on the fourth of five testing stages: integration testing. If [unit testing](/en/blog/sap-unit-test) was about checking the quality of each individual ingredient, now it's time to gather those verified ingredients and confirm a dish actually comes together — that the kitchen and the dining floor mesh properly.

No matter how perfect the ingredients or equipment are on their own, the restaurant doesn't run unless they connect into a single flow. Today's topic is integration testing: confirming that the separate pieces come together as one working system.

> **3-line summary**
> - Integration testing gathers modules that already passed unit testing and checks that they connect along the actual business flow.
> - It verifies the links between modules (kitchen and floor), the overall flow (order → shipment → billing), and connections to external systems.
> - Most errors show up at the seams, so that's where testing focuses hardest.

[[TOC]]

## What integration testing is

Integration testing gathers each module that has already passed unit testing and verifies they connect seamlessly along the real business flow, from start to finish.

If unit testing was about checking the quality of a single onion or a single cut of meat, integration testing is about watching those ingredients actually become a dish and make it out to the dining floor. It confirms connections like: "when the floor places an order, does it show up correctly on the kitchen monitor?" and "when the kitchen finishes, does the floor get notified?"

When an order comes in through Sales (SD), Inventory (MM) needs to pick up the signal and prepare the shipment, and Finance (FI) needs to issue the billing document. Integration testing verifies that these connections mesh precisely — that the output of one step lands correctly as the input of the next.

## Why it matters

![Diagram of the integration test flow from sales order (SD) to goods issue (MM) to invoice (FI) to payment (FI), with the connection points marked](/images/sap-integration-test-flow.jpg)
*Figure 1. The business flow crossing modules, and where the seams are*


Why bother running everything together? To prevent the absurd situation after go-live where "the order came in, so why didn't the shipment go out?" Integration testing looks at three things, broadly.

**Are the connections between modules solid?** When Sales creates an order, Inventory needs to pick up the signal and act. This checks whether that connection meshes precisely — whether the kitchen and the floor are moving on the same signal.

**Does the overall flow hold together as designed?** It checks the full sequence — customer order → product shipment → billing — for missing steps or breaks along the way.

**Does it connect properly with external systems?** SAP doesn't run in isolation. It has to connect to outside systems like a warehouse system (WMS) or a production system (MES). This is where those connection points (interfaces) get tested carefully against spec.

## How it's run

Integration testing follows a structured sequence.

First, you build **test scenarios** — a detailed "script" laying out the business flow that needs to work, step by step. For an "order-to-cash" flow, for example: Sales registers a sales order (SD), Logistics ships the product (MM), Finance issues the invoice (FI), and Finance processes the payment (FI).

Next, you prepare **an environment and data that mirror production.** You set up a clean test server (QAS) identical to the production environment and use master data (customer and product information) close to the real thing. Fake data won't surface realistic errors.

Then, everyone **gathers in the war room.** Representatives from sales, purchasing, production, and finance sit in one room, each working through their part of the script and confirming in real time whether their output lands correctly with the next person. All eyes stay on the **seams** — that's where things loosen up fastest and where most errors show up.

Any issue found gets logged in a defect-tracking system, prioritized by severity, fixed by the responsible developer, and re-verified together in the war room. This cycle repeats several times, and the system gets steadily more solid with each pass.

## Rabbit's Takeaway

Integration testing isn't just about putting the pieces together — it's about confirming that each piece works in perfect harmony with the others, flowing exactly as designed. This is what dramatically lowers the risk of the business grinding to a halt after go-live.

That said, integration testing is still, ultimately, an "expert's-eye view" of how the systems connect. UAT, where real users try the system themselves and give final sign-off, is a different story. 😎

**Read more**

- [SAP unit testing: checking the quality of every single ingredient](/en/blog/sap-unit-test)

<!-- Related posts: prerequisite=sap-unit-test; related=; deepens= -->
