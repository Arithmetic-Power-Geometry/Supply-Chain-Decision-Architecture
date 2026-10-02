# Stage-1 Reconstruction Status — 2026-10-02

The 705-record Reviewer-A screening base has been recovered and checked locally against the stable-ID corpus.

## Current exact decision state after source adjudication

- Candidate records: 705
- Include: 659
- Exclude: 46
- Uncertain: 0
- Source-verification queue: 147/147 resolved
- Source-adjudication duplicate IDs: 0
- Conflicting adjudication decisions: 0

The 147 source-adjudication records comprise 129 includes and 18 excludes. Before those updates, the recovered post-initial-adjudication ledger contained 550 includes, 127 uncertain records, and 28 excludes. The 20 already-included adjudication records were review-layer records and remained included; the 127 uncertain records resolved to 109 includes and 18 excludes.

## Freeze status

Decision closure is complete for Reviewer A, but Stage 1 is not yet declared final/frozen.

Before freeze:
1. persist or deterministically regenerate the compact 705-record decision ledger on the branch;
2. join it to the stable candidate corpus by record_id;
3. verify 705 rows and 705 unique IDs;
4. verify zero uncertain decisions and valid exclusion codes;
5. audit primary/review routing, especially the earlier rule-based batches;
6. retain the independent second-coder requirement as a separate G4 gate.

The 659 records are Stage-1 inclusions, not the final paper corpus. Stage-2 full-text eligibility may reduce this number substantially.

## Paper trigger

Do not write the full results-driven paper yet. Paper construction begins after Stage-2 eligibility is frozen, claim-level SCDA coding is complete, independent reliability is measured, and the nested architecture/comparator/robustness/holdout tests have produced frozen outputs. Only then should the manuscript make empirical claims about K4, KS7, KSV8, or SCDA9.
