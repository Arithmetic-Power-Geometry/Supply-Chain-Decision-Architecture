# Raw Bibliographic Exports

This directory is the landing zone for unmodified database exports.

## Rule
Raw exports are immutable research evidence. Never manually clean, delete, reorder, or overwrite records to improve downstream results.

## Naming
Use:
`YYYY-MM-DD_database_search-id_part.ext`

Examples:
`2026-10-01_scopus_S001_01.csv`
`2026-10-01_wos_S002_01.csv`

## Required provenance
Each export must be traceable to a row in `data/search_log.csv`, including exact executed query, execution date, filters, result count, and export filename.

## Canonical ingestion fields
Before analysis, database-specific exports are mapped into:
- record_id
- title
- year
- doi
- database
- search_id
- authors
- abstract
- author_keywords
- source_title
- document_type
- cited_by
- source_record_url

Original fields may be retained in addition.

## Integrity
Where feasible, record SHA-256 checksums in a manifest before transformation.

Raw files are inputs. Normalized, deduplicated, screened, and coded files belong in staged/processed data or workflow artifacts.
