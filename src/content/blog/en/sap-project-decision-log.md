---
title: "SAP project decision records: the kitchen bulletin board nobody rereads"
mapTitle: "SAP project decision records"
description: "Why SAP implementation meeting minutes pile up while the reasons behind decisions disappear, and what business-side leads should actually be writing down."
pubDate: 2026-08-06
category: "project"
series: "Learning SAP through a restaurant"
level: "beginner"
tags: ["SAPProject", "SAPDecisionMaking", "SAPImplementation", "SAPMeetingMinutes"]
---

Hi, this is Rabbit! 🐰

Back when we were prepping to open a new location, there was a bulletin board on the kitchen wall. Every week, after a meeting, someone would pin up a sheet of paper. Four months in, the board was packed.

Then, about two months after opening, a problem came up — and nobody could find the answer on that board. The sheets just said things like "discussed layout" or "aligned on ordering process." What was discussed was there. **What got decided, and why, wasn't.**

This is one of the most common things that happens on SAP implementation projects. Meeting minutes pile up faithfully, while the one thing you actually need after go-live isn't in them.

> **3-line summary**
> - Project meeting minutes usually capture "what was discussed" but drop "why it was decided that way."
> - A decision with no reason attached becomes a setting nobody can explain the moment the person who made it moves on.
> - What business-side leads need to leave behind isn't the meeting content — it's <strong class="key">the reasoning behind the decision</strong>.

[[TOC]]

## The discussion survives; the decision disappears

Most project meetings get recorded. Attendees, agenda, discussion points — all laid out in a table and dropped into a shared folder. The problem is that even when there's a "Decision" column in that table, it usually ends in one line. Something like "aligned" or "proceeding pending business confirmation."

Four months later, that sentence tells the reader nothing. What was aligned on, what the alternatives were, why this option got picked — none of it's there.

So when someone asks after go-live, "why is this field set as mandatory?" — there's nobody who can answer. The record exists; the answer doesn't. This is the debt that quietly builds up while a project works its way through [SAP implementation projects: the five hurdles of opening a new store](/en/blog/sap-build-project-difficulty).

## What was said and what got understood aren't the same

When the business side says "we usually do it this way," the consultant translates that into system language as they hear it. Things quietly go sideways during that translation more often than you'd think.

Say the head chef says, "ingredients usually come in during the morning." What they meant by "usually" was "mostly, but urgent deliveries come in the afternoon too." The designer might write that down as "goods receipt happens only in the morning." Neither side lied, but the outcome diverges.

This kind of mismatch almost never shows up in the meeting itself — both sides walk away believing they agreed on the same thing. It surfaces after go-live, the first afternoon materials show up.

> 💡 **Key point**: Writing "goods receipt: morning" in the minutes won't catch this. You need "mostly mornings, but urgent cases happen in the afternoon — needs exception handling" to catch it. What needs to be recorded isn't the conclusion — it's the conditions attached to it.

## Deferred answers harden into the standard

There's always a moment where the business side says "let us think about that a bit more." Because things are busy, or because it's genuinely unclear which option is better, the decision gets deferred.

The project doesn't stop and wait. There's a schedule, so the gap has to get filled somehow — and standard functionality or another company's approach usually fills it. That's not necessarily a bad outcome. [SAP Best Practice: why you'd want to use a proven recipe](/en/blog/sap-best-practice).

The problem is that **the fact it was a choice doesn't get recorded.** The business side deliberately reviewing and picking the standard, versus the standard filling the gap because the business side never answered, look identical on screen. That's why, when it's time to change that setting later, nobody can answer "why was this set up this way."

So deferred decisions need a record too. "Business judgment deferred — proceeding with the standard approach, revisit after go-live" written down as a single line is a completely different thing from leaving nothing behind at all.

## When people change, the reasons go with them

Projects run long, and people change over the course of them. Consultants rotate off, business-side leads get reassigned, developers move to other projects.

Whatever context lived only in people's heads disappears at that point. What's left is the system configuration and minutes that say "aligned."

What's especially risky are **settings put in place to handle an exception.** If a condition was built to handle a specific situation, and that situation was never documented, whoever looks at it later just sees unnecessary complexity. They try to clean it up, and the problem it was quietly preventing comes right back.

The people who built it move on; the people who use it stay. The record is the only bridge between the two.

## What the business side needs to leave behind

The minutes a consultant writes and the record a business-side lead needs to leave behind serve different purposes. One is for project management. The other is **a record meant to be read after go-live.**

It doesn't need to be elaborate. Four things attached to every decision are enough.

- **What was decided** — the actual confirmed outcome, in a sentence
- **What the alternatives were** — including the ones considered but not chosen
- **Why this one** — which specifics of our operation drove it
- **What conditions apply** — exceptions, points to revisit later

The fourth is the one that gets skipped most often, and needed most often.

![Four things to leave behind every time a decision gets made — what was decided, what the alternatives were, why this one, what conditions apply](/images/sap-project-decision-log-01.jpg)
*Figure 1. Four things to leave behind every time a decision gets made*

This record matters especially during [SAP Fit/Gap analysis: measuring the distance between standard and your restaurant](/en/blog/sap-fit-gap), when you're measuring the distance between the standard and your own way of working and deciding what to adjust. The reasoning behind that judgment needs to survive so the gap can be revisited later.

## Rabbit's Takeaway

By the time a project wraps, there's a pile of deliverables left behind — design docs, test results, manuals. But the question that comes up most often after go-live isn't "how do I use this" — it's **"why does this work this way?"**

The first question is answered in the manual. The second one usually isn't answered anywhere.

==A system only retains as much explanation as the business side left reasons for.== No matter how good the judgment was in the room, if the reasoning behind it never gets written down, four months later it's just a setting nobody can explain. 😎

---

**Read more**

- [SAP implementation projects: the five hurdles of opening a new store](/en/blog/sap-build-project-difficulty)
- [SAP Fit/Gap analysis: measuring the distance between standard and your restaurant](/en/blog/sap-fit-gap)
- [SAP change management: the staff has to change before the new kitchen opens](/en/blog/sap-change-management)

<!-- Related posts: prerequisite=sap-build-project-difficulty; related=sap-fit-gap,sap-change-management -->
