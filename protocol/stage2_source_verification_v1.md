# Stage-2 Source Verification Protocol v1

Stage-2 eligibility is evidence-led and record-specific. Bibliographic discovery, source acquisition, and eligibility are separate operations.

For each acquisition-batch record, the execution ledger preserves the stable record ID and discovery metadata. Source verification then records the scholarly source type, persistent identifier or location, bibliographic verification state, evidence-access state, and an evidence note sufficient to audit the decision.

A DOI match or metadata match verifies identity only; it does not establish eligibility. An abstract may support a decision only when it contains enough information to apply the frozen eligibility criteria. Otherwise the record remains pending or uncertain until stronger source evidence is available. Failure of automated full-text retrieval does not itself justify exclusion.

A terminal Stage-2 decision requires a documented source state and evidence note. Exclusions require E01-E10. Includes require primary or review/synthesis routing. Source-supported decisions made by Reviewer A remain AI-assisted and do not substitute for the independent coder-B reliability sample.

Batch validation is fail-closed: malformed source states, unsupported terminal decisions, missing exclusion codes, missing study routing, or absent evidence notes cause the validator to fail. No batch is merged into the frozen eligible corpus until its evidence audit passes and required adjudication is complete.
