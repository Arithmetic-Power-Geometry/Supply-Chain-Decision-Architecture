# Independent Coding Reliability Protocol v1

## Purpose
Reliability tests whether SCDA dimensions can be applied reproducibly by independent coders. It is not a mechanism for making the architecture appear reliable.

## Sample
At least 20% of the frozen claim-level validation corpus is independently recoded. The reliability subset is stratified across era, discipline, decision level, process, evidence maturity and context where the corpus permits. All claims from a selected publication remain together to avoid claim leakage.

## Independence
Coder B receives the frozen codebook and source material required for coding but not coder A's labels. The two coding files remain separate until the pre-adjudication reliability artifact has been generated and frozen.

## Statistics
For nominal single-label dimensions report:
- number of matched non-missing claims;
- missing-pair count;
- raw agreement;
- Cohen's kappa.

Where a later dimension is genuinely multi-label or missingness makes nominal kappa inappropriate, use a prespecified Krippendorff-alpha implementation and state the distance function. Do not switch statistics after inspecting which gives a more favorable result.

## Interpretation
No universal kappa threshold is treated as a law. Dimension-level estimates, sample size and disagreement pattern are reported together. As an internal model-development gate:
- >=0.80: strong reproducibility;
- 0.67--0.7999: usable with explicit review and sensitivity analysis;
- <0.67: revise, merge, demote or remove the dimension before headline architecture claims.

These are preregistered development rules, not claims that the cutoffs are universal standards.

## Adjudication
Reliability is calculated before adjudication. Each disagreement is then reviewed and preserved in an adjudication ledger with coder-A value, coder-B value, final value, rationale and adjudicator. Post-adjudication agreement is never reported as inter-coder reliability.

## Failure rule
A dimension that repeatedly fails independent coding cannot be retained merely because it improves collision rate or entropy.
