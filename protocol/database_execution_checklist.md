# Database Search Execution Checklist

Complete one row/check for every S001–S008 search.

## Before execution
- Confirm database is Scopus or Web of Science Core Collection.
- Use the frozen query file verbatim.
- Confirm Article and English filters.
- Confirm no unintended subject-area restriction.
- Confirm historical coverage has no lower year cutoff.

## Record immediately
- Search ID.
- Database.
- Date and local time.
- Exact query/version.
- Result count shown by database.
- Applied filters.
- Export format.
- Number of exported files/batches.
- Any database export limit encountered.

## Export
Prefer CSV plus RIS/BibTeX when practical. Include the richest available metadata. Large result sets may require multiple numbered export batches.

## After export
- Do not edit raw files.
- Name files according to data/raw/README.md.
- Calculate checksum when ingested.
- Reconcile sum of exported batch counts against displayed database count.
- Log discrepancies before deduplication.

## Failure rule
If database syntax, export limits, indexing behavior, or access restrictions require changing a query, do not silently alter it. Record the issue and create a versioned protocol amendment before rerunning.

## Handoff
The raw files are the next inputs to the deterministic normalization and deduplication pipeline. Search counts remain empirical values and must never be estimated.
