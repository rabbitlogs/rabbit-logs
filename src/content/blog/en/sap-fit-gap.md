---
title: "SAP Fit/Gap analysis: measuring the distance between standard and your restaurant"
mapTitle: "SAP Fit/Gap analysis"
description: "Fit/Gap analysis identifies how well SAP's standard functionality matches your company (Fit) and what needs adjustment (Gap), explained through the process of adapting a corporate standard menu to your own restaurant."
pubDate: "2025-09-17"
category: "project"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPProjects", "FitGap", "SAPTesting", "Implementation"]
---

Hi, this is Rabbit! 🐰

[Last time](/en/blog/sap-test-overview), we mapped out the full picture of SAP testing's five stages. Today's the first of those stages: **Fit/Gap analysis**.

You might say, "isn't Fit/Gap part of design, not testing?" And you'd be right. But I like to call it "the first test of whether the system we're about to build actually fits our company" — because it's the stage where you check, ahead of time, whether the standard operating approach handed down from headquarters can actually be used as-is at your restaurant.

> **3-line summary**
> - Fit is where SAP's standard functionality matches our business as-is; Gap is what needs adjusting or is simply missing.
> - Doing this right before development starts (at the design stage) avoids expensive rework later.
> - How you resolve each Gap — develop, change the process, or accept it — is what drives the project's cost.

[[TOC]]

## What is Fit/Gap analysis

After the PI stage, we've drawn up a future blueprint (To-Be) of "here's how our company will operate going forward." Now it's time to build the system that matches that blueprint, and the first question to ask is: "how much of what we want does SAP already give us out of the box?"

Answering that question is what Fit/Gap analysis does. It's like taking the standard menu lineup from headquarters and trying it out at your own restaurant.

**Fit** (what matches) is when you can use the headquarters standard as-is. If the inventory management approach we want lines up exactly with SAP's standard functionality, that's "we can just use the standard for this."

**Gap** (what doesn't match or is missing) is when our restaurant's specific needs aren't covered by the standard. Company-specific discount policies or a complex approval chain often just aren't in SAP's standard offering. "This function doesn't exist in SAP, so what do we do?" — that question marks a Gap, and it's the homework that needs focused attention.

In the end, Fit/Gap analysis is the process of comparing what we want (To-Be) against the SAP standard, and clearly separating what we can use as-is (Fit) from what needs adjustment (Gap).

## Timing is everything

When should this analysis happen? The answer is "right before development actually starts." In SAP methodology, that's usually during the Blueprint (or Explore) stage.

In restaurant terms: you decide on a concept (To-Be design), try applying the headquarters standard operating approach in practice (Fit/Gap), and only then either customize it for your restaurant (development) or adopt it as-is (build). If you build everything first and only discover the mismatch afterward, you're tearing things apart and redoing them — doubling both time and cost. That's why timing is everything.

## Three ways to resolve a Gap

![Diagram distinguishing Fit from Gap, and outlining the three ways to resolve a Gap: development, process change, or acceptance](/images/sap-fit-gap-ways.jpg)
*Figure 1. Distinguishing Fit from Gap, and three ways to resolve a Gap*


Every Gap found in a Fit/Gap workshop gets logged in a list. Then comes the decision of how to resolve each one — and this is where the project's direction splits. There are three paths.

**Development (fit the standard to us).** "Let's build a custom report for our company." The most common path, but it costs extra time and money. This means either developing custom functionality (Z-code) or adjusting configuration. It's adding a special dish of your own on top of the headquarters standard menu.

**Process change (fit us to the standard).** "Actually, SAP's standard approach is more efficient — let's adapt our workflow to the system." The most ideal option, but it can meet resistance from staff attached to the old way of doing things, so it takes real effort to build buy-in.

**Acceptance (just live with it).** "It's a bit inconvenient, but not unworkable, so let's just use the standard as-is." You can't develop everything, so a sensible compromise is sometimes the smart call.

This decision determines how much additional development is needed, which directly drives the project's difficulty and cost.

## Rabbit's Takeaway

Fit/Gap analysis is more than just comparing functionality against requirements — it's the compass that sets the project's scope, budget, and timeline. How you choose to resolve each Gap changes the weight of the entire project.

A thorough, realistic Fit/Gap analysis isn't just "an expensive spreadsheet" — it's the first real step toward building a system that truly fits your company. 😎

**Read more**

- [SAP testing's five stages: the verification journey of opening a new restaurant](/en/blog/sap-test-overview)

<!-- Related posts: prerequisite=sap-test-overview; related=; deepens= -->
