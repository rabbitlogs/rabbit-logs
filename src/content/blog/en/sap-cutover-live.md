---
title: "SAP cutover on the ground: a record of 30 war-like hours"
mapTitle: "SAP cutover on the ground"
description: "What actually happens during an SAP cutover — rollback decisions, data mismatches, and the PP module checklist — recorded from the perspective of someone who lived through it."
pubDate: "2025-11-12"
category: "project"
series: "SAP project fundamentals"
level: "intermediate"
tags: ["SAPProjects", "SAPCutover", "SAPImplementation", "SAPDataMigration"]
---

Hi, this is Rabbit! 🐰

It's the night before a restaurant's reopening at a new location. All the equipment is in place in the new kitchen, the menu is finalized, and the staff have been trained. All that's left is to flip on the sign at dawn and welcome the first customers.

Then, past midnight, a fridge temperature sensor starts throwing errors. The new POS system turns out to have some menu prices entered wrong. The ingredient inventory list doesn't match what's actually in the fridge.

The [cutover overview post](/en/blog/sap-cutover) covered planning and preparation. This post is a record of how that plan actually collides with reality on the ground. Here's what a **cutover on the ground** really looks like.

> **3-line summary**
> - A cutover never goes exactly to plan. Unexpected problems always come up.
> - A PP module cutover requires three things to align at once: inventory conversion, open production orders, and the MES interface.
> - Rollback isn't failure. A prepared rollback beats an unprepared go-live.

[[TOC]]

## How 30 hours actually unfold

Cutovers happen over weekends or holidays, using the window when the business is closed to switch systems. But for the project team, that window is an overnight marathon.

The old system shuts down Saturday afternoon. From that point, the clock is running. Data migration scripts run in the order laid out in the runbook, and once one finishes, the next owner picks it up. When an error hits, someone tracks down the cause, fixes it, and reruns it.

==Two or three in the morning is the hardest stretch. That's usually when the daytime tension has worn off and fatigue has built up — and it's often exactly when the most critical tasks are stacked up.==

I once stayed on-site for over 30 hours straight on one project. I sat in front of a monitor watching script results come in, analyzing error logs, and syncing up with the team. I drank coffee like an IV drip and didn't get so much as a proper nap. Here's what I learned from that.

The toughest stretch on the ground is that two-to-three-a.m. window. That's when daytime tension has faded and fatigue has piled up, and it's often when the most critical data migration tasks cluster together. Big calls have to get made right when judgment is at its weakest — and that's exactly when it tends to happen.

## Rollback: the bravest decision you can make

Sometimes a cutover succeeds on the first try. Sometimes you have to decide to roll back.

One project I worked on took two failed cutover attempts, a month apart, before succeeding on the third. The first attempt failed at the opening inventory conversion stage — too many items where the actual warehouse quantity didn't match what the system showed. In restaurant terms, it's like moving ingredients into the new storeroom only to find the quantities on record don't match what's actually there. Open for business in that state, and orders go wrong and dishes don't come out from day one.

The second attempt got stuck on master data errors — critical mismatches turned up in the foundational data: business partners, material codes, pricing conditions.

Both times, we made the call to roll back.

> 💡 **Key point**: Rollback isn't a "Ctrl+Z." It's a formal declaration that the cutover is off, and it takes a month of root-cause analysis and fixes before you can try again. But forcing a go-live when you're not ready leads to far bigger chaos over the following months. The courage to decide on a rollback is what saves the project.

![SAP cutover-on-the-ground timeline diagram — flow from downtime start through the rollback decision point to go-live](/images/sap-cutover-live-01.jpg)
*Figure 1. Cutover flow and the rollback decision point*

## Why a PP module cutover is especially tricky

Every module matters, but a production (PP) module cutover requires three conditions to align at once.

**Opening inventory conversion and validation** comes first. This is the work of registering actual warehouse material quantities in SAP. It sounds simple, but thousands of material codes and quantities all have to be correct. Get even one wrong, and MRP generates the wrong purchase requisitions and the production plan goes off track.

In restaurant terms, it's moving every ingredient into the new kitchen's fridge and cross-checking the inventory list against what's physically there, item by item. If the system says you have 10kg of frozen tuna but you actually have 7kg, you're serving less tonight than what was booked.

**Migrating open production orders** comes second. Production orders still in progress in the legacy system get moved to SAP, and you confirm they flow through to MES correctly. The factory keeps running through cutover — you're handing off the "things we're making right now" that the old system was tracking until yesterday, over to SAP.

**Processing the production confirmation interface** comes third. Confirmation data that piled up in MES during downtime gets pulled into SAP and processed. The factory floor can keep running without SAP, but if those results don't make it into SAP, inventory and cost figures get tangled.

> ⚠️ **Note**: If any one of these three fails, it's hard to proceed with go-live. Opening inventory mismatches in particular stay invisible until the moment you run MRP, and then the problem explodes. Spend enough time validating data before cutover.

## Lessons from the ground

**Buffer time in the runbook isn't slack.** Build in generous buffer between tasks. More tasks run over than run on schedule. Without buffer, one delayed task pushes back everything after it.

**Set escalation criteria ahead of time.** Decide in advance what counts as "I can't solve this alone" and who to report it to. The worst outcome is someone struggling alone at three in the morning with a never-before-seen error, burning time that can't be recovered.

**Keep communication to a single channel.** During cutover, share live status in a group chat or shared dashboard. If "where are we right now?" starts flying around from every direction, things fall apart on the ground.

## Rabbit's Takeaway

When the first production order gets issued in SAP after cutover wraps up, watching that screen is a special feeling. Months of work is actually working.

But what comes next matters even more. The period right after go-live is the most fragile. Unexpected questions and errors pour in from the floor. Key people need to be there, holding the line.

Cutover isn't the end. It's that feeling of closing out the first day of business in the new kitchen — that's when the real restaurant begins. 😎

**Read more**

- [SAP cutover: moving day from the old kitchen to the new one](/en/blog/sap-cutover)
- [SAP change management: the staff has to change before the new kitchen opens](/en/blog/sap-change-management)
- [SAP UAT: the owner's final walkthrough before opening the doors](/en/blog/sap-uat)

<!-- Related posts: prerequisite=sap-cutover; related=sap-change-management,sap-uat; deepens= -->
