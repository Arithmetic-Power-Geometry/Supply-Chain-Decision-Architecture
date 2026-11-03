# SCDA coder identities and evidence-reconciliation ledger

**Prepared:** 2026-11-03  
**Scope:** IJIEOM editorial audit in `EMSUB/`  
**Status:** OPEN — researcher-identification assertion recorded; independent coding provenance and manuscript interpretation remain unverified.

## 1. Coder identities (author-reported, not independently authenticated)

The project lead reported that the researchers carried out the coding and identified:

| Project label | Researcher | Source/status |
| --- | --- | --- |
| Coder A | Dr. Md Saifullah Khalid | Project-lead confirmation in conversation; no signed researcher confirmation identified in the inspected repository |
| Coder B | Dr. Arvind Hans | Project-lead confirmation in conversation; no signed researcher confirmation identified in the inspected repository |

**Do not treat the identity mapping as independently established from GitHub files.** Obtain each coder's approval and reconcile the submitted non-blind author-contribution statement; keep the main manuscript anonymized. The existing `EMSUB/audit/AUTHORSHIP_UPDATE.md` says contributions require coauthor approval. Do not assert that either named researcher has signed off yet.

## 2. Evidence inventory and original-file link gap

| Artifact | Link | Evidence assessment |
| --- | --- | --- |
| Independent coding protocol | [protocol/intercoder_reliability_v1.md](../../protocol/intercoder_reliability_v1.md) | Specifies pre-adjudication independence and agreement computations |
| Coder B handoff instructions | [protocol/coder_b_human_instructions_FINAL.md](../../protocol/coder_b_human_instructions_FINAL.md) | Defines Coder B's intended assignment; does not demonstrate completion |
| Final-named Coder B blinded sample | [data/frozen/coder_b_blinded_sample_FINAL_v1.csv](../../data/frozen/coder_b_blinded_sample_FINAL_v1.csv) | the checked-in file is a small unfilled sample rather than a completed 125-record return; inspected coding fields are unfilled; this is not a completed coder return |
| Coder A/production claims | [data/frozen/production_claims_FROZEN_v1.csv](../../data/frozen/production_claims_FROZEN_v1.csv) | Research corpus artifact; cannot alone establish a human Coder A's independent 125-item assessments |
| Published reliability summary | [data/Final_SCM/Cohen_Kappa_125_FINAL.csv](../../data/Final_SCM/Cohen_Kappa_125_FINAL.csv) | Nine summary statistics, each nominally using n=125; no paired individual coder ratings included |
| Coder-specific model summary | [data/Final_SCM/coder_architecture_sensitivity_FINAL.csv](../../data/Final_SCM/coder_architecture_sensitivity_FINAL.csv) | Aggregate comparisons only; not a substitute for coder-level ratings |
| Computation script | [scripts/compute_reliability.py](../../scripts/compute_reliability.py) | Would reproduce results only when supplied two completed, matching input coding files |
| Coder B validation script | [scripts/validate_coder_b_return.py](../../scripts/validate_coder_b_return.py) | Can validate a returned file; no validation output or genuine completed return identified in reviewed tree |

**Unresolved evidence:** In the inspected default-branch tree, no separately completed, 125-record Coder A and Coder B rating files, signed handoff, validated return, or trace of a reproduction command and corresponding outputs were identified. Do not claim that the named coders generated the numeric results until these inputs are reconciled. Preserve original files, timestamps, and hashes if obtained; never synthesize or retrospectively backfill ratings. The blinded template's row count and the 125-record published statistics also require reconciliation.

## 3. The `BLOCKED` handoff and competing final-status claims

The original [handoff gate](../../protocol/coder_b_final_handoff_gate_v1.md) remains `BLOCKED` with all conditions unchecked. Do **not** rewrite it to `PASS` without historical supporting evidence.

The following checked-in records also identify unresolved earlier states:

- [artifacts/final/paper_use_provenance_v1.json](../../artifacts/final/paper_use_provenance_v1.json): `Reviewer A (AI-assisted)`, `independent_coder_b: pending`, architecture competition not run in that recorded state.
- [artifacts/final/production_corpus_status_v1.json](../../artifacts/final/production_corpus_status_v1.json): `REVIEWER_A_CORPUS_IN_PROGRESS_NOT_FROZEN`, Coder B pending.
- [data/Final_SCM/README.md](../../data/Final_SCM/README.md): later declares Coder B an independent human coder and lists final 125-record reliability results, but does not link the completed coder files or a verifiable transition log.

These records may represent different project stages; their actual chronology and transition must be established from dated, authentic evidence. As of this audit, the final gate is **not independently verified**, despite publication-facing summary files being present.

## 4. Reliability threshold and manuscript interpretation

The prespecified [intercoder reliability protocol](../../protocol/intercoder_reliability_v1.md) calls for revising, merging, demoting or removing dimensions with **kappa below 0.67** before headline architecture claims. The currently stored [summary CSV](../../data/Final_SCM/Cohen_Kappa_125_FINAL.csv) reports:

| Dimension | Reported Cohen's kappa |
| --- | ---: |
| decision_level | 0.035666 |
| process | 0.074690 |
| flow | 0.539840 |
| objective | 0.493271 |
| theory | 0.205607 |
| method | 0.227626 |
| technology | 0.712237 |
| evidence_maturity | 0.363200 |
| context | 0.177293 |

Only technology clears 0.67. This is not a clerical problem; it limits claims about stable, independently reproducible coding across the nine dimensions.

**Defensible manuscript interpretation (conditional on independently verifying the paired ratings):** SCDA9 yielded a lower *reported collision rate* under the study's selected coding/tolerance rule; collision minimization does **not** establish semantic validity, intercoder reproducibility, prospective performance, or a fully validated nine-dimension taxonomy. Label the architecture comparison as exploratory/conditional and report all reliability failures prominently, including the decisions that led to retaining the dimensions for descriptive model-comparison experiments. Do not claim that retaining unreliable dimensions fulfilled the prespecified development gate.

If paired independent coding inputs cannot be produced and authenticated, withdraw or explicitly relabel unsupported human intercoder claims, and do not report those values as independently verified Cohen's kappa. Any corrected analysis must preserve an immutable copy of original results and record the discrepancy.

## 5. Actions, evidence needed, and closure rules

| Priority | Required action | Evidence required | Status |
| --- | --- | --- | --- |
| 1 | Obtain named Coder A/B confirmation and correct non-blind title-page roles; preserve blinded labels | Author-approved contribution statements and the two coders' attestation | OPEN |
| 2 | Locate original completed, independently produced A/B files for the stated 125 matched claim/study units | Source files with 125 matching IDs, provenance/timestamps/checksums, unfilled-template distinction | OPEN |
| 2 | Recompute all nine kappa values from frozen paired pre-adjudication inputs | `scripts/compute_reliability.py` command, recorded input hashes, output and independent comparison to frozen summary | OPEN |
| 3 | Trace each original handoff-gate requirement and the chronology after the blocked checkpoint | Source-sufficiency decisions, admissible freeze manifest and hashes, blinded-sample generator/run, validated human return | OPEN |
| 4 | State why unreproducible dimensions were retained for exploratory collision comparisons | Explicit protocol-deviation assessment and bounded claims in the revised main and supplement | OPEN |
| 4 | Reconcile `EMSUB/audit/AUTHORSHIP_UPDATE.md`, `SUBMISSION_CHECKS.md` and title-page source | Author-approved wording and rebuilt relevant outputs | OPEN |

**Audit decision:** `NOT RECONCILED / DO NOT CERTIFY AS VERIFIED`. This ledger supplements, rather than silently edits, original historical records. No numerical results, original samples, scripts, or author contributions have been altered.

**Notes on scope:** Review based on the GitHub default-branch tree and cited tracked files as observed on 2026-11-03. Untracked local/external author files may exist; absence from this inspection is not proof that they never existed.
