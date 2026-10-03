# Production Claim Coding Gate v1

## Unit of analysis
The empirical unit is a substantive decision-relevant research claim, not a paper. A retained primary study may contribute zero, one, or multiple claims. Claims from the same publication retain one study_id and are clustered in all prevalence and uncertainty analyses.

## Admission gate
A row enters the production claim corpus only when:
1. the Stage-2 decision is include and study_type is primary;
2. claim_text is supported by the inspected source basis;
3. claim_location identifies abstract, page/section, table, figure, or other retrievable source location;
4. L, P, F and O use the frozen codebook or are explicitly marked ambiguous;
5. theory is recorded only when the source explicitly declares a theoretical lens;
6. method is one of Conceptual, Empirical, Optimization, Simulation, Statistics, Machine Learning, Artificial Intelligence, Multi-agent/Autonomous;
7. evidence_maturity is one of Conceptual, Synthetic, Simulation, Benchmark, Case study, Observational, Pilot, Deployed, Longitudinal;
8. context records the reported application context, using General only when no industry is central;
9. coder, confidence, source_support and source_identifier are non-empty.

## No silent inference
Technology sophistication does not determine evidence maturity. Topic labels are not theories. A paper title is not automatically a claim. Missing or ambiguous dimensions are preserved as uncertainty and are not filled merely to increase SCDA9 coverage.

## Pilot status
data/primary_pilot_claims_v1.csv is calibration history only. Its legacy labels are not production categories and must not enter headline large-corpus analyses without source re-inspection and recoding under the frozen codebook.

## Production sequence
Retained primary-study pool -> source inspection -> claim extraction -> frozen-category coding -> validation -> independent reliability sample -> architecture competition and robustness analyses.
