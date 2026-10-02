# Large-Corpus Validation v1

This branch executes the active open-evidence protocol before any field-wide SCDA claim is written.

## Retrieval
Four frozen OpenAlex query families are executed independently. Raw JSON pages and retrieval manifests are preserved as workflow evidence. The first validation run is deliberately bounded to two 100-record pages per family (maximum 800 raw records) so that screening and coding remain auditable.

## Corpus construction
Records are deduplicated by normalized DOI, then normalized title. Query-family provenance is retained. The resulting CSV is a **candidate corpus**, not an included-study corpus.

## Validation stages
1. retrieval and provenance;
2. DOI/title deduplication;
3. eligibility screening;
4. stratified sampling across eras and query families;
5. claim-level SCDA coding with uncertainty;
6. independent/second coding on a substantial sample;
7. agreement statistics;
8. K4/KS7/KSV8/SCDA9 comparison;
9. leave-one-dimension-out ablation;
10. comparator-framework stress test.

No automated keyword classifier is allowed to stand in for scholarly claim coding. No large-corpus SCDA result is reported until stages 3--10 are complete.
