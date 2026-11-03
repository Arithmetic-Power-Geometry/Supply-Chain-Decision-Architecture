# IJIEOM submission package — review-readiness audit (2026-11-03)

**Disposition: CONDITIONAL / NOT CERTIFIED AS FULLY REVIEW-READY.**

This record distinguishes the materials actually inspected from repository-wide checks that could not be completed. It does not alter historical evidence or scientific results.

## Inputs inspected

- Author-provided `SCDA_IJIEOM_ok(2).zip` (14 files; main manuscript, tables, supplement, title page, LaTeX sources, bibliography, figures).
- The current repository `README.md`, `EMSUB/README.md`, `EMSUB/evidence/README.md`, `EMSUB/audit/UPLOADED_EVIDENCE_REVIEW_20261103.md`, `EMSUB/audit/CODER_RELIABILITY_RECONCILIATION_20261103.md`, and `EMSUB/audit/P03_HANDOFF_AND_MANUSCRIPT_CLAIMS_20261103.md`.
- Repository code-search attempts for `prompt`, `P01`, `audit`, `handoff`, `README`, `TODO`, `AI`, and `ChatGPT` returned no results. **This is not evidence of a clean full repository tree**: search may not index this repository. A complete tree listing, file-by-file scan, and Git-history scan were unavailable through the connected interface. No such inspection is claimed.

## Exact package checks

| File | Pages | Extracted whitespace-delimited words | SHA-256 prefix | Review status |
| --- | ---: | ---: | --- | --- |
| Anonymous `main.pdf` | 21 | 6,865 | `a46c02f7f6e205cb` | Text and PDF metadata checked |
| Separate `tables.pdf` | 6 | 337 | `2bfc521d3178d37f` | Text and PDF metadata checked |
| Anonymous `supplement.pdf` | 23 | 7,324 | `c2cfb4362e4f97eb` | Text and PDF metadata checked |
| Confidential `title_page.pdf` | 1 | 159 | `ad6b061cffcb750f` | Contains author identities as intended; not for anonymous review |

The PDFs' `author` metadata fields were empty. Case-insensitive searches of all packaged `.tex`, `.bib`, and extracted PDF text did not find exact strings `prompt`, `ChatGPT`, `Codex`, `LLM`, `AI-assisted`, `author instruction`, `TODO`, or `placeholder`. This does **not** establish that no AI was used; it establishes only absence of these strings in inspected material. Figure images and visual layout were not exhaustively inspected for embedded text. No OCR or independent full visual proof was performed.

The confidential title-page source in this *latest* package attributes primary coding (Coder A) to Md Saifullah Khalid and second coding (Coder B) to Arvind Hans. This corrects the mismatch reported for an earlier package in `P03_HANDOFF_AND_MANUSCRIPT_CLAIMS_20261103.md`. This is a **document consistency correction**, not independent verification of the historical coding roles or coauthor approval.

## Results and limitations to preserve

- Candidate records: 705; stage-2: 659; retained: 518; excluded: 141.
- Deep-review corpus: 125 studies; primary analytical subset: 121 studies; source-supported analytical claims: 124.
- Collision: K4 52.42%, KS7 19.35%, KSV8 17.74%, SCDA9 12.90%.
- Nine dimension-wise kappas: 0.036–0.712. Eight of nine are below the prespecified 0.67 threshold.
- The earlier reliability protocol and the 125-study calculation differ in unit of analysis and treatment of blank theory values.
- The original independent coder handoff chronology and pre-adjudication provenance remain unverified; the historical handoff gate must not be retrospectively marked PASS.
- The prespecified 2024–2026 temporal holdout is empty. Collision reduction alone does not validate the taxonomy or establish organisational performance benefits.

## Remaining submission and repository gates

1. **Journal proof:** Authors must open the ScholarOne-generated PDF proof and verify the structured abstract, correct order, complete figures/tables, and anonymity. A local ZIP check is not the journal-generated proof.
2. **AI-use declaration:** Emerald's submission form requires accurate disclosure in Methods and Acknowledgements if an AI tool was used to develop or generate any portion of the manuscript. The inspected main source has no `Acknowledg` heading. Authors must resolve the disclosure based on actual use, not the absence of tool-name strings.
3. **Independent coding evidence:** Preserve original dated Coder A/B returns, handoff and freeze provenance if available; obtain factual coauthor approval for the contribution statement. Do not invent or backdate records.
4. **Original evidence availability:** The original binary paired-coder workbook and other uploaded workbooks were not committed to `EMSUB/evidence/` at the time of the inspected evidence README. Reproduction from the repository alone is therefore incomplete.
5. **Full-repository inspection:** Enumerate the full default-branch tree and, separately, Git history before claiming all prompt/workflow material has been reviewed. Do not delete provenance, reproducibility data, historical audits, or evidence of AI assistance to misrepresent research conduct.
6. **Scientific interpretation:** Keep the reliability protocol departure, coder sensitivity, empty temporal holdout, and conditional model-depth conclusion visible to reviewers.

## Publication-facing organisation

The top-level repository README and `EMSUB/README.md` describe the research questions, data, methods, reproduction commands, results and limitations. Older process documents and original audit records remain intact for provenance; this audit does not certify or rewrite them. No numerical values, original source workbooks, frozen datasets, experimental scripts, or Git history were changed.

**Outcome:** The submitted ZIP is textually free of the tested prompt/AI-tool strings and has blank PDF author metadata in the anonymous files. Scientific provenance and journal disclosure gates remain open. Do not label the repository or manuscript `fully verified`, `100% review-ready`, or `AI-free`.
