# Supply Chain Decision Architecture

## 1. Motivation

Supply-chain scholarship is commonly partitioned by function, technology, industry, or method. This can obscure a more fundamental common object: the **decision**.

The Supply Chain Decision Architecture (SCDA) treats supply-chain management as a structured decision system. It separates:

1. **what decision must be made**,
2. **where in the supply chain it occurs**,
3. **what objective it serves**,
4. **what analytical method is used**,
5. **what technology enables it**, and
6. **what level of evidence supports the claimed effect**.

## 2. Formal representation

A study or operational decision instance is represented as

```
D = (L, P, F, O, T, M, E, V, I)
```

where:

- **L — Decision level:** strategic, tactical, operational, real-time/autonomous
- **P — Process:** plan, source, make, store, move, deliver, return, recover, enable
- **F — Flow:** material, information, financial, knowledge, risk, carbon
- **O — Objective:** cost, service, quality, speed, flexibility, resilience, sustainability, trust
- **T — Theory:** organizational, economic, behavioral, systems, resource-based, transaction-cost, information-processing, or other declared lens
- **M — Method:** conceptual, empirical, optimization, simulation, statistics, machine learning, artificial intelligence, multi-agent/autonomous
- **E — Enabling technology:** ERP, RFID, IoT, cloud/edge, blockchain, digital twin, AI platform, or none
- **V — Evidence maturity:** conceptual, synthetic, simulation, benchmark, case study, observational, pilot, deployed, longitudinal
- **I — Industry/context:** manufacturing, retail, healthcare, food, automotive, semiconductor, energy, humanitarian, construction, public sector, or general

## 3. Decision cycle

The architecture models the operational logic of supply-chain management as:

```
Sense → Predict → Plan → Source → Make → Move → Deliver → Return → Recover → Learn
```

This is not intended as a rigid process sequence. It is a decision-oriented abstraction that supports comparison across disciplines.

## 4. Separation principle

SCDA distinguishes four layers that are frequently conflated:

```
Problem → Decision → Method → Technology
```

For example, demand uncertainty is a problem; inventory replenishment is a decision; stochastic optimization is a method; and an AI-enabled planning platform is an enabling technology.

## 5. Evidence principle

A claimed capability should not be treated as equivalent to demonstrated impact. SCDA therefore records evidence maturity independently from method or technology.

## 6. Comparative propositions

The software implementation evaluates the following research propositions:

- **P1 — Decision-centered representation improves cross-disciplinary comparability** relative to technology-only or function-only categorization.
- **P2 — Multi-dimensional coding reduces category collision** in heterogeneous SCM studies.
- **P3 — Evidence maturity is orthogonal to technological sophistication.**
- **P4 — Technology-centered taxonomies systematically underrepresent managerial and organizational dimensions.**
- **P5 — Decision architecture exposes research gaps as sparse combinations of decision, objective, method, and evidence.**

## 7. Evaluation strategy

The repository tests SCDA against simplified baseline taxonomies:

- function-only classification,
- technology-only classification,
- method-only classification.

Evaluation focuses on:

- coverage,
- collision rate,
- distinguishability,
- consistency,
- deterministic reproducibility,
- ability to expose evidence gaps.

The objective is not to claim superiority from taxonomy size alone, but to test whether the additional dimensions produce materially better analytical separation.
