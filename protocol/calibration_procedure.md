# Coding Calibration Procedure

## Purpose
Calibrate interpretation before production coding and expose ambiguous codebook boundaries without using real-corpus outcomes to tune SCDA.

## Phase 1 — synthetic calibration
Code the scenarios in data/calibration_set.csv without consulting the answer fields, then compare against the frozen reference codes.

## Phase 2 — landmark calibration
Independently code a subset of landmark papers after inspecting abstracts/full text. Record disagreements rather than forcing consensus.

## Phase 3 — codebook amendment
Amend definitions only when disagreement reveals genuine ambiguity. Every amendment receives a version, date, rationale, and affected dimensions.

## Phase 4 — freeze
Freeze the production codebook before systematic-corpus headline analysis.

## Reliability design
A second independent coding pass/coder should evaluate a random stratified subset of the real corpus. Report per-dimension agreement and Cohen's kappa where assumptions are appropriate. Do not invent independent coding.

## Decision rule
If a dimension is repeatedly ambiguous, unreliable, or adds negligible non-redundant information in ablation, simplify or remove it rather than preserving the original nine-dimensional design.
