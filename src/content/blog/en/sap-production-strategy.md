---
title: "SAP production strategies: MTS vs. MTO, or buffet vs. steakhouse"
mapTitle: "SAP production strategies"
description: "The difference between MTS (make-to-stock) and MTO (make-to-order) — the core of SAP production strategy codes — explained through the buffet and steakhouse analogy, along with how each strategy affects lead time and inventory management."
pubDate: "2025-08-31"
category: "study"
series: "SAP PP fundamentals"
level: "beginner"
tags: ["SAPLearning", "SAPPP", "ProductionStrategy", "MTS", "MTO"]
---

Hi, this is Rabbit! 🐰

Run a restaurant, and this question never goes away: make it ahead of time, or make it after the order comes in?

A buffet preps ahead. It forecasts how many guests will show up and when, prepares the food in advance, and guests simply serve themselves the moment they arrive. A steakhouse, on the other hand, starts cooking only after the order comes in — because everyone wants their steak cooked differently, and a steak grilled ahead of time just isn't the same.

In SAP, these two ways of operating are defined as the <strong class="key">production strategy (Planning Strategy)</strong>.

> **3-line summary**
> - **MTS** (Make-to-Stock): forecast demand and produce ahead of time. Faster delivery, but carries inventory risk.
> - **MTO** (Make-to-Order): produce only after an order comes in. No excess inventory, but a longer lead time.
> - Even within a single company, different items can be assigned different strategies based on their characteristics.

[[TOC]]

## MTS: prepping ahead, buffet-style

A buffet kitchen is busy from the morning. Anticipating a rush at the lunch peak, it prepares large batches of fried rice, doenjang jjigae (soybean paste stew), and braised short ribs well in advance. The moment guests arrive, they serve themselves whatever they want right away. No waiting required.

This is **MTS** (Make-to-Stock): forecasting demand, producing ahead of time, and shipping from stock once orders come in.

In SAP, this is generally handled with **strategy code 10**. MRP builds a production plan based on sales forecasts and builds up finished-goods inventory. When an order comes in, it ships straight from the warehouse.

**Pros:** delivery is fast — you can ship the moment an order arrives. Production lines also run more steadily.

**Cons:** if the demand forecast is off, inventory piles up. You end up with a mountain of food nobody's buying. That means storage costs and losses from waste.

MTS suits **standardized products** — items where the spec is identical no matter who buys it, like A4 paper, bottled water, or general-purpose screws. Making these ahead of time is simply more efficient.

## MTO: order first, then start grilling — the steakhouse

A steakhouse works differently. The moment a guest sits down and says "sirloin, medium rare, please," that's when the kitchen pulls the meat from the fridge and starts grilling. Everyone wants their steak done differently, and a steak grilled ahead of time just doesn't taste as good.

This is **MTO** (Make-to-Order): production starts only after the customer's order comes in.

In SAP, **strategy code 20** is the standard MTO approach. Once a sales order is created, a production order is generated based on it. No inventory gets built up.

**Pros:** almost no inventory, since you only make what's been ordered. You can also accommodate special customer requirements.

**Cons:** lead time is longer — customers have to wait, since production doesn't start until the order comes in. The production schedule also becomes uneven, following the rhythm of incoming orders.

MTO suits **customized products** — items where standard inventory is hard to maintain, like industrial machinery built to customer spec, custom-made furniture, or specialty chemicals.

![Diagram comparing SAP production strategies MTS vs. MTO — the difference in lead time and inventory characteristics between the buffet (make-to-stock) and steakhouse (make-to-order) models](/images/sap-production-strategy-01.jpg)
*Figure 1. Comparing lead time and inventory characteristics between MTS and MTO*

## A middle ground: preparing only up to the semi-finished stage

Is there a way to capture both the buffet's speed and the steakhouse's customization at the same time?

Think of a sandwich shop. Bread, cheese, ham, and vegetables are all prepped in advance. When a customer says "add chicken, hold the pickles," the shop assembles the order right there from the prepped ingredients. Because the ingredients are already ready, you don't wait too long, and you still get it made to your taste.

In SAP, this is implemented with **strategy code 40 (planning with final assembly)**.

Semi-finished goods and key materials are produced ahead of time based on demand forecasting, just like MTS. Final assembly only happens after the customer order comes in. This keeps finished-goods inventory low while still meeting delivery expectations reasonably well.

There's also an approach that waits even further into the process before production starts. **Strategy code 50 (planning without final assembly)** plans only up to the semi-finished stage, with everything after that starting only once an order comes in. It's a middle ground that raises the level of customization while still trying to shorten lead time.

In practice, it's common to mix different strategies for different items within the same plant — standard parts run on MTS, custom finished goods on MTO, and shared semi-finished goods on strategy 40. SAP supports configuring this combined approach differently for each item.

> 💡 **Key point**: The strategy code is set on the MRP tab of the material master. Even within a single company, different items can have different strategy codes — for example, running standard parts as MTS (10) and custom products as MTO (20) within the same plant.

## Which strategy fits your company

There are three factors to weigh when choosing a strategy.

**First, how standardized is the product?** If it's identical no matter who buys it, MTS fits. If specs vary by customer, MTO fits.

**Second, what's the required delivery speed?** If customers expect immediate or very short lead times, you need MTS. If some waiting is acceptable, MTO becomes a viable option too.

**Third, can you absorb the inventory cost?** If you can afford to hold finished-goods inventory and your demand forecasting is reasonably accurate, MTS works in your favor. If inventory cost is a heavy burden or demand swings wildly, MTO is the safer choice.

> ⚠️ **Note**: A strategy code isn't something you set once and forget. It needs revisiting whenever business conditions change. If delivery-time competition intensifies, consider shifting from MTO to MTS; conversely, if inventory losses grow, consider moving from MTS to MTO or strategy 40.

## Rabbit's Takeaway

The strategy code numbers feel unfamiliar the first time you encounter them — 10, 20, 40, 50 — with no obvious pattern.

But underneath it all, there's really just one question: **"When does production actually start?"**

==Make it before the order comes in, and it's MTS. Make it after, and it's MTO. Make it partway ahead and finish the rest after the order arrives, and it's strategy 40.== Remember this one rule, and you won't lose the thread even if the code numbers get confusing.

Choosing between a buffet and a steakhouse isn't just a difference in operating style — it's a decision about what you're promising your customer. 😎

**Read more**

- [SAP PP: how a kitchen's production plan comes together](/en/blog/sap-pp-overview)
- [SAP MRP: planning materials like a restaurant prepping a big group order](/en/blog/sap-mrp)
- [SAP planned order vs. production order: the meal plan and the actual cooking ticket](/en/blog/sap-planned-vs-production-order)

<!-- Related posts: prerequisite=sap-pp-overview; related=sap-mrp,sap-planned-vs-production-order; deepens= -->
