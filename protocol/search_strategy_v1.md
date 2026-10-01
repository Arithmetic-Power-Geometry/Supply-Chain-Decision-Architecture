# Systematic Search Strategy — Version 1.0

Status: PRE-REGISTERED INTERNAL PROTOCOL
Freeze date: 2026-10-01

## Purpose
Construct a broad, reproducible corpus of supply-chain-management research suitable for testing the Supply Chain Decision Architecture (SCDA), rather than retrieving only papers that already use decision-oriented terminology.

## Core databases
Primary retrieval:
1. Scopus
2. Web of Science Core Collection

Supplementary discovery/verification:
- IEEE Xplore
- ScienceDirect
- SpringerLink
- Wiley Online Library
- Taylor & Francis Online
- INFORMS
- publisher/DOI pages
- backward and forward citation chaining

Supplementary sources do not replace the primary-database search counts used in the PRISMA flow.

## Search fields
Title, abstract, and author keywords wherever database syntax permits.

## Search blocks

### Block A — Domain anchor
("supply chain management" OR "supply chain" OR "supply network")

### Block B — Decision/problem vocabulary
(decision* OR planning OR schedul* OR sourcing OR procurement OR production OR inventory OR transport* OR logistics OR distribution OR fulfillment OR coordination OR collaboration OR disruption OR risk OR resilien* OR sustainab* OR circular* OR visibility OR traceability)

### Block C — Analytical/computational vocabulary
(optim* OR simulation OR analytic* OR forecast* OR "machine learning" OR "artificial intelligence" OR "deep learning" OR "digital twin*" OR blockchain OR "internet of things" OR IoT OR autonomous OR agent* OR "generative AI" OR "large language model*")

### Block D — Management/theory vocabulary
(strategy OR governance OR relationship* OR integration OR capability OR performance OR trust OR collaboration OR organization* OR theory OR empirical)

## Retrieval families
To avoid technology bias, execute multiple query families and union the results.

F1 — Broad SCM:
A

F2 — SCM decisions/operations:
A AND B

F3 — SCM analytics/computation:
A AND C

F4 — SCM management/theory:
A AND D

The broad F1 search is essential: papers are not excluded merely because they lack modern decision, technology, or theory terminology.

## Time coverage
No lower year cutoff in the broad historical search. Retrieval continues through the final search date in 2026.

## Document types
Primary quantitative corpus: peer-reviewed journal articles.
Reviews are stored separately in the review-of-reviews corpus.
Conference papers may be retained in a supplementary frontier set when required for fast-moving computer-science topics, but are not silently mixed into the primary journal corpus.

## Language
English for the primary coded corpus. Language restriction must be reported as a limitation.

## Screening
Stage 1: automated/exact deduplication by DOI, then normalized title.
Stage 2: title/abstract eligibility screening.
Stage 3: full-text eligibility.
Stage 4: quality/provenance check and SCDA codability assessment.

## Inclusion
Include when the study materially examines a supply-chain-level phenomenon, decision, coordination mechanism, model, managerial capability, technology, outcome, or evidence relationship.

## Exclusion
Exclude:
- studies using "supply chain" only as incidental context;
- isolated logistics/production technical problems without meaningful supply-chain implication;
- editorials, news, promotional pieces;
- duplicate records;
- records without sufficient scholarly metadata;
- review articles from the primary-study corpus (retain separately).

## Citation chaining
Backward and forward citation chaining is conducted for:
- landmark studies;
- major reviews;
- papers that introduce a new theoretical, methodological, or technological category not represented in the current corpus.

Every chained inclusion receives provenance.

## Anti-bias rule
Search terms and eligibility criteria are frozen before quantitative SCDA comparison. Later amendments require a versioned protocol change with rationale and must be tested through sensitivity analysis.

## Search log
For every database/query record:
database; exact query; fields; filters; execution date; result count; export file; notes.

## Corpus freeze
The corpus is frozen only after deduplication, eligibility screening, provenance validation, and saturation/coverage diagnostics are complete.
