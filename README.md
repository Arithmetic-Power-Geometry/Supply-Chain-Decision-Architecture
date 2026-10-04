# Supply Chain Decision Architecture (SCDA)

This repository contains the reproducible research software, frozen evidence records, analytical datasets, and computational artifacts associated with **The Decision Architecture of Supply Chain Management: Separating Decisions, Solutions, Evidence, and Context**.

SCDA separates the identity of a supply-chain decision from the solution used to address it, the evidence status of the focal claim, and the context in which the evidence is observed. The complete representation is:

`R = (K, S, V, I) = ((L, P, F, O), (T, M, G), V, I)`

where the Decision Kernel is `K=(L,P,F,O)`, the Solution layer is `S=(T,M,G)`, `V` is evidence status, and `I` is application context.

## Architecture

The nine dimensions are:

| Layer | Dimension | Meaning |
|---|---|---|
| Decision Kernel | L | Decision level |
| Decision Kernel | P | Supply-chain process |
| Decision Kernel | F | Focal flow |
| Decision Kernel | O | Primary objective |
| Solution | T | Explicit theoretical lens |
| Solution | M | Principal method |
| Solution | G | Principal enabling technology |
| Evidence | V | Evidence status |
| Context | I | Reported application context |

Four nested representations are evaluated on the same analytical corpus:

- **K4** = (L, P, F, O)
- **KS7** = K4 + (T, M, G)
- **KSV8** = KS7 + V
- **SCDA9** = KSV8 + I

The full nine-dimensional representation is an empirical candidate rather than an assumed endpoint.

## Evidence base

The frozen review workflow contains:

- 705 unique candidate records
- 659 records advanced to Stage-2 screening
- 518 retained and 141 excluded
- 342 retained primary studies and 176 review/framework studies
- 125 studies in the deep-review corpus
- 121 primary analytical studies
- 4 review/framework roles within the deep-review corpus
- 124 source-supported analytical claims

The deep-review corpus is a purposive analytical subset used for source-verifiable coding and architecture comparison; it is not a prevalence-weighted sample of the SCM literature.

## Main empirical results

For the frozen 124-claim analysis, collision decreases across the nested representations:

| Model | Dimensions | Coverage | Collision | Distinct signatures | Entropy |
|---|---:|---:|---:|---:|---:|
| K4 | 4 | 1.0000 | 0.5242 | 80 | 5.9961 |
| KS7 | 7 | 0.8802 | 0.1935 | 108 | 6.6234 |
| KSV8 | 8 | 0.8952 | 0.1774 | 110 | 6.6771 |
| SCDA9 | 9 | 0.9068 | 0.1290 | 115 | 6.7969 |

Under the prespecified smallest-adequate rule with collision tolerance τ = 0.02, SCDA9 is selected in the full frozen analysis. At τ = 0.05, KSV8 becomes the smallest adequate representation. The untouched 24-study publication holdout selects KS7.

Independent second-coder assessment produced heterogeneous dimension-wise Cohen's κ values from 0.036 to 0.712. Coder-specific analyses preserve the monotone K4 → KS7 → KSV8 → SCDA9 collision reduction, while repeated holdouts show that the preferred depth is sensitive to coder and sampled records.

A 5,000-replicate permutation diagnostic shows that adding independently permuted fields can mechanically reduce collision. Collision is therefore interpreted as **within-corpus discriminability**, not as proof of ontology validity.

Across 500 publication-cluster bootstrap replicates, K4 is never selected; KS7 is selected 40.4%, KSV8 23.0%, and SCDA9 36.6%. The evidence supports a layered decision-and-solution representation while treating the precise outer-layer boundary as contingent on coding, sample composition, and analytical purpose.

## Reproducibility

The repository preserves the evidence trail and computational materials used to evaluate SCDA, including screening records, frozen claim data, coding artifacts, architecture-comparison outputs, ablation and sensitivity analyses, holdouts, matched-case diagnostics, robustness analyses, and workflow-generated artifacts.

Local software execution:

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python benchmarks/run_benchmark.py
```

## Citation

Akhtar, M. A. K. (2026). *The Decision Architecture of Supply Chain Management: Separating Decisions, Solutions, Evidence, and Context* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23134495

**DOI:** https://doi.org/10.5281/zenodo.23134495

## License

Code is released under the Apache License 2.0. Bibliographic records, source materials, and third-party content remain subject to their respective rights and licenses.
