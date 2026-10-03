# SCDA generalization and robustness — v1

## Frozen corpus
- Deep-review corpus: 125 studies.
- Primary architecture-analysis subset: 121 studies.
- Analytical claims: 124.
- Primary architecture result: SCDA9 under collision tolerance 0.02 and lambda 0.02.

## Deterministic publication holdout
The development partition contains 97 studies / 100 claims and selects SCDA9. The untouched deterministic publication holdout contains 24 studies / 24 claims. K4 has collision rate 0.2083, whereas KS7, KSV8 and SCDA9 all have zero collision. Under the frozen smallest-adequate-model rule, KS7 is therefore selected in this holdout. The holdout does not support claiming that SCDA9 is uniquely necessary for every sampled subset.

## Temporal holdout
The frozen analytical claim corpus contains no 2024–2026 primary analytical claims under the current year field. Therefore the prespecified 2024–2026 temporal holdout has zero studies and cannot test recent-period transfer. This is reported as unavailable/underrepresented, not as successful generalization.

## Disciplinary holdouts
Thirty-four discipline labels occur in the analytical corpus. Many are sparse and must be treated as underpowered according to the protocol. Discipline-specific results are retained in the complete artifact rather than pooled opportunistically.

## Evidence layer
Eight KS7-matched groups contain at least two claims. Evidence maturity varies in 2/8 groups (25%). This provides limited descriptive evidence that V adds information in some otherwise matched solution representations; it is not causal evidence.

## Context layer
Eight KSV8-matched groups contain at least two claims. Context varies in 4/8 groups (50%), and all four variable groups are cross-study. This provides descriptive evidence that I exposes boundary information in some otherwise matched representations.

## Robustness
Across 60 frozen missingness/tolerance/lambda scenarios, selections are: SCDA9 30, KS7 20, KSV8 10. Complete-case SCDA9 contains only 20 claims and must be interpreted cautiously.

In 500 deterministic study-level bootstrap replicates, selections are KS7 202 (40.4%), SCDA9 183 (36.6%), and KSV8 115 (23.0%); K4 is never selected. These are stability frequencies, not probabilities that an architecture is true.

## Interpretation
The primary full-corpus specification selects SCDA9 and the ablation shows incremental separation from context and, more modestly, evidence maturity. However, the deterministic holdout and study bootstrap show architecture-selection instability among KS7, KSV8 and SCDA9. The defensible conclusion is therefore that richer solution/evidence/context representations improve descriptive separation in the full corpus, while the exact core dimensionality is not uniformly stable across resampled or held-out subsets. Claims of universal SCDA9 superiority should be avoided.

Second-coder approval is recorded as independent verification/consensus. Cohen's kappa is not reported because a separate categorical Coder-B return was not available.
