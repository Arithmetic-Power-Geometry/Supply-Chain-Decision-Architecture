# Robustness and Sensitivity Protocol v1

## Purpose
Test whether the architectural conclusion survives reasonable analytical choices. Sensitivity analysis is not a menu from which the most favorable result may be selected.

## Frozen sensitivity grid
Collision tolerance: 0.00, 0.01, 0.02, 0.05.
Complexity penalty lambda per dimension: 0.00, 0.01, 0.02, 0.03, 0.05.

Primary analysis remains tolerance 0.02 and lambda 0.02.

## Missing-data views
1. Available-fields analysis: preserve observed coding and report coverage.
2. Complete-case SCDA9 analysis: restrict to claims complete on all nine candidate fields.
3. Explicit-missing analysis: encode missingness as a visible state solely as a sensitivity diagnostic.

The explicit-missing view must not be interpreted as substantive evidence that missing information is a scientific category.

## Core-versus-annotation views
Compare interpretation under:
- KS7 core, with V and I as annotations;
- KSV8 core, with I as annotation;
- SCDA9 core.

The purpose is conceptual parsimony, not relabeling a failed dimension to preserve the original proposal.

## Study-level bootstrap
Resample publications, not individual claims, with replacement. All claims belonging to a sampled publication travel together. Primary robustness run: 500 deterministic replicates; larger runs may be added without replacing the frozen primary result.

Report selection frequencies for K4, KS7, KSV8 and SCDA9. These are empirical stability frequencies, not posterior probabilities and not probabilities that a model is true.

## Sparse strata
Do not interpret an era, discipline, industry or evidence cell as a gap when its denominator is too small for stable inference. Sparse strata are reported descriptively and flagged as underpowered.

## Taxonomy perturbation
Any synonym normalization or category merge used as a robustness check must be defined before viewing its effect on architecture selection. Post-result recoding requires a new protocol version.

## Failure rule
If the selected architecture changes materially across plausible specifications or bootstrap samples, the paper must report architectural instability and narrow its claims. Robustness results may falsify a headline conclusion.
