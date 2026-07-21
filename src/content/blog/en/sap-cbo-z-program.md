---
title: "SAP CBO: the head chef's secret recipe, also known as Z-code"
mapTitle: "SAP CBO"
description: "CBO (Z-code) is what a company builds when standard SAP functionality can't cover its work. Covers what it is, its pros and cons, and the real-world dilemma against standard T-codes."
pubDate: "2026-01-04"
category: "operations"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPOperations", "CBO", "ZCode", "Customization"]
---

Hi, this is Rabbit! 🐰

You've probably heard someone on the business side say, "this needs to be built as a Z." Today we're covering an old companion of SAP development: **CBO** (Z-code). When standard SAP functionality can't handle a company's specific business needs, CBO shows up like a savior — but that same savior can sometimes end up being the reason the system gets bloated and slow.

Today, let's cover what CBO actually is, its pros and cons, and the real-world dilemma it creates on the ground.

> **3-line summary**
> - CBO is a program a company adds on its own; its name starts with Z or Y, so it's called "Z-code."
> - Built separately without touching standard functionality, it's stable — but it becomes hard to manage once it piles up.
> - There's no clean answer between standard T-codes (hard to control, but powerful) and Z-code (convenient, but a burden as it accumulates).

[[TOC]]

## What exactly is CBO

**CBO** stands for "Customer Bolt-On" — in plain terms, "a program the customer (company) added on its own." It's similar to bringing in a special tool just for your store, on top of an already well-equipped kitchen.

In practice, the term **Z-code** gets used far more often than CBO. SAP has a rule that any development object a company builds itself must have a name starting with Z or Y — a device for telling standard SAP programs apart from company-built ones at a glance. It's like marking headquarters' standard menu items separately from a location's own special items on the menu board. You can tell right away, "ah, this is something we built."

## An analogy: headquarters' recipe and the store's special sauce

A restaurant analogy makes this easier to grasp. Say headquarters hands down a standard recipe. It tastes great and checks every box — except for one thing: it's missing the spicy sauce your regulars keep asking for.

At this point, you have two options.

**Modification** means tearing into headquarters' recipe itself — equivalent to directly modifying SAP's standard program. It's risky, and if headquarters later updates the recipe, conflicts can occur.

**CBO development** means leaving headquarters' recipe untouched and building your own special sauce on the side, to go with it. You add your own character without damaging the original menu item. This is how CBO (Z-code) operates.

## Light and shadow — the pros and cons of CBO

CBO can be either the hero that boosts a company's operational efficiency, or the culprit that slows the system down.

**Its strength is flexibility.** It's hard for an SAP standard used by countless companies worldwide to perfectly match your company's way of working. In a situation like "our approval process has five stages, and the standard doesn't cover that," CBO is a lifesaver. Since it doesn't touch the standard program directly, system stability is preserved, and there's less risk of conflict when SAP is upgraded.

**Its weakness is the management burden.** Building a CBO isn't the end of the story — it needs continuous upkeep as regulations or business needs change. Once these CBOs pile up one after another, they can turn into a "black box" that nobody remembers the reason for. It gets even worse once the person who built it leaves the company. Building CBOs freely whenever they seem needed also makes the system progressively heavier and slower.

## The real-world dilemma — standard T-code vs. Z-code

That's the theory, but the same question keeps coming up on the ground: should business users be trained on the standard T-code, or is it enough to just teach them how to use the Z-code? Most tasks can be handled fine through Z-code, and since company rules are already baked in, it's easier to control. Standard T-codes, on the other hand, are powerful, but if everyone uses them differently, the process can end up tangled.

**Z-code is like a friendly manager's checklist.** Your store's own rules — blocking certain values under certain conditions, auto-filling required fields — are already built in, so staff just follow the steps and enter data. Fewer mistakes, easier work.

**A standard T-code is like a powerful all-purpose kitchen tool.** It has a lot of functionality and is efficient in the right hands, but it can cause trouble if used without a full understanding. It doesn't block your company's detailed rules, so the chance of a wrong entry is higher than with Z-code.

## There's no single right answer, only balance

So is it the right answer for everyone to just use standard T-codes? Not really. If everyone only used the standard, important business rules baked into the Z-code could get ignored, and that comes back around as unexplained data mismatches at month-end close or year-end reporting.

In the end, the answer isn't "which side is right" — it's "how do you capture the strengths of both while minimizing the weaknesses."

![Diagram comparing the characteristics of a standard T-code versus a Z-code (CBO)](/images/sap-cbo-comparison.jpg)
*Figure 1. The difference between a standard T-code (all-purpose tool) and Z-code (custom assistant)*

Laying out the character, strengths, and weaknesses of each in a table makes the difference clearer.

| | Standard T-code | Z-code (CBO) |
|---|---|---|
| Character | All-purpose kitchen tool | Friendly checklist |
| Strength | Powerful and general-purpose | Company rules already built in |
| Weakness | Hard to control and manage | Turns into a black box as it accumulates |
| Best fit | Standard tasks, infrequent work | Repetitive tasks, company-specific rules |

*Table 1. Comparing the character of standard T-codes and Z-code*

## Rabbit's Takeaway

CBO (Z-code) is a useful tool for giving a company exactly the functionality it needs. But without a plan and management principles, it's also a double-edged sword that can weigh the system down.

Before building a CBO, it always helps to ask: "Does this really need to be a CBO?" "Could standard functionality or configuration handle this instead?" "If we build this now, will we actually be able to manage it well later?" Build the CBOs you truly need, but pair them with development standards and documentation — that's how to turn the love-hate relationship with Z-code into something you can actually love. 😎

**Read more**

- [SAP PP T-codes: kitchen workflow organized by process](/en/blog/sap-pp-tcode)
- [SAP T-code: how to quickly call up a kitchen's regular menu items](/en/blog/sap-tcode-basics)

<!-- Related posts: prerequisite=; related=sap-pp-tcode,sap-tcode-basics; deepens= -->
