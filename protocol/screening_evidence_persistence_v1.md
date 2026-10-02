# Screening Evidence Persistence v1

GitHub is the authoritative persistence layer for SCDA screening decisions.

## Storage model

Candidate bibliographic metadata are generated deterministically by the retrieval and stable-ID workflow. Screening judgments are stored separately as compact decision ledgers keyed by `record_id`.

A decision ledger records:
- stable record ID;
- Stage-1 decision;
- exclusion reason where applicable;
- study type;
- reviewer identity/role;
- confidence;
- adjudication flag.

The complete screening table is reconstructed by a deterministic join from the stable candidate corpus and the committed decision ledgers. This avoids duplicating volatile bibliographic metadata while preserving every substantive screening judgment.

## Integrity rules

1. One screening judgment per stable record ID per screening stage.
2. No row-order identifiers.
3. Exclusions require a frozen E-code.
4. Uncertain records require adjudication.
5. AI-assisted Reviewer-A judgments are explicitly labelled and do not substitute for independent second-coder reliability.
6. A batch is not counted as repository-persisted until its decision ledger is committed.
7. Stage 1 is not frozen until every candidate has one terminal Stage-1 judgment and the reconstructed ledger passes validation.
