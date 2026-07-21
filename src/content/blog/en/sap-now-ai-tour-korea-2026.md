---
title: "SAP NOW AI Tour Korea 2026: the autonomous enterprise, confirmed on-site"
mapTitle: "SAP NOW AI Tour 2026"
description: "A firsthand account of the SAP NOW AI Tour Korea keynote in July 2026 — the autonomous enterprise strategy, its prerequisites, and the temperature of the room, confirmed through Hyundai Autoever's cost-analysis case study."
pubDate: 2026-07-14
category: "operations"
series: "SAP Operations"
level: "beginner"
tags: ["SAPOperations", "SAPNOW", "EventRecap", "AutonomousEnterprise", "SAPJoule"]
---

Hi, this is Rabbit! 🐰

Same spot as this time last year: the Grand InterContinental Seoul Parnas, SAP NOW AI Tour Korea. If last year's keynote had one star — the AI assistant **Joule** — this year put a much bigger picture on stage, Joule included. The name SAP put forward this time was the **Autonomous Enterprise**.

![Wide shot of the SAP NOW AI Tour Korea 2026 venue. Three large screens display the "SAP NOW AI Tour KOREA" logo, with attendees seated at round tables throughout](/images/sap-now-ai-tour-korea-2026-01.jpg)
*Figure 1. The SAP NOW AI Tour Korea 2026 venue. All three stage screens pointed at the same phrase.*

> **3-line summary**
> - The core of this year's SAP NOW AI Tour Korea keynote was the "autonomous enterprise" strategy, resting on a three-layer structure of Joule, the Autonomous Suite, and the Business AI Platform.
> - SAP was explicit that this structure only works if clean data and governance are in place first.
> - Hyundai Autoever's cost-analysis automation case study was live proof of exactly what that prerequisite changes in practice.

[[TOC]]

## The name the keynote put forward: the autonomous enterprise

This year's keynote was led by the executive overseeing SAP's Business Data Cloud and Business AI division. Their message was clear: using AI as a simple assistive tool is different from using it as an operating model that actually runs the business. In the structure they described, people make the important calls, and AI carries out the follow-up work based on those decisions. SAP called this the <strong class="key">autonomous enterprise</strong>.

The way they explained it stood out. They used returns processing as the example: Joule analyzes a customer's return history, cost, and past return reasons and surfaces it to the person handling the case, who only has to decide whether to approve it. Once approved, the follow-up steps — paperwork, refund notification, product pickup, replacement shipment — get picked up and handled by AI agents. People focus on judgment, AI focuses on execution.

Three layers were introduced to support this structure.

- **Joule** — the single, natural-language entry point where users ask questions and kick off work
- **Autonomous Suite** — the layer of agents, apps, and data that actually executes work across finance, supply chain, procurement, HR, customer experience, and more
- **Business AI Platform** — the foundation managing data, AI models, and access permissions

SAP's picture is to start with repetitive tasks inside individual departments like finance or purchasing, and extend this structure to work that spans multiple departments over time.

## The prerequisite: the homework sitting behind the shine

One point SAP emphasized stood out here: general-purpose AI model performance alone isn't enough to automate enterprise work. For AI to actually make judgments and execute, the explanation was that <strong class="key">clean data</strong>, <strong class="key">business context</strong>, and <strong class="key">governance</strong> all need to be connected first as the basis for that judgment.

The sessions that followed dug into this point in more detail. A general-purpose large language model alone struggles to grasp an organization's structure, business rules, approval processes, or decision criteria. There was also a clear governance thread — the need to be able to check and control what data AI used and what work it performed. SAP drew a clear line here: not full automation where every judgment is handed to AI, but a structure where AI handles repetitive work while exceptions get routed to people.

> ⚠️ **Note**: For this structure to actually work, the data piled up in the system has to be organized in the first place. The Clean Core conversation that kept recurring in last year's tracks showed up again this year's keynote, under a different name but carrying the same weight.

## The numbers start explaining themselves: Hyundai Autoever

What actually changes in practice was clearer in the real-world case studies than in the theory. As a production-management practitioner, the presentation that caught my attention most was Hyundai Autoever's.

Hyundai Autoever's presentation explained why they chose profitability analysis in the controlling area as their first proof-of-concept (PoC) project. Until now, the business side had been building business plans in Excel, collecting them by email, and manually cross-checking them against actual results. This process of reconciling plan against actuals is a familiar scene at any company that deals with cost and profitability, regardless of industry.

In this PoC, they fed plan data directly into the SAP system and had Joule, the AI assistant, explain the causes of plan-versus-actual variance and profit/loss changes in natural language. Work that used to mean people manually cross-checking numbers to figure out why they came out a certain way now starts with AI flagging the likely cause first. They said the scope will expand going forward to predicting slow-moving/obsolete inventory and automating parts investigation in the purchasing and materials area.

This case lines up precisely with the prerequisite covered earlier. For AI to explain the cause of a cost variance, both plan and actual data need to already exist in the system in a clean form. That explanation simply isn't possible with numbers scattered across spreadsheets and emails. It was a session that showed the big picture of the autonomous enterprise being validated, one small PoC at a time.

## Rabbit's Takeaway

Walking out of the venue last year, the question that stuck with me was, "I want to use Joule — but is our system ready to receive it?" This year, one more question got attached to that: ==how much can we actually trust the data we're handing AI as the basis for its judgment?== The name "autonomous enterprise" sounds impressive, but what actually carries that name is the quality of the data piling up in the system every single day. 😎

**Read more**

- [SAP NOW AI Tour 2025 Korea: one thing I confirmed on-site](/en/blog/sap-now-ai-tour-2025)
- [SAP Joule and Clean Core: clean the kitchen before you add the new dish](/en/blog/sap-joule-clean-core)

<!-- Related posts: prerequisite=; related=sap-now-ai-tour-2025,sap-joule-clean-core; deepens= -->
