# SCDA — journal submission and reproducibility materials

This directory records the preparation and evidence checks for *The Decision Architecture of Supply Chain Management: Separating Decisions, Solutions, Evidence, and Context*, submitted for consideration to the *International Journal of Industrial Engineering and Operations Management* (IJIEOM).

## Manuscript scope

The study compares four nested representations of supply-chain research claims: K4 (decision kernel), KS7 (kernel plus solution), KSV8 (plus evidence status), and SCDA9 (plus context). The reported 124-claim analysis derives from 121 primary studies within a 125-study deep-review set. The broader review retained 518 studies from 705 candidate records.

Reported collision rates are 52.42% (K4), 19.35% (KS7), 17.74% (KSV8), and 12.90% (SCDA9). These values describe discrimination within the analysed corpus; they do not demonstrate improved organisational performance or establish the nine-dimensional representation as universally optimal.

## Evidence and verification

The repository contains analytical scripts, review and coding records, reproducibility checks, and audit outputs. The original evidence deposit is incomplete: the source workbooks listed in [evidence/README.md](evidence/README.md) were not committed there at the time of its verification. Recomputed coder-agreement outputs and their limitations are documented in the [evidence audit](audit/UPLOADED_EVIDENCE_REVIEW_20261103.md) and [reconciliation record](audit/CODER_RELIABILITY_RECONCILIATION_20261103.md).

Cohen's kappa across the nine coded dimensions ranges from 0.036 to 0.712; eight dimensions are below the prespecified 0.67 threshold. The original independent coding-handoff chronology is not independently established, and the prespecified 2024–2026 temporal holdout contains no qualifying analytical records. These limitations should be considered when interpreting architecture selection and generalisability.

## Reproduction

From the repository root:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python benchmarks/run_benchmark.py
```

Reproduction of the original paired-coder calculations additionally requires the unmodified workbook identified in [evidence/README.md](evidence/README.md). Consult the linked records for precise inputs and denominator conventions.

## Submission files

The author-provided IJIEOM package separates the anonymised main manuscript, tables, supplementary material, and confidential title page. The package supplied for the present review is not asserted to be identical to every older repository manuscript draft. Check the final journal-generated proof for completeness and anonymity.

## Research integrity

Source evidence, analysis outputs, methodological qualifications, and repository history are retained for traceability. Research claims must be assessed against the manuscript and underlying records; preparation notes are not evidence of a scientific result. Any use of generative AI that falls under the journal's disclosure policy must be declared accurately in the submitted manuscript.
