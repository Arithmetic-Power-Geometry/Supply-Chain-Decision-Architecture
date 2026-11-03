# SCDA IJIEOM submission gate — 2026-11-03

**Decision: CONDITIONAL / NOT YET CERTIFIED.** This report does not claim that ScholarOne proof or authors' declarations have been inspected.

## Independently run in this review

- Inspected the author-uploaded repository ZIP `Supply-Chain-Decision-Architecture-main.zip`. It is a downloaded snapshot, not necessarily the latest GitHub commit.
- Ran `PYTHONPATH=src python -m unittest discover -s tests -v` from the extracted snapshot: **19 tests passed**.
- Running the tests without installation or `PYTHONPATH=src` failed with `ModuleNotFoundError: No module named 'scda'`. This is an environment/setup requirement, not a failing assertion.
- The ZIP still contains the three old `EMSUB/prompts/` files because it predates their removal from the live main branch. Live GitHub deletion commits were previously recorded.

## Existing repository audits (not independently rerun here)

- Main PDF, tables and supplement reportedly compiled successfully.
- Four reported architecture collision rates: K4 52.42%, KS7 19.35%, KSV8 17.74%, SCDA9 12.90%.
- Study-level paired-coder kappas range 0.036–0.712, with eight of nine below the original 0.67 development gate.
- Historical independent coder handoff and freeze provenance remain unverified.
- The 2024–2026 temporal holdout is empty.
- The original 125-pair workbook is not present in the checked-in `EMSUB/evidence/` folder.

## Submission blockers requiring author-supplied facts or materials

1. Review the **ScholarOne-generated proof** for anonymity, order of figures/tables, correct author/title-page separation, reference completeness and journal word-count treatment.
2. Reconcile the coder A/B source files, dated pre-adjudication return and signed/confirmed contributions if available. If not, qualify the manuscript's independence and reliability claims; do not infer missing records.
3. Deposit the unmodified paired-coder workbook (subject to rights/privacy) with full checksum, or clearly describe its controlled availability and reproduce its results from the original source.
4. Explain the protocol departure (study-level vs claim-level coding, missing theory treated as category) and eight below-threshold dimensions in Methods/Limitations; avoid claims of validated taxonomy or predictive performance.
5. Confirm all coauthors approve the final text and contribution statements.
6. Complete the Emerald AI-use declaration accurately according to actual manuscript preparation; repository cleanup does not affect that requirement.

## Reproduction commands

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python benchmarks/run_benchmark.py
```

If not installing the package, use `PYTHONPATH=src python -m unittest discover -s tests -v`.

**Do not mark this gate PASS** until the source data, author attestations, journal proof and disclosure checks are actually completed.
