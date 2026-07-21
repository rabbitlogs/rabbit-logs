---
title: "SAP field names: reading them like recipe card ingredient names"
mapTitle: "SAP field names"
description: "Why SAP field names like AUFNR and MATNR look like alien code, and an easy way to decode them — explained through the ingredient names on a kitchen recipe card."
pubDate: "2026-06-18"
category: "study"
series: "Learning SAP through a restaurant"
level: "beginner"
tags: ["SAPLearning", "SAPFieldNames", "SAPTables", "AUFK"]
---

Hi, this is Rabbit! 🐰

You hand a recipe card to a new kitchen hire, and after staring at it a while, they ask: "Chef, what on earth is 'AUFNR'?" It's the exact same expression someone new to SAP makes staring at field names on screen. 'AUFNR', 'MATNR', 'WERKS' — these short, alien-looking words. What do they actually mean?

The truth is, they only look unfamiliar because they're German abbreviations. Once you know the rules behind <strong class="key">field names</strong>, an unfamiliar screen stops feeling so intimidating. Today, centered on the **AUFK table** — closely related to [SAP PP master data: understanding the 4 essentials](/en/blog/sap-pp-master-data) — I'll break down SAP field names using the analogy of recipe card ingredient names.

> **3-line summary**
> - SAP field names are German abbreviations — like a recipe card's ingredient names, they're fixed symbols that hold specific information in a specific spot.
> - In the AUFK table, fields like AUFNR, AUART, and WERKS mean order number, order type, and production location, respectively.
> - Because SAP started in Germany in 1972, the tradition of using German abbreviations to save memory space has carried through to today.

[[TOC]]

## Why field names are like recipe card ingredient names

Picture a restaurant's recipe card. It needs exact ingredients and amounts — "kimchi 300g," "pork 150g" — for anyone to follow it and make the dish. If it just said "ingredient 1," "ingredient 2," you couldn't complete the dish at all.

SAP field names work the same way. In SAP, "creating a production order" is like filling out a complete recipe card. Field names like AUFNR (order number) and MATNR (material number) are the "ingredient names" printed on that card. They're fixed symbols that tell the system exactly, "put the order number here."

### Reading the AUFK table's recipe card

Today's main dish is the "production order" recipe card — the `AUFK` table. It's the core table holding a production order's header information. Let's look at what "ingredients" it contains.

![Diagram mapping the AUFK table's key fields to recipe card ingredient names](/images/sap-field-names-01.jpg)
*Figure 1. AUFK table's key fields — read as recipe card ingredient names*

Rather than listing fields at random, grouping ones with similar character makes the pattern easier to see. And writing out the original German alongside each one makes it instantly clear why those three letters ended up there.

**① Identification info** — the ingredients that tell you "what" this order is

| Field | German origin | Meaning | Restaurant analogy |
|---|---|---|---|
| `AUFNR` | Auftrag + Nummer | Order number | Order slip number |
| `AUART` | Auftrag + Art | Order type | Cuisine type (Korean, Chinese, Western) |
| `AUTYP` | Auftrag + Typ | Order category | Order form category |

**② Time and responsibility info** — the ingredients that tell you "when, and whose responsibility"

| Field | German origin | Meaning | Restaurant analogy |
|---|---|---|---|
| `WERKS` | Werk | Plant (factory) | The kitchen doing the cooking |
| `GSTRP` | Geplant + Start + Termin | Basic start date | Scheduled cooking start time |
| `GLTRP` | Geplant + Liefer + Termin | Basic finish date | Scheduled completion time |
| `KOSTV` | Kosten + Verantwortlich | Responsible cost center | The team responsible for the cost |

**③ History and status info** — the ingredients that tell you "how the recipe card has been managed"

| Field     | German origin           | Meaning     | Restaurant analogy          |
| ------- | ---------------- | ----- | ---------------- |
| `ERNAM` | Erfasst von      | Created by   | The chef who first wrote the recipe     |
| `ERDAT` | Erfasst am       | Created on   | The date the recipe was first written     |
| `AENAM` | Geändert von     | Changed by   | The chef who last edited the recipe |
| `AEDAT` | Geändert am      | Last changed on | The date the recipe was last edited |
| `LOEKZ` | Löschkennzeichen | Deletion flag | The "discontinued" mark on a menu       |

*Table 1. AUFK table's key fields — grouped by identification, time/responsibility, and history/status*

Look closely at the middle column — the German origin. `AUFNR` isn't something you just memorize; it's simply the front part of **Auftrag** (order) + **Nummer** (number) stitched together. `GSTRP` is the same kind of combination: **Geplant** (planned) + **Start** + **Termin** (schedule). Break the original word down once, and the next time you run into a similarly patterned field, you can guess the meaning without memorizing it.

## Why German abbreviations, of all things

This is a question a lot of people wonder about: "Why are SAP field names German abbreviations instead of English?" The answer is simple. Because SAP is a German company.

SAP started in Germany in 1972. Back then, it was common for computers to have less than 1MB of storage, and developers had to conserve every bit of space they could. Taking the first letters of German words and abbreviating them was highly efficient in that environment. Auftrag (order) became AUF, Material became MAT, and so on. That tradition has carried through to today's SAP field names.

> 💡 **Key point**: Just looking at the first three letters of a field name often gets you close to its meaning, since patterns like AUF (order), MAT (material), and WERK (plant) repeat throughout.

## Rabbit's Takeaway

Trying to memorize field names one by one is a losing game. Instead, build the habit of asking, "what ingredient is this?" See AUFNR, and read it as "the order-number ingredient." See WERKS, and read it as "the kitchen-location ingredient."

==Once this way of reading clicks, even a table you've never seen before stops feeling like alien code.== A chef who can read a recipe card picks up a new dish quickly — and a practitioner who knows the rules behind field names reads an unfamiliar screen just as fast. 😎

**Read more**

- [SAP data types: sorting recipes, ingredients, and order slips](/en/blog/sap-data-types)
- [SAP T-code: calling up your regular kitchen orders fast](/en/blog/sap-tcode-basics)

<!-- Related posts: prerequisite=sap-data-types; related=sap-tcode-basics; deepens= -->
