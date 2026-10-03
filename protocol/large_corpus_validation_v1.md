# Large-Corpus Validation v2 — IEEE TEM Benchmark-Plus Protocol

## Benchmark
The validation is designed against the methodological bar visible in recent IEEE Transactions on Engineering Management reviews: PRISMA-style transparent selection, substantive content synthesis, cross-disciplinary integration, and explicit managerial relevance. SCDA adds falsifiable architecture evaluation rather than relying only on thematic clustering.

## Stage A — Discovery and provenance
Execute the four frozen OpenAlex families. Preserve raw pages, timestamps, reported counts, cursor/page state, query-family provenance and SHA-256 manifests. Crossref verifies DOI metadata; publisher records resolve material discrepancies. Scopus/WoS are not reported unless actually executed.

## Stage B — Deduplication and eligibility
Deduplicate by normalized DOI, then normalized title with manual resolution of near matches. Record inclusion/exclusion reason for every screened record. Reviews populate the review-of-reviews layer; primary studies populate quantitative validation.

## Stage C — Stratified corpus
Build a corpus spanning historical era, discipline, decision level, process, method/technology family, evidence maturity and application context. Report stratum counts before analysis. Do not optimize sampling to make SCDA look favorable.

## Stage D — Claim-level coding
The focal unit is a substantive research claim. A paper may contribute multiple claims, but claims from one paper are clustered under the same study identifier and never treated as independent publications in prevalence statistics. Preserve source basis and coding confidence.

## Stage E — Reliability
A second independent coding pass covers at least 20% of the frozen coded corpus, stratified across eras and major dimensions. Report raw agreement and Cohen's kappa for nominal single-label dimensions; use Krippendorff's alpha where missing/multi-label structure makes it preferable. Dimensions with weak reliability are revised, demoted or removed before model claims.

## Stage F — Architecture competition
Evaluate K4, KS7, KSV8 and SCDA9 on identical claims. Report coverage, collision rate, distinct signatures, entropy, complexity-adjusted information gain and leave-one-dimension-out ablation. Prefer the smallest representation preserving substantively useful distinctions with acceptable reliability.

## Stage G — Strong literature baselines
Reconstruct the strongest genuine multidimensional SCM frameworks from their original definitions. Compare codability and distinctions on the same frozen sample. One-dimensional function/method/technology controls remain diagnostics only and cannot support superiority claims.

## Stage H — Generalization
Use temporal and disciplinary holdouts. Fit/finalize coding rules without seeing the holdout results, then test whether architecture behavior persists in later-era and cross-discipline subsets. Report sensitivity to ambiguous records and alternative coding rules.

## Stage I — Evidence-maturity test
Construct matched decision/solution cases that differ in evidence maturity (conceptual, synthetic, simulation, benchmark, case study, observational, pilot, deployed, longitudinal). Test whether V changes interpretation after K and S are held comparable.

## Stage J — Research-usefulness outputs
Generate machine-readable decision maps, evidence maps, sparse-cell candidates, contradiction flags and artifact-to-result provenance. A sparse cell is not automatically called a research gap; gap claims require substantive interpretation and evidence.

## Stage K — Managerial relevance
For each robust decision/evidence pattern, state the managerial decision, demonstrated evidence level, boundary/context and practical implication. Do not translate technical sophistication into managerial effectiveness without evidence.

## Publication gates
No field-wide headline claim is written until:
1. retrieval and screening are frozen;
2. corpus provenance is complete;
3. reliability is reported;
4. comparator definitions are frozen;
5. nested-model and ablation results reproduce in CI;
6. temporal/disciplinary robustness is reported;
7. all headline figures/tables regenerate from committed code and frozen data.

## Falsification rule
SCDA9 is not the default winner. If KS7 or KSV8 preserves the useful distinctions with better reliability/parsimony, the theory is simplified accordingly. A null result for V or I is a valid scientific result.
