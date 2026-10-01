# Open Search Execution and Audit

## Stage 1 — OpenAlex discovery
Execute O001–O005 separately. Preserve raw responses before transformation. Do not merge search families at retrieval time.

## Stage 2 — Canonicalization
Map records into the canonical corpus schema while retaining:
- OpenAlex work ID;
- DOI;
- title;
- publication year/date;
- source/venue;
- work type;
- authorship metadata;
- citation count;
- abstract/search metadata when available;
- retrieval search ID.

## Stage 3 — Deduplication
Merge repeated records across O001–O005 using normalized DOI and exact normalized title. Retain a many-to-one provenance table showing every search family that retrieved each canonical record.

## Stage 4 — Crossref verification
For DOI-bearing candidate records, verify bibliographic metadata against Crossref. Differences are logged, not silently overwritten.

## Stage 5 — Screening
Perform title/abstract screening using the frozen eligibility rules. Records lacking enough information remain uncertain until publisher verification.

## Stage 6 — Citation chaining
Use landmark papers, major reviews, and category-introducing studies as seeds for backward/forward discovery. Chained records receive explicit provenance and are screened by the same rules.

## Audit outputs
The workflow should eventually produce:
- raw retrieval artifacts;
- checksums;
- canonical corpus;
- provenance map;
- duplicate map;
- metadata discrepancy log;
- screening log;
- PRISMA-style counts appropriate to the actual open-source workflow.

## Non-negotiable rule
No numerical corpus claim enters the paper until the corresponding artifact is frozen and reproducible.
