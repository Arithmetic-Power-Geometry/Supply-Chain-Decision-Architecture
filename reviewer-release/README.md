# SCDA — reviewer-facing research release

This curated release accompanies *The Decision Architecture of Supply Chain Management: Separating Decisions, Solutions, Evidence, and Context*. It presents the research methods, verified summary results, reproducibility entry points, and limitations. It is **not** a replacement for the complete repository or an assertion that all underlying source files are available.

## Study and methods

SCDA separates the decision kernel K=(L,P,F,O), solution S=(T,M,G), evidence status V, and context I. Four nested representations are compared: K4, KS7, KSV8 and SCDA9.

A two-stage review identified 705 candidate records, advanced 659 to stage 2, retained 518 and excluded 141. The 125-study deep-review set comprises 121 primary analytical studies and four review/framework roles; the primary comparison uses 124 source-supported claims.

The primary comparisons use collision, coverage, parsimony, nested-model sensitivity and robustness diagnostics. A separate 125-study paired-coder calculation reports dimension-wise Cohen's kappa. Its unit and missing-value treatment differ from the original claim-level protocol; the distinction is documented in [LIMITATIONS.md](LIMITATIONS.md).

## Main reported results

| Representation | Dimensions | Collision |
| --- | ---: | ---: |
| K4 | 4 | 52.42% |
| KS7 | 7 | 19.35% |
| KSV8 | 8 | 17.74% |
| SCDA9 | 9 | 12.90% |

The reduction measures within-corpus discrimination. It does not establish a validated nine-dimensional instrument or organisational benefit.

## Research data and programs

- [Frozen model-comparison and diagnostic files](../data/Final_SCM/) — the existing project data directory, including the model comparison, bootstrap, holdout, permutation and reliability summaries.
- [Coder agreement summary](../data/Final_SCM/Cohen_Kappa_125_FINAL.csv) — nine study-level reliability statistics.
- [Study-level reliability reconstruction](../EMSUB/scripts/recompute_125_coder_agreement.py) — executable verification of the reported 125-pair agreement from the original paired workbook, when available.
- [Original claim-level reliability implementation](../scripts/compute_reliability.py) — a different unit and missingness rule; **not interchangeable** with the 125-pair reconstruction.
- [Prespecified coding reliability protocol](../protocol/intercoder_reliability_v1.md).
- [Repository package and tests](../pyproject.toml), [tests](../tests/), and [illustrative benchmark](../benchmarks/run_benchmark.py). The illustrative benchmark is **not** the 124-claim manuscript experiment.

## Reproduction

From the repository root:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python benchmarks/run_benchmark.py
```

For the manuscript's 125-pair kappa reproduction, obtain the unmodified source workbook identified in [the evidence inventory](../EMSUB/evidence/README.md), install `openpyxl`, and follow the command documented there. The workbook has not been confirmed as deposited in this GitHub tree; therefore, a fresh reader cannot yet reproduce that calculation using GitHub alone.

## Interpretive limits

See [LIMITATIONS.md](LIMITATIONS.md). Original evidence records and repository history are preserved. This curated release excludes internal workflow instructions from its navigation, without modifying or concealing the historical record.

## Manuscript and submission

The journal submission uses an anonymised main manuscript, separate tables and supplementary material. The author-provided ZIP is not represented as a committed or independently verified ScholarOne proof. Any applicable journal disclosure and coauthor-approval requirements remain the authors' responsibility.
