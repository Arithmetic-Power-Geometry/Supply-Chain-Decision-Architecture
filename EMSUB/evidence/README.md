# SCDA source-evidence deposit and verification

This directory is reserved for the original, unmodified research-evidence attachments. **No original binary workbooks or uploaded CSVs were committed in this step.** Do not describe this directory as containing completed human-coder evidence until those files are actually present.

## Source files to deposit (unaltered)

- `SCDA_Coder_A_Coder_B_Adjudication_Datasets_FINAL(3).xlsx` — paired 125-record coder ratings and adjudication; SHA-256 `2d64dac2ec007997` (prefix; confirm full digest on upload)
- `SCDA_125_Frozen_Model_Competition_Ablation_v1(1).xlsx` — model competition and ablation
- `SCDA_125_Generalization_Robustness_COMPLETE_v1(1).xlsx` — robustness and bootstrap
- `SCDA_Bibliography_125_Audit(1).xlsx` — bibliography audit
- `SCDA_Managerial_Decision_Usefulness_v1(1).xlsx` — managerial diagnostics
- `FINAL_RESULTS_FREEZE_v1.json` — frozen-result manifest
- `Coder_A_B_Agreement_Recomputed.csv` — summary
- `Coder_Sensitivity_Architecture.csv` — architecture sensitivity
- `Repeated_Holdout_500_Coder_Sensitivity.csv` — repeated holdout
- `Permutation_Null_5000_Coder_Sensitivity.csv` — permutation null

When deposited, preserve filenames and exact bytes and record full SHA-256 digests. If a new version is needed, add it with a new filename; do not silently overwrite a frozen artifact.

## Reproduction

Run from repository root after uploading the original paired workbook:

```bash
python -m pip install openpyxl
python EMSUB/scripts/recompute_125_coder_agreement.py \
  'EMSUB/evidence/SCDA_Coder_A_Coder_B_Adjudication_Datasets_FINAL(3).xlsx' \
  --expected data/Final_SCM/Cohen_Kappa_125_FINAL.csv \
  --out EMSUB/audit/RECOMPUTED_125_CODER_AGREEMENT.json
```

The script checks all nine reported kappas against the frozen summary. The calculation treats blanks as a category to match the published summary. The earlier `scripts/compute_reliability.py` uses claim IDs and excludes missing pairs, so it is **not** an interchangeable implementation.

See [uploaded-evidence audit](../audit/UPLOADED_EVIDENCE_REVIEW_20261103.md) and [reconciliation ledger](../audit/CODER_RELIABILITY_RECONCILIATION_20261103.md). Independent-human-coding provenance, pre-adjudication chronology and κ<0.67 protocol departures remain open.
