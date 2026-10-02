# Independent Coder B — Human Coding Instructions

## Final file to complete
When the Reviewer-A production corpus is frozen, complete:

`data/frozen/coder_b_blinded_sample_FINAL_v1.csv`

Do **not** use `coder_b_blinded_sample_PRELIMINARY_v1.csv` for final reliability.

## Independence requirement
Coder B must code independently. Do not inspect:
- `data/production_claims_final_v1.csv`
- Reviewer-A dimension values
- Reviewer-A confidence or notes
- architecture/model-comparison outputs.

Coder B may inspect the claim text, cited source/source location, and the frozen codebook.

## Fields to code
For every row, fill:
1. decision_level
2. process
3. flow
4. objective
5. theory
6. method
7. technology
8. evidence_maturity
9. context
10. confidence

Leave claim_id, study_id, record_id, claim_text, claim_location, source_support and source_identifier unchanged.

## Frozen categories
### decision_level
Strategic; Tactical; Operational; Real-time/autonomous

### process
Plan; Source; Make; Store; Move; Deliver; Return; Recover; Enable

### flow
Material; Information; Financial; Knowledge; Risk; Carbon

### objective
Cost; Service; Quality; Speed; Flexibility; Resilience; Sustainability; Trust

### theory
Record an explicitly declared theoretical lens only. Do not infer a management theory from the topic. Leave blank when none is explicitly supported.

### method
Conceptual; Empirical; Optimization; Simulation; Statistics; Machine Learning; Artificial Intelligence; Multi-agent/Autonomous

### technology
Record the principal enabling technology when the claim is technology-dependent; otherwise use None.

### evidence_maturity
Conceptual; Synthetic; Simulation; Benchmark; Case study; Observational; Pilot; Deployed; Longitudinal

### context
Record the reported application/industry context. Use General only when no specific context is central.

### confidence
certain; probable; ambiguous

## Coding rule
Code the focal substantive claim supported by the supplied source evidence. Do not code from title alone. Do not invent a dimension merely to avoid a blank value. If genuinely ambiguous, choose the best-supported value only when defensible and mark confidence=ambiguous; otherwise leave the unsupported field blank.

## Return
Save the completed file without changing its filename or row order and return it to the project owner. Reliability is computed on the independent, pre-adjudication values before Reviewer A and Coder B discuss disagreements.
