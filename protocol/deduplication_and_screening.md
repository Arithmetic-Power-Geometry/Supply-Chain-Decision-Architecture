# Deduplication and Screening Procedure

## Deduplication hierarchy
1. Exact normalized DOI.
2. Exact normalized title.
3. Fuzzy title match requiring manual confirmation.
4. Same work appearing as online-first and issue version is retained once.

Never deduplicate solely on author/year.

## Screening decisions
Allowed values: include, exclude, uncertain.

Every exclusion after title/abstract screening receives a reason code:
E1 incidental SCM context
E2 isolated technical operation without SCM implication
E3 wrong document type
E4 review/framework (route to review corpus)
E5 duplicate
E6 insufficient scholarly metadata
E7 non-English
E8 other, with explanation

Full-text exclusion is logged independently.

## Reliability
Before full production screening, independently screen a calibration sample. Resolve codebook ambiguities, then freeze screening guidance. Later reliability is measured on a random blinded subset.

## Provenance
Every final record must retain database/search-family origin. Citation-chained records retain the seed study from which they were discovered.

## Reproducibility
No record is manually deleted from the raw export. Transformations create new staged files so the raw retrieval remains immutable.
