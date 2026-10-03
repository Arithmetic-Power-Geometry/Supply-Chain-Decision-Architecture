# Frozen 125-study architecture competition — v1

## Analytical freeze
- Deep-review corpus: 125 studies.
- Primary architecture-analysis subset: 121 studies.
- Primary claim corpus: 124 claims.
- Claim digest (SHA-256): `c4dfb379c8bfc25c8725d81f5172d6f2bed6ae871d03c755e5fe2213e03b1a29`.
- Second-coder green signal is recorded as independent verification/consensus. Cohen's kappa is not claimed because an independent categorical coding return is not available.

## Primary specification
Collision tolerance = 0.02; complexity penalty lambda = 0.02.

| Model | Coverage | Collision rate | Distinct signatures | Entropy | Parsimony score |
|---|---:|---:|---:|---:|---:|
| K4 | 1.0000 | 0.5242 | 80 | 5.9961 | 0.3958 |
| KS7 | 0.8802 | 0.1935 | 108 | 6.6234 | 0.5698 |
| KSV8 | 0.8952 | 0.1774 | 110 | 6.6771 | 0.5763 |
| SCDA9 | 0.9068 | 0.1290 | 115 | 6.7969 | 0.6098 |

Under the frozen smallest-adequate-model rule, SCDA9 is selected in the primary specification.

## Sensitivity
SCDA9 is selected for collision tolerances 0.00, 0.01, and 0.02 across all frozen lambda values (0.00–0.05). At collision tolerance 0.05, KSV8 becomes the smallest adequate model across the same lambda grid. This is a boundary sensitivity and must be reported rather than hidden.

## SCDA9 leave-one-dimension-out ablation
Removing process produces the largest collision increase (+0.1048), followed by flow (+0.0645) and context (+0.0484). Removing evidence maturity increases collision by +0.0161. Removing method produces no change in collision rate, distinct signatures, or entropy in this corpus. Therefore the primary result supports SCDA9 under the prespecified tolerance, while also showing that not every dimension contributes equal incremental separation.

These are architecture-separation results, not causal performance estimates and not probabilities that a model is true.
