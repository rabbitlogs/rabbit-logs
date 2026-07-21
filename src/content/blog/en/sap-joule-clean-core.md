---
title: "SAP Joule and Clean Core: clean the kitchen before you add the new dish"
mapTitle: "SAP Joule & Clean Core"
description: "Using SAP's AI assistant Joule assumes Clean Core, and getting to Clean Core means cleaning up accumulated Z-code first. Notes from SAP NOW AI Tour 2025 Korea on the real order of AI adoption, from a practitioner's view."
pubDate: "2026-01-11"
category: "operations"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPOperations", "SAPJoule", "CleanCore", "SAPBusinessAI"]
---

Hi, this is Rabbit! 🐰

Adding a single new dish to the menu can, every so often, turn into rebuilding the whole kitchen. The customer only sees the plate, but the head chef knows that serving that one plate might mean rearranging the stove layout and rethinking how ingredients move through the room.

That's exactly the thought I had this past July, the first time I really got a close look at **Joule**, SAP's AI assistant, at **SAP NOW AI Tour 2025 Korea**. The new dish looked genuinely appetizing — the question was whether our kitchen could actually handle it. Today I want to lay out what mattered most from that day: Joule and **Clean Core**.

The short version: **AI adoption runs backwards.** What you want to use sits at the very top. What you actually need to touch sits at the very bottom.

> **3-line summary**
> - Joule is an "AI assistant built for the SAP system," operated through natural-language instructions.
> - Using Joule well effectively requires **Clean Core** as a precondition.
> - Getting to Clean Core means **cleaning up accumulated Z-code** first — this is less a feature rollout and more a system rebuild.

[[TOC]]

## SAP Joule, an AI assistant built for the system

**Joule** is an "AI assistant built for the SAP system." Give it a plain-language instruction — "put together this quarter's sales report" or "find this customer's open orders" — and Joule digs through the system and hands back the result.

In kitchen terms, it's a sous-chef who has every ingredient's location and every recipe memorized, so a single word gets you exactly what you need. No more hunting through shelves or tracking down yesterday's delivery — you just say "grab that" and it's done. It works this way across everything SAP touches: finance, procurement, supply chain, HR, and more.

The Joule demo I saw at SAP NOW AI Tour 2025 Korea was genuinely impressive. Watching a single natural-language query pull data across multiple modules made me think, "this could actually change how we work." The problem is that reality catches up before that thought even fades. This sous-chef **only performs at its best in a kitchen that's already organized.**

## Clean Core: the condition Joule needs to work

For Joule to work intelligently, the system underneath it has to stand on a consistent set of rules. That rule set is called **Clean Core**.

The concept is easy to grasp through a smartphone analogy. We don't go tearing into the operating system itself, whether it's iOS or Android. Whatever functionality we need, we get as an app from the app store. Clean Core works on the same logic. **Keep the core S/4HANA system clean, exactly as standard**, and attach whatever custom development the company needs as an app on an external platform like BTP (Business Technology Platform).

Keeping the core clean buys you two things. SAP can upgrade the system with fewer conflicts, and a standards-based AI like Joule can read the system predictably. It's the same reason a sous-chef doesn't get lost — the shelves are arranged exactly to headquarters' standard layout.

So the order falls into place: **want to use Joule → Clean Core is the precondition.** But the real gate sits one step further back.

## The real gate: years of accumulated Z-code

![Dependency diagram running from SAP Joule to Clean Core to Z-code cleanup. The goal sits at the top (Joule), but the work has to start at the bottom (Z-code)](/images/clean-core-dependency.jpg)
*Figure 1. The backwards order of AI adoption. The goal sits at the top (Joule), but the work has to start at the bottom (Z-code).*

Many companies' systems have already drifted well away from standard. That's because, in order to handle work that standard functionality alone couldn't cover, companies have spent years piling up custom code they built themselves — [Z-code, or CBO](/en/blog/sap-cbo-z-program). Corners of the system end up filled with programs whose names start with "Z."

Each individual piece of Z-code was a reasonable call at the time. It was a house special sauce, built to match a regular customer's taste. Approval steps more complex than standard, fields the industry needed that the standard screen didn't have — one request from the business at a time, and it added up.

But once hundreds of these sauces have piled up, going back to headquarters' standard recipe becomes a massive undertaking on its own. A Clean Core transition isn't "add one more feature" — it becomes **a project on the scale of tearing out and redesigning the whole kitchen.** And plenty of companies haven't even finished moving their UI to the modern Fiori-based screens yet, which makes the road even longer.

Walking out of SAP NOW AI Tour 2025 Korea, this was the thought that stuck with me. The future Joule shows off is genuinely appealing — but the road to get there is longer than it looks.

## So, where do you actually start

The starting point isn't reviewing new features — it's **diagnosing your own system.** Here's the order worth thinking through.

First, **map out the Z-code that's already piled up.** What was built, why, and for whom. Is it still actually in use, and could it be replaced by standard functionality or a configuration change? This inventory itself becomes a map of where your system actually stands today.

Second, **sort what goes back to standard from what moves to BTP.** Clean Core doesn't mean eliminating all customization. It means keeping the core system clean while rebuilding the necessary extensions the standard way (BTP, SAP Build). The key work is deciding which existing Z-code gets absorbed back into standard, and which needs to move to an external platform.

Third, **draw a phased roadmap.** Almost no company converts everything at once. The realistic approach is applying Clean Core principles to new development from day one, and cleaning up existing Z-code gradually, timed to upgrade cycles or business changes.

Rush to bring in AI before doing this, and you just add a sous-chef to a kitchen that's still a mess — the traffic only gets more tangled. Diagnosis first, tools second.

## Rabbit's Takeaway

The real gate for AI adoption isn't "how smart is Joule" — it's **"how close to standard is our system, really."**

A flashy new dish makes you want to put it on the menu right away, but the kitchen has to be able to handle it before it ever reaches a customer's table. Before getting swept up in a feature demo, open up your own system and look at the Z-code piled up inside it first. That diagnosis is page one of any AI adoption roadmap. I went to see a new dish, and ended up pulling out the blueprints for our own kitchen instead. 😎

**Read more**

- [SAP NOW AI Tour 2025 Korea: one thing I confirmed on-site](/en/blog/sap-now-ai-tour-2025)
- [SAP CBO: the head chef's secret recipe, also known as Z-code](/en/blog/sap-cbo-z-program)

<!-- Related posts: prerequisite=sap-now-ai-tour-2025; related=sap-cbo-z-program; deepens= -->
