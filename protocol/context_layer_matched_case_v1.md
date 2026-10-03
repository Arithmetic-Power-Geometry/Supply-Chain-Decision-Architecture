# Context-Layer Matched-Case Falsification Protocol v1

## Question
Does context/industry I add reproducible boundary information after decision kernel, solution and evidence maturity are held approximately constant?

## Primary exact-match key
decision level + process + flow + objective + theory + method + technology + evidence maturity.

A matched group contains at least two claims. Cross-study matched groups are distinguished from multiple claims within one publication.

## Context coding
Context records the empirical/application environment supported by the source. It must not be inferred from author affiliation, journal title or technology alone. "General" is used only when the claim is explicitly cross-sector/general or no narrower application context is part of the claim.

Context labels must be normalized under the frozen codebook before analysis. Synonyms must not be counted as different industries merely because wording differs.

## Primary diagnostics
For each matched group report claim count, independent-study count, observed normalized contexts, context count and whether variation crosses independent publications.

Report both overall context-variation rate and cross-study context-variation rate.

## Interpretation
Different context labels are not sufficient to establish a core architecture dimension. Evidence for I is stronger when context is:
1. independently codable;
2. non-redundant after K+S+V matching;
3. associated with reproducible boundary conditions, applicability differences or outcome interpretation;
4. stable across holdouts.

## Architecture consequence
If I repeatedly contributes reliable boundary information and improves out-of-sample representation, SCDA9 remains viable.
If I primarily says where a claim was studied without changing decision/solution identity, retain context as an orthogonal boundary-condition annotation.
If context coding is unreliable, redundant or too sparse, demote/remove it from the core representation.

No architecture version is privileged in advance.
