# Artifact Integrity and Evidence Freeze

## Principle
Every quantitative value reported in the eventual paper must be reproducible from a frozen input corpus and versioned analysis code.

## Workflow evidence
Generated analytical outputs are stored under `artifacts/` during workflow execution. A machine-readable manifest records:
- relative path
- byte size
- SHA-256 digest

## Freeze
At the publication evidence freeze:
1. record the Git commit SHA;
2. record raw-input checksums where redistribution permits;
3. generate all tables/figures/data summaries from the same commit;
4. generate the artifact manifest;
5. archive the evidence bundle;
6. record the archive DOI/version if deposited.

## Rule
Manually edited analytical outputs are not publication evidence. If a table or figure requires a correction, correct the source data/code and regenerate it.

## Manuscript relationship
The software and workflow produce research evidence and reproducibility artifacts. They do not generate or define the scholarly conclusions. Interpretation remains a research task grounded in the frozen evidence.
