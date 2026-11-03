# Uploaded SCDA evidence review — 2026-11-03

**Status:** Uploaded evidence inspected; paired agreement independently recomputed; original researcher identity and historical independence remain to be authenticated. This is a supplement to [the open reconciliation ledger](CODER_RELIABILITY_RECONCILIATION_20261103.md), not a replacement for original source files.

## 1. Key finding: 125 paired coding records now supplied

The user supplied `SCDA_Coder_A_Coder_B_Adjudication_Datasets_FINAL(3).xlsx` (SHA-256: `2d64dac2ec007997...`, abbreviated). The workbook contains five tabs:

- `README` — descriptions of data and claimed coding provenance;
- `Coder_A_125_Human` — 125 record IDs and Coder A ratings;
- `Coder_B_125_Human` — 125 record IDs and Coder B ratings;
- `Adjudication_Log_Frozen` — 12 adjudication entries;
- `Coder_A_B_Paired_125` — 125 paired rows with nine dimensions each.

**Numerical verification performed:** Parsed all 125 rows by nonblank `record_id` (the `study_no` column is blank for rows after the first 55 and must not be used to filter the dataset). For each dimension, counted exact matching category values and calculated Cohen's kappa as `(p_observed - p_expected)/(1 - p_expected)` using empirical coder-specific marginal proportions. Empty theory values were treated as an explicit blank category in this reconciliation, matching the supplied summary; this differs from `scripts/compute_reliability.py`, which drops missing pairs. The study-level `record_id` unit also differs from that script's `claim_id` join. This methodological discrepancy must be documented and resolved before describing the script as the source of the 125-study results.

| Dimension | N | Recomputed raw agreement | Recomputed kappa | Matches existing final summary (6 decimals)? |
| --- | ---: | ---: | ---: | --- |
| decision_level | 125 | 0.448 | 0.035666 | Yes |
| process | 125 | 0.288 | 0.074690 | Yes |
| flow | 125 | 0.640 | 0.539840 | Yes |
| objective | 125 | 0.600 | 0.493271 | Yes |
| theory | 125 | 0.864 | 0.205607 | Yes |
| method | 125 | 0.504 | 0.227626 | Yes |
| technology | 125 | 0.896 | 0.712237 | Yes |
| evidence_maturity | 125 | 0.592 | 0.363200 | Yes |
| context | 125 | 0.488 | 0.177293 | Yes |

**What is now supported:** The uploaded paired dataset numerically reproduces [the frozen reliability summary](../../data/Final_SCM/Cohen_Kappa_125_FINAL.csv). The previous audit's statement that paired data were not available **in the inspected GitHub tree** remains historically accurate; paired data are now available as a user-supplied attachment, but the binary workbook itself is not yet committed to this repository.

**What is not yet independently proven:** Whether these rows were genuinely completed independently by the named people, when the coding took place, whether ratings were changed after adjudication, and whether the study-level pairing follows the pre-registered claim-level sample protocol. The workbook's `README` itself states that coder/provenance wording was corrected to reflect user confirmation. That wording is not independent authentication. Do not close the provenance gate without corroborating source files and author attestations.

## 2. Additional uploaded files and relevance

| Uploaded filename | SHA-256 prefix | Audit use |
| --- | --- | --- |
| `FINAL_RESULTS_FREEZE_v1.json` | `9cf2de4e137ab13a` | Frozen headline values and source-workbook hash manifest |
| `SCDA_125_Frozen_Model_Competition_Ablation_v1(1).xlsx` | `5acdda870400a31d` | Primary nested model comparison, ablation, sensitivity |
| `SCDA_125_Generalization_Robustness_COMPLETE_v1(1).xlsx` | `f0b95e99023f132f` | Generalization, 60-setting robustness, 500 bootstrap |
| `SCDA_Bibliography_125_Audit(1).xlsx` | `171c7d4fdb8041a0` | Source bibliography inventory, not independent DOI verification |
| `SCDA_Managerial_Decision_Usefulness_v1(1).xlsx` | `9074ab49374aaad9` | Managerial ambiguity diagnostics |
| `SCDA_Coder_A_Coder_B_Adjudication_Datasets_FINAL(3).xlsx` | `2d64dac2ec007997` | Paired coder ratings and adjudication |
| `Coder_A_B_Agreement_Recomputed.csv` | `1a897c6fa0832bb2` | Reported coder agreement summary |
| `Coder_Sensitivity_Architecture.csv` | `ac132b45688740ad` | Coder-specific architecture outcomes |
| `Repeated_Holdout_500_Coder_Sensitivity.csv` | `b95bda5367a64980` | Coder-specific holdout sensitivity |
| `Permutation_Null_5000_Coder_Sensitivity.csv` | `26c95913c1dee1fe` | Coder-specific permutation-null results |

The four workbook hashes in the uploaded `FINAL_RESULTS_FREEZE_v1.json` match the corresponding uploaded workbook bytes for the model competition, generalization/robustness, managerial diagnostics, and bibliography audit. This is a useful consistency check; it does not establish the creation date or independence of the source data.

## 3. Remaining corrections and submission gate

1. **Preserve original workbook** in the project's evidence archive and record its full SHA-256, source, and receipt date. The original binary attachment was not written to GitHub by this audit; this Markdown report is the committed record.
2. **Confirm coder identities** with both researchers: project lead identifies Md Saifullah Khalid as Coder A and Arvind Hans as Coder B. Do not infer identities from the workbook's generic `Coder A (Human)`/`Coder B (Human)` labels.
3. **Reconcile chronology and protocol**: the [handoff gate](../../protocol/coder_b_final_handoff_gate_v1.md) still reads `BLOCKED`, and the checked-in Coder B template is unfilled. Investigate the original completed returns, signatures, timestamps and frozen sample, and document whether the 125-study dataset was an authorized protocol amendment.
4. **Reconcile kappa methodology**: `theory` has blank values, and the published kappa treats blank as a category; the checked-in script drops incomplete pairs. A transparent, versioned reproduction script for the actual study-level calculation is needed.
5. **Revise interpretation**: eight of nine dimensions fail the prespecified 0.67 reliability gate; a lower collision rate does not validate the nine-dimensional taxonomy. Retain numerical values but limit claims appropriately.

**Reviewer conclusion:** This upload **materially improves numerical auditability** and closes the narrow question of whether the reported nine kappas can be recomputed from a supplied 125-row paired dataset. It does **not** close the broader independent-human-coding provenance or protocol-compliance concerns. No frozen numeric outputs were changed.
