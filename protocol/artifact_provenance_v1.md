# Artifact Provenance and Paper Traceability Protocol v1

## Principle
Every quantitative headline result, table and figure in the final paper must have a reproducible lineage:
raw evidence -> screened records -> coded claims -> analysis script -> generated artifact -> paper object.

A repository file is not scientific evidence merely because it has a hash. Hashes establish identity and lineage, not correctness.

## Required provenance
For each registered analysis record:
- producer script and its SHA-256;
- input paths and SHA-256 where files exist;
- frozen parameters;
- output paths and SHA-256;
- Git commit;
- intended paper section/table/figure.

Raw retrieval files remain immutable. Corrections are represented as new derived records or adjudication layers rather than silent replacement of source evidence.

## Staleness
If an upstream input, producer script or parameter changes, dependent outputs must be regenerated before they may be used in the final paper. The final submission bundle must be generated from one identifiable repository commit.

## Paper rule
No manually calculated headline number may be introduced when the same result is expected from a registered analysis artifact. Tables and figures derived from analysis should be generated from the same frozen artifacts used for prose claims.

## Scope
The provenance graph is generated only when its required inputs exist. During corpus construction, absent downstream files are expected and do not justify placeholder results.

## Final freeze
Before manuscript construction after G20, freeze:
1. retrieval manifests;
2. screening ledger and flow;
3. coded claim corpus;
4. reliability/adjudication artifacts;
5. model-selection, holdout, matched-case, robustness and managerial artifacts;
6. claim-provenance ledger;
7. repository commit.

After the paper is written, rerun the provenance and manuscript integrity gates against the submission commit.
