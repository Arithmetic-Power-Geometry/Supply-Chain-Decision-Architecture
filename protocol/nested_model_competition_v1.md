# Nested Architecture Competition and Parsimony Protocol v1

## Candidate representations
K4 = decision level + process + flow + objective.
KS7 = K4 + theory + method + technology.
KSV8 = KS7 + evidence maturity.
SCDA9 = KSV8 + context.

All representations are evaluated on the same frozen claims. No model receives a different eligibility subset merely because a field is difficult to code.

## Primary diagnostics
Report coverage, collision rate, number of distinct signatures and signature entropy. Claims remain linked to study_id; paper-level prevalence and uncertainty analyses must cluster by study.

## Parsimony
The architecture is not chosen by maximum dimensionality. The primary selection rule is the smallest representation whose collision rate lies within a prespecified tolerance of the best observed collision rate, with coverage reported alongside it.

Primary tolerance: 0.02 absolute collision rate.
Sensitivity grid: 0.00, 0.01, 0.02, 0.05.

A diagnostic parsimony score is also reported:
(1 - collision rate) * coverage - lambda * number of dimensions.

Primary lambda: 0.02 per dimension.
Sensitivity grid: 0.00, 0.01, 0.02, 0.03, 0.05.

The score is secondary; it cannot override a reproducibility failure.

## Leave-one-dimension-out falsification
For SCDA9, remove each dimension in turn and report change in collision, coverage and signature entropy. A dimension with negligible incremental information, poor reliability or unstable generalization is a candidate for demotion/removal.

## Decision hierarchy
1. coding reliability;
2. out-of-sample/holdout robustness;
3. non-redundant information;
4. coverage;
5. parsimony.

A dimension cannot be rescued by in-sample collision reduction if it fails reliability or holdout tests.

## Outcome rule
The paper reports whichever representation survives these tests. SCDA9 is a candidate hypothesis, not the predetermined conclusion.
