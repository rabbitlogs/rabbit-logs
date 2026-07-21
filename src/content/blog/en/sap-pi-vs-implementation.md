---
title: "SAP PI vs. implementation: the people who plan the restaurant and the people who build it"
mapTitle: "SAP PI vs. implementation"
description: "Under the same label of 'SAP consultant,' PI (planning) and implementation (building) are completely different roles. Mapped against the process of opening a new restaurant, here's how the two worlds differ and how they balance each other."
pubDate: "2025-08-06"
category: "project"
series: "Learning SAP through a restaurant"
level: "intermediate"
tags: ["SAPProjects", "SAPConsultant", "PI", "Implementation"]
---

Hi, this is Rabbit! 🐰

Say you're opening a new restaurant location. You need two completely different kinds of people for this. One is the planner who sketches out "what concept, what layout should this place have." The other is the construction team that takes that sketch and actually builds the kitchen and brings in the equipment.

SAP projects work exactly the same way. Even under the same "SAP consultant" label, there are two groups doing completely different jobs: <strong class="key">PI</strong> (Process Innovation) and <strong class="key">implementation</strong>. Like the designer who plans the store and the contractor who builds it from the blueprint. I've been through both a production PI engagement and an SAP PP implementation myself, and based on that experience, here's why these two sides so often clash, and how to strike a balance between them.

> **3-line summary**
> - PI is the "designer" who sketches the ideal future way of working (To-Be).
> - Implementation is the "contractor" who turns that design into a working SAP system.
> - Friction between the two is inevitable, and successful projects close that gap early.

[[TOC]]

## PI: the designer who sketches the store's concept

The people who set the first stone of an SAP project are the **PI** consultants. In new-store terms, they're the planners drawing the big picture of what kind of concept the place should have. They're typically business consultants who specialize in management strategy and process innovation.

Their job is to analyze how the company works today (As-Is) and design the most ideal future way of working (To-Be). There's really one question on their mind: "For this company to operate at a global standard, how should it work going forward?"

Rather than focusing on budget or technical constraints, they concentrate on drawing the most efficient "dream blueprint." It's a bit like imagining the best possible customer experience first, then designing the store backward from there. That's why the results sometimes look bold or unconventional.

## Implementation: the contractor who turns the blueprint into a real store

The people who take PI's blueprint and run with it are the **implementation** consultants. These are technical specialists — module consultants who know specific SAP modules inside and out (FI, CO, SD, MM, PP, and so on), and [ABAP](https://www.sap.com/products/technology-platform/abap.html) developers who write the code. In store terms, they're the construction crew that takes the blueprint and actually builds the kitchen and installs the equipment.

They implement the To-Be process that PI designed as an actual SAP system. But they can't just build off the blueprint alone — they have to account for the site's infrastructure, budget, SAP standard functionality, and available staffing. It's like how even the most beautiful store blueprint still has to respect the building's actual electrical capacity and gas lines.

The implementation consultant's goal isn't a "system that only works on paper" — it's a "system that actually runs in the real world." They're the real contractors, reconciling the gap between the blueprint and reality.

## "We can't build it exactly like this"

Interestingly, PI and implementation usually belong to different organizations even within the same overall project — sometimes company A handles PI while company B handles implementation. So friction between the two worlds is almost inevitable.

Implementation consultants, running into real-world constraints, often end up saying things like this. Budget and schedule pressure produces lines like "building this feature exactly as designed would double the cost and add six more months." Missing infrastructure on-site produces "you're asking for real-time data entry, but there aren't even terminals out there yet." Limitations in SAP's standard functionality raise concerns like "this isn't in the standard system, so we'd have to build it from scratch — how do we even maintain that later?"

In the end, the ideal picture from the PI phase often gets scaled back or changed as it goes through the "reality check" of implementation. It's like how a gorgeous store blueprint still has to have its kitchen layout adjusted if the building's support columns don't line up.

## What connects the two worlds is, ultimately, balance

So is PI just dreaming while implementation stays grounded in reality? Not really. Both are essential to a project's success.

PI's "ideal" sets the direction the company should move toward — without direction, a system loses its way, the same way a store with no concept just blends into the crowd. Implementation's "reality" turns that goal into a sustainable system that actually delivers value. No matter how great the concept, a store that can't actually be built never opens its doors.

When the two worlds understand each other and find balance, ==SAP sheds its reputation as an "expensive, complicated spreadsheet" and becomes a genuine engine of digital transformation.==

![Diagram comparing the roles of PI (designer) and implementation (contractor)](/images/sap-pi-vs-implementation-01.jpg)
*Figure 1. PI draws the future blueprint; implementation turns that blueprint into reality*

## Four ways to strike the balance

Projects that go smoothly tend to follow a similar pattern.

**Bring reality into the PI phase from the start.** Have implementation specialists participate in the design phase to review technical and cost considerations together. Designing with real-world constraints in mind from day one matters.

**Take a phased approach (MVP).** Rather than trying to build every feature at once, launch the core functionality first and expand from there gradually. Landing a small win early matters. It's the same reason a new restaurant is safer starting with a few signature dishes rather than a full menu on day one.

**Prioritize standard functionality.** Lean on SAP standard features as much as possible, and keep custom development (so-called Z-code) to a minimum to reduce the maintenance burden later.

**Invest in change management and training.** Help end users genuinely understand "why we're doing it this way" and adapt to it. Even the best-designed store can't serve customers if the staff doesn't know how to run it.

## Rabbit's Takeaway

Projects succeed when PI's big picture meets implementation's practical execution — the same way a store only opens once the planner's concept meets the construction team's craft.

Having gone through both roles myself, I've come to see that neither side is simply right and the other wrong. ==Understanding each other's language is, honestly, the most practical way to make a project run smoothly.== 😎

**Read more**

- [SAP implementation projects, the five hurdles of opening a new store](/en/blog/sap-build-project-difficulty)
- [The 10 SAP modules, seeing the whole restaurant at a glance](/en/blog/sap-modules-guide)

<!-- Related posts: prerequisite=; related=sap-build-project-difficulty,sap-modules-guide; deepens= -->
