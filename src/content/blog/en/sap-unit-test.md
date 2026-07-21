---
title: "SAP unit testing: inspecting each ingredient one by one"
mapTitle: "SAP unit testing"
description: "Unit testing is where a developer verifies that the smallest piece of functionality they built works correctly on its own — explained through the process of inspecting each ingredient brought into a restaurant."
pubDate: "2025-10-01"
category: "project"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPProjects", "UnitTesting", "SAPTesting", "Implementation"]
---

Hi, this is Rabbit! 🐰

We're on the third of five testing stages: unit testing. Once [prototype testing](/en/blog/sap-prototype-test) locked in what the functionality should look like, developers and consultants start building their individual "parts" — an order-entry program for sales, an automatic goods-receipt feature for purchasing, a custom report for accounting.

But before assembling these parts into the big kitchen we call "SAP," there's a question worth asking first: "is this ingredient actually fresh enough to bring into the kitchen?" Today we cover the first checkpoint where developers verify their own work: unit testing.

> **3-line summary**
> - Unit testing checks whether the smallest unit of the system (a program, a function) works correctly on its own.
> - The developer or consultant who built that piece verifies it themselves, with a "my work, my responsibility" mindset.
> - Small units have to be flawless first, so that combining them later causes fewer problems.

[[TOC]]

## What is unit testing

Unit testing, true to its name, is the activity of checking whether the smallest unit that makes up the system works correctly on its own. Here, a "unit" is a very small piece — a single program, a single function.

Think of it like a restaurant: it's the process of pulling out each ingredient that came in and inspecting it individually. Is this onion firm, is this meat fresh — checking the quality of each ingredient separately, without worrying about the ingredient next to it or how it'll be cooked. Right now, only the condition of this one ingredient matters.

Who does this inspection? The person who brought that ingredient in — meaning the developer who built the program, or the module consultant who configured the feature — does it themselves. It's the first step of quality assurance, done before handing the work off to anyone else, with a "my work, my responsibility" mindset.

The core idea of unit testing is that catching small problems early requires each small piece to be flawless first. Good dishes only come from good ingredients.

## When and how it happens

Unit testing isn't a one-time event held on a set day. It has to be finished "right after" a developer completes a feature, and "before" integration testing combines multiple parts together. It's an activity that repeats throughout development.

Say a developer just finished a new order-entry program. They check various scenarios one by one — normal input, invalid values, empty fields. If an error shows up under a specific condition, they fix it immediately and run through every check again from the start. Only once everything passes does it become "okay, this is ready to move to the next stage."

## Unit testing vs. integration testing

![Table comparing unit testing and integration testing across five criteria, using the analogy of ingredient inspection vs. dish inspection](/images/sap-unit-test-01.jpg)
*Figure 1. The difference between unit testing and integration testing — ingredient inspection vs. dish inspection*

A lot of people mix up unit testing with the next stage, integration testing. Here's the clear distinction.

| Criteria | Unit testing | Integration testing |
|---|---|---|
| Analogy | Inspecting the quality of one ingredient | Checking whether combined ingredients become a dish |
| Scope | One small piece — a program or function | The full business flow across connected modules |
| Purpose | Catch logic errors in individual functionality | Catch connection errors between modules |
| Timing | Right after development finishes | After unit testing is complete |
| Participants | Developers, module consultants | Multiple consultants, key users |

*Table 1. The difference between unit testing and integration testing*

Skip unit testing and jump straight to integration testing, and it's like finishing a whole dish without ever checking the ingredients first. When something tastes off later, figuring out whether it was the onion, the meat, or the seasoning takes far more time and money.

## Rabbit's Takeaway

Unit testing is small and repetitive, so it doesn't stand out much from the outside — but it's the cornerstone holding up the quality of the entire project. Through this process of developers guaranteeing the quality of their own code, the project ends up with a large stack of solid, defect-free components.

Gathering these verified parts and confirming they all mesh together properly is the job of the next stage: integration testing. 😎

**Read more**

- [SAP prototype testing: the trial store you visit before construction begins](/en/blog/sap-prototype-test)

<!-- Related posts: prerequisite=sap-prototype-test; related=; deepens= -->
