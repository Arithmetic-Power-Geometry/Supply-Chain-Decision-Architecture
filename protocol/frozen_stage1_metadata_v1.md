# Frozen Stage-1 metadata provenance v1

Stage-2 screening is bound to the exact candidate metadata snapshot that produced the frozen Reviewer-A Stage-1 screening universe. Fresh OpenAlex retrieval is retained as a reproducibility/update diagnostic and MUST NOT silently replace metadata for already-screened stable record IDs.

Frozen source:
- GitHub Actions run: 36981846265 (run #199)
- Head SHA: 4749e7b318c760ebb256e79c35fcef2654d2b395
- Artifact: scda-evidence
- Artifact ID: 11215299923
- Artifact digest: sha256:bbcb768fce87845525e13f3f652271c81568a556f73c1181766eb441b526ea11
- Frozen file: artifacts/corpus/openalex_candidate_corpus_stable.csv
- Frozen records: 705 unique stable record IDs

The workflow restores this pinned snapshot to data/frozen/stage1_candidate_metadata_v1.csv and verifies the artifact digest, row count, uniqueness, and a known drift sentinel record before Stage-2 initialization.

Scientific rule: a record may leave the eligible corpus only through documented screening/adjudication. It must never disappear because an external discovery index changes between workflow runs.

The pinned workflow artifact currently expires on 2026-12-31. Before branch merge/public release, the snapshot must be moved to a durable repository or archival data asset without changing its bytes or provenance identity.

Frozen stable-corpus file SHA-256: 6bdcc48b9c38b37709c01474237e0650b247891449b72d4c5b2094e26845b3a9.
Known drift sentinel: SCDA-28ADCDD54D899FD6.
