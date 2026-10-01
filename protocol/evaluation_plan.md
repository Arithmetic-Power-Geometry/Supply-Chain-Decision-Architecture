# Comparative Evaluation Plan — v1.0

Status: frozen before real-corpus results.

## Central question
Does SCDA provide useful, reproducible structure beyond simpler and previously published organizing frameworks, without receiving an automatic advantage merely from using more dimensions?

## Units
Primary unit: coded scholarly study/contribution.
Primary comparisons use the frozen systematic corpus. Landmark and synthetic records are excluded from headline estimates.

## Metric families

### 1. Codability and coverage
Report the proportion of records that can be coded for each dimension and framework. Missingness is reported by era and discipline.

### 2. Collision
A collision occurs when distinct studies receive the same representation under a framework. Report collision rate and signature multiplicity distribution.

### 3. Information content
For each categorical dimension and joint representation, compute empirical Shannon entropy. Report normalized entropy where useful.

### 4. Complexity-adjusted utility
Do not equate a larger number of fields with a better framework.
Report:
- information gain contributed by each added dimension;
- marginal reduction in collisions;
- gain per dimension;
- gain per reliably codable dimension;
- redundancy between dimensions.

### 5. Ablation
Starting from full SCDA, remove one dimension at a time and measure changes in collision, entropy, gap structure, and coverage.
Also evaluate nested kernels where theoretically justified.

### 6. Prior-framework baselines
Implement comparison schemes from actual prior reviews/frameworks only after their definitions are faithfully reconstructed. Simplified one-dimensional controls are diagnostic, not evidence of superiority over the literature.

### 7. Reliability
Report agreement by dimension. Dimensions with weak reliability cannot be presented as strong contributions even if they increase mathematical distinguishability.

### 8. Robustness
Repeat headline analyses:
- excluding ambiguous codes;
- by historical era;
- by discipline;
- by topic;
- with alternative treatment of multi-label records;
- after removing technology-heavy frontier records.

### 9. Gap discovery
A sparse cell is not automatically a research gap. Candidate gaps require:
1. low/zero observed density,
2. conceptual plausibility,
3. evidence that the combination matters,
4. confirmation that absence is not a retrieval/coding artifact.

### 10. Temporal validation
Test whether architecture dimensions remain meaningful across historical eras rather than fitting only digital-era literature.

## Interpretation rule
No single metric determines superiority. Conclusions must jointly consider informativeness, parsimony, reliability, robustness, historical validity, and managerial interpretability.
