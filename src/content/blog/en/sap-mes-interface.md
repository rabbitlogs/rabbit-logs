---
title: "SAP MES interfaces: the waiter's craft of connecting floor and kitchen"
mapTitle: "SAP MES interfaces"
description: "The interface is the channel SAP and MES use to exchange data. This post breaks down the structural difference between RFC and PI/PO, and how to choose between synchronous and asynchronous, from a hands-on practitioner's view."
pubDate: "2025-07-30"
category: "study"
series: "SAP MES series"
level: "beginner"
tags: ["SAPLearning", "SAPMES", "SAPRFC", "SAPPI"]
---

Hi, this is Rabbit! 🐰

The floor manager takes an order. But there's no way to get it to the kitchen. Running back there in person means the next customer waits, and shouting across the room throws off the whole floor. For a restaurant to actually run, there has to be a waiter between the floor and the kitchen — someone who takes the order to the kitchen and brings the finished dish back out.

Between SAP and MES, the **interface** plays that waiter's role. When a project team debates "RFC or PI/PO," or "synchronous or asynchronous," that's exactly the conversation about how to run the waiter.

> **3-line summary**
> - An SAP MES interface is the connecting channel the two systems use to exchange data.
> - There are two main connection methods: RFC (a direct line) and PI/PO (central dispatch).
> - Communication style splits into synchronous (wait for a response) and asynchronous (hand it off and move on), combined to fit the task.

[[TOC]]

## Why an interface is needed at all

SAP and MES are separate systems built by different companies. Their data formats, communication protocols, and even their "languages" all differ. Connecting them directly without an interface would require each system to understand the other's language, and in practice, that's almost never how it's built.

In restaurant terms: the order form the floor manager (SAP) uses and the cooking instruction sheet the kitchen (MES) uses are different formats. Without a waiter (the interface), the floor manager would have to rewrite every order into kitchen language by hand — inefficient, and error-prone.

==The interface handles this translation and delivery automatically, and also confirms that the data actually made it through.== When an interface breaks, inventory data stops matching and production results don't reach SAP, throwing off cost calculations.

## RFC: the direct-line method

<strong class="key">RFC (Remote Function Call)</strong> is how SAP calls a function on MES directly. Nothing sits in between — it's a straight connection. Think of it as a direct phone line.

SAP calls MES and asks, "do we have 100 units of Product A in stock right now?" MES checks the warehouse and answers immediately: "yes, 100 units." SAP doesn't move on to the next task until it gets that answer back.

> 💡 **Key point**: RFC is fast and simple. Because it's a direct connection, there's no communication lag, and you get real-time confirmation of results.

The downside is just as clear, though. If MES is undergoing maintenance or responding slowly, SAP has to sit and wait right there. A failure on one side propagates straight to the other. This weak point becomes more pronounced as the system grows more complex.

RFC is simple and fast, but once you're connecting more than two systems, or operational stability matters more, it's worth considering PI/PO instead.

## PI/PO: the central-dispatch method

<strong class="key">PI/PO (Process Integration / Process Orchestration)</strong> places a middle dispatch system between SAP and MES. All communication passes through this middle layer. Think of it as an all-purpose interpreter managing every conversation from a central point.

When SAP sends a message, PI/PO receives it, converts it into a format MES understands, and passes it along — and the same happens in reverse. The floor manager (SAP) hands an order to the waiter (PI/PO), who translates it into kitchen language and delivers it to the kitchen (MES).

PI/PO adds one more layer of structure compared to RFC, but there are three reasons it's often preferred on the ground.

- **Stability**: if MES goes down briefly, PI/PO holds onto the message and resends it once things are back up. No data gets lost.
- **Flexibility**: it can connect simultaneously with multiple systems beyond MES, like a WMS (warehouse management system) or QMS (quality management system) — like an interpreter fluent in several languages, handling more destinations without strain.
- **Monitoring**: every communication is logged in PI/PO, making it easy to trace when, where, and what error blocked a piece of data.

These three strengths are exactly why large-scale manufacturing projects tend to favor PI/PO.

![Comparison diagram of SAP MES interface structures — RFC vs. PI/PO connection methods](/images/sap-mes-interface-01.jpg)
*Figure 1. RFC versus PI/PO structure*

## Synchronous vs. asynchronous: choosing a conversation style

Once you've settled on a connection method (RFC or PI/PO), the next decision is communication style.

**Synchronous**: like waiting for the "read" indicator to disappear on a chat message. SAP sends a request and pauses everything until MES responds. This is used when you need a real-time answer — for example, confirming that semi-finished goods are actually in stock before creating a production order.

**Asynchronous**: the "reply whenever" approach. SAP dumps hundreds of today's production plans onto MES at once and moves on to the next task without waiting for a response. This fits large-volume production plans that need to get delivered reliably.

![Comparison diagram of SAP MES interface communication styles — synchronous vs. asynchronous](/images/sap-mes-interface-02.jpg)
*Figure 2. Synchronous versus asynchronous communication*

> ⚠️ **Note**: With asynchronous communication, SAP can't immediately confirm right after sending whether MES actually received it. A separate monitoring or error-alert system needs to be designed alongside it.

==There's no fixed rule that RFC beats PI/PO, or synchronous beats asynchronous. Combining synchronous for cases that need real-time confirmation with asynchronous for cases that need reliable bulk delivery is the heart of interface design.==

## Rabbit's Takeaway

Assuming developers can just design the interface on their own is only half right. Which data needs to move when, in which direction, and how often — the business side knows that better than anyone.

Having a clear answer to "does this task need real-time confirmation, or does reliable bulk delivery matter more" makes conversations with developers far more concrete. When an SAP PP practitioner can bring well-defined requirements into an interface design meeting, the quality of the whole project changes. 😎

**Read more**

- [SAP MES: the perfect division of labor between the head chef and the kitchen team](/en/blog/sap-mes-role)
- [SAP Activity and CNF: reporting the kitchen log back to the head chef](/en/blog/sap-activity-cnf)

<!-- Related posts: prerequisite=sap-mes-role; related=sap-activity-cnf; deepens= -->
