# Generalization and Holdout Protocol v1

## Unit of partition
The publication/study is the indivisible partitioning unit. All claims from the same study remain in the same partition. Claim-level random splitting is prohibited.

## Development/holdout split
A deterministic SHA-256 assignment based on stable study_id places approximately 20% of studies in the general holdout. The salt and algorithm are frozen in code before large-corpus model results are inspected.

The development partition may be used to clarify codebook wording and compare candidate architectures. Once the architecture/codebook is frozen, the holdout is opened for evaluation.

## Temporal stress test
A separate temporal test treats studies from 2024--2026 as the recent-period holdout and earlier studies as development/history. This asks whether the representation transfers to recent AI, digital-twin, resilience and autonomous-decision research rather than merely fitting older SCM literature.

## Disciplinary stress test
For each sufficiently represented discipline, evaluate a leave-one-discipline-out test: management/organization, OR/optimization, industrial engineering/operations, information systems/digital, and AI/data science where defensible.

A discipline with too few independent publications is reported as underpowered rather than pooled opportunistically.

## Metrics
For each partition report model coverage, collision rate, distinct signatures, signature entropy and the selected smallest-adequate architecture under the frozen competition rule. Dimension-level missingness and reliability are reported alongside these metrics.

## Leakage checks
CI must fail if any study_id appears in more than one partition. Multiple claims from a paper are never counted as independent publications.

## Holdout integrity
Holdout results may falsify or weaken the proposed architecture. If holdout results lead to a redesign, the redesigned model is a new version and the used holdout is no longer described as untouched validation. A new external or future validation set is then required for a clean confirmatory test.

## Interpretation
Generalization is supported only to the eras and disciplines represented by the evaluated corpus. Absence of evidence in an underrepresented stratum is not evidence of universality.
