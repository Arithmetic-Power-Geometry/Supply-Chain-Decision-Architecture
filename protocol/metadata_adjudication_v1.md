# Metadata Verification and Adjudication v1

## Principle
Discovery metadata and verification metadata are separate evidence layers. Crossref verification never silently overwrites OpenAlex retrieval records.

## Automated flags
A DOI-bearing record is flagged for manual/source adjudication when:
1. Crossref returns no DOI record;
2. normalized title similarity is below 0.80;
3. publication years disagree;
4. Crossref work type is inconsistent with the screened scholarly record;
5. DOI duplication links apparently different titles.

Title similarity >=0.90 is a high-agreement diagnostic, not proof of eligibility. Similarity 0.80--0.8999 remains acceptable for automated metadata agreement but may still be reviewed during screening.

## Authority order for disputed metadata
1. publisher/version-of-record page or DOI landing metadata;
2. Crossref DOI metadata;
3. OpenAlex discovery metadata.

This order resolves bibliographic identity only. It does not determine study eligibility, claim coding or evidence maturity.

## Audit trail
Corrections are written to a separate adjudication table containing source value, verification value, final value, reason, evidence source and reviewer. Raw retrieval pages remain immutable.

## Publication reporting
Report DOI coverage, Crossref verification rate, title-disagreement count, year-disagreement count and unresolved metadata cases. Do not describe a DOI as verified when verification failed.
