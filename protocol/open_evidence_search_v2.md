# Open Evidence Search Protocol — v2.0

Status: active protocol
Activation date: 2026-10-01

## Reason for amendment
The original protocol specified Scopus and Web of Science as primary retrieval databases. Those subscription databases are not available for execution in the present research workflow. They are therefore not reported as searched.

Version 1 remains in the repository as a historical preregistration record. This amendment changes retrieval sources, not the SCDA dimensions or the frozen comparative evaluation plan.

## Primary discovery source
OpenAlex is used for broad scholarly discovery and citation-network expansion.

## Independent metadata/DOI verification
Crossref is used to verify DOI-centered bibliographic metadata and supplement missing publisher metadata where available.

## Publisher verification
Publisher/DOI landing pages are used for records requiring confirmation of title, venue, year, article type, or abstract-level eligibility.

## Retrieval families
The conceptual families remain unchanged:
F1 broad SCM
F2 decisions and operations
F3 analytics and computation
F4 management and theory

The open retrieval implementation must preserve the query text, execution timestamp, returned count where exposed, pagination state, and raw response files.

## Eligibility
Primary quantitative corpus:
- scholarly journal articles;
- English-language records where language metadata/abstract screening permits determination;
- publication date through the final 2026 search date;
- material examination of a supply-chain phenomenon, decision, coordination mechanism, model, capability, technology, or outcome.

Reviews remain in the review-of-reviews layer rather than the primary quantitative corpus.

## Triangulation
No source is assumed complete. OpenAlex provides discovery; Crossref provides independent DOI/metadata verification; publisher pages resolve material discrepancies. Citation chaining supplements keyword retrieval.

## Deduplication
Deduplicate using normalized DOI first, then normalized title with manual confirmation of uncertain near-matches. Preserve all source provenance.

## Bias control
The SCDA coding dimensions, layered architecture, evaluation metrics, ablation plan, and interpretation rules remain frozen before retrieval results are analyzed.

## Reporting rule
The paper must name the sources actually searched. It must not state or imply Scopus or Web of Science coverage unless those databases are later executed and logged.

## Limitation
An open-index corpus is not equivalent to a Scopus/Web of Science corpus. Coverage differences and metadata incompleteness are reported as limitations and tested where possible through citation chaining and publisher verification.
