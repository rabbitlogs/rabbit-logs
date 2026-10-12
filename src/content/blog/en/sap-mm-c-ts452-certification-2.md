---
title: "SAP MM certification C_TS452 first and second attempts failed: a wrong recipe and a broken kitchen"
mapTitle: "SAP MM certification C_TS452 attempts 1 and 2"
description: "My SAP MM certification (C_TS452) first and second attempts: machine-translated instructions, time allocation, the trap of not checking before saving, and how I filed a support case after an exam system defect and got the attempt back."
pubDate: 2026-10-13
category: "study"
series: "SAP MM certification journey"
level: "beginner"
tags: ["SAPLearning", "SAPCertification", "SAPMM", "C_TS452", "SAPExamReview"]
---

Hi, this is Rabbit! 🐰

Have you ever cooked from a foreign cookbook run through a translator? Most of it reads fine, but every now and then "2 teaspoons of sugar" turns into "2 cups of sugar." You follow the recipe exactly, and the dish still falls apart. And some days, the recipe and your hands are ready, but the kitchen's gas valve is shut.

That is what my first and second **SAP MM certification C_TS452** attempts were like: both ended in a fail. This part covers what went wrong in those two failures, focusing on what someone preparing for the same exam can avoid.

> **Three-line summary**
> - In the first attempt, machine-translated instructions, time sunk into one task, and no check before saving turned half of the tasks I thought I had finished into zeros.
> - In the second attempt, a base setting was missing from the exam system, so I could not carry out most of the tasks.
> - I filed a support case with evidence and got the attempt back the same day.

[[TOC]]

## C_TS452 first attempt: why it failed

I took the first exam in September 2026. When I pressed submit, I had no idea it would turn out that way. There were tasks I never reached, but I thought most of what I did finish was correct. Working backward from the score, **nearly half of the tasks I thought I had finished scored zero**. There were three causes.

### Machine-translated instructions

You can choose the language of the task instructions at the start. The Korean instructions are machine-translated, and **some of the numbers and structure that the grading depends on read differently from the original**. Reordered sentences made it unclear which value went where.

A SyBA exam checks whether the saved values match the instructions exactly. If the translation is wrong, you score zero even when you follow it, and because later tasks use the output of earlier ones, an entire group of tasks can fall apart.

> 💡 **Key point**: in [SAP certification exams](/en/blog/sap-exam-format) I said to turn off your browser's auto-translate. For the same reason, it is safer to choose **English for the instruction language** too. In a system whose menus and field names are in English, English instructions are also faster to compare against.

### Time sucked into one task

Three hours sounds generous, but divided by the number of sub-exercises it is **4–5 minutes per item**. I got lost in configuration screens (Customizing, setting the rules for how the system behaves) that I rarely touched at work, and spent **about 100 minutes** on a single task. In the end I either never touched the last tasks or only skimmed them.

For the record, in [SAP certification exams](/en/blog/sap-exam-format) I once wrote that it was "realistically a 40-minute-to-1-hour exam" if your practical skills are solid. For a module I was learning for the first time, that was not true. Even on my well-prepared third attempt, the tasks took 80–90 minutes, and about 2 hours with verification.

### No check against the instructions before saving

This was the most painful cause. Chased by the clock, I filled in a screen, pressed Save, and moved straight on.

- One extra zero typed into an amount field
- A required field left out, saving a result different from what was intended
- One extra step, not in the instructions, done out of work habit, so a later task did not behave as intended

The last one is like adding a seasoning that is not in the recipe because you think the customer will like it. **It is a trap that people who know the system well fall into most easily.**

![Before-and-after comparison of three things I changed after my first SAP MM certification C_TS452 attempt: from machine-translated Korean instructions to the original English, from holding on to one stuck screen to drilling stuck screens separately, and from moving on right after Save to checking before saving and confirming on the display screen after](/images/sap-mm-c-ts452-certification-2-01-v2.jpg)
*Figure 1. Three things I changed after the first attempt*

## C_TS452 second attempt: when the exam system is broken

In early October I went into my second attempt. As soon as I started the first task, an odd error appeared. I was trying to do an inventory-related step, and saving was blocked with a message to the effect that **a base setting was missing**, one that should already exist in the exam system. It was not something candidates create.

Many tasks depended on that setting, so **I could not carry out most of them**. I did only what I could, and the result was a fail.

### My mistake, or an exam system defect?

In a hands-on exam, getting an earlier step wrong and blocking a later one is common, so the first thing to do is make sure it is not your own mistake. I judged it to be a defect for three reasons.

- The setting in question was **one the instructions never asked me to create or change**
- The error appeared right after the exam started, **before I had changed anything**
- The same kind of step worked normally on the practice system

> 💡 **Key point**: if something feels off, capture the exact error message, the screen where it happened, and the time right away. When you write a support case, that is everything.

### How to file an SAP support case

After the exam, I filed an <strong class="key">SAP support case</strong> through **Create a case** in the [SAP Learning Help Center](https://learning.sap.com/helpcenter). This is what I included.

- The exam code and the date and time of the attempt
- Where the error happened, the exact message, and a screenshot of the error screen
- An explanation that the setting was outside the candidate's scope of work
- Which tasks I could not carry out because of it

To get the situation across precisely in English, I described it to an AI to produce a draft, then checked it myself for anything inaccurate before submitting. It was handled faster than I expected, and **my attempt was reissued the same day**. When the cause is not the candidate's fault, such as an exam system defect, you can get your attempt back this way.

### Why I did not retake it right away

Right after getting the attempt back, there was an open slot that same evening. But **I had no confirmation that the defect had been fixed**, so I did not go straight back in. If the same defect remained, I would just lose another attempt. Instead, I rebooked a few days later.

![SAP Certification Hub time selection screen showing 2 p.m., 5 p.m., and 8 p.m. slots on the same day](/images/sap-mm-c-ts452-certification-2-02.jpg)
*Figure 2. Several slots can be open on the same day, but it is safer not to rush until you know the defect is fixed.*

## Rabbit's Takeaway

The two failures were different in nature. The first was a failure to execute what I knew by the instructions; the second was an accident out of my hands. Yet the lesson was the same. ==The habit of checking the instructions against the screen all the way through prevents your own mistakes and also proves a system defect.== Showing that the kitchen was broken also comes down to careful records 😎

---

**Read more**

- [SAP MM certification C_TS452 exam structure: before you step into the practice kitchen](/en/blog/sap-mm-c-ts452-certification-1)
- [SAP MM certification C_TS452 practice and passing: the same dish, faster and more precisely](/en/blog/sap-mm-c-ts452-certification-3)
- [SAP certification exams: from a written test to a hands-on kitchen exam room](/en/blog/sap-exam-format)

<!-- Related posts: prerequisite=sap-mm-c-ts452-certification-1; related=sap-exam-format; deepens=sap-mm-c-ts452-certification-3 -->
