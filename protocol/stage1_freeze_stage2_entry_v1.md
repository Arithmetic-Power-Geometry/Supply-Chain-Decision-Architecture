# Stage-1 Freeze / Stage-2 Entry

Stage 1 is frozen only if `scripts/finalize_stage1.py` passes all checks.

Required:
- 705 base rows and 705 unique stable IDs.
- 147 unique adjudication overrides, all present in the base.
- terminal decisions only.
- included records routed primary/review.
- excluded records carry E01-E10.
- audited totals: 659 include, 46 exclude, 0 uncertain.

Outputs:
- `artifacts/screening/stage1_final_ledger.csv`
- `artifacts/screening/stage1_final_audit.json`
- `artifacts/screening/stage2_queue.csv`

The 659-record Stage-2 queue is not the final paper corpus. Independent second-coder reliability remains mandatory.

The results-driven paper is written after Stage-2 freeze, claim-level coding, reliability, architecture/comparator tests, robustness/holdouts, matched-case tests and managerial-value outputs are frozen.
