# Coder-B Final Handoff Gate

The file `data/frozen/coder_b_blinded_sample_FINAL_v1.csv` MUST NOT be created until all conditions below pass.

- [ ] retained-primary source-sufficiency review complete
- [ ] every retained-primary record has one of: admissible claim(s), zero-claim-with-reason, or role reclassification
- [ ] all pre-reliability adjudications resolved
- [ ] production claim validator passes
- [ ] admissible Reviewer-A corpus frozen
- [ ] SHA-256 digest recorded
- [ ] final sample generated from frozen corpus using `scripts/prepare_claim_reliability_sample.py`
- [ ] sample contains at least 20% of frozen claims and keeps every sampled publication intact
- [ ] Reviewer-A labels absent from blinded sample
- [ ] sample manifest records corpus digest, sample digest, claim/study counts and generation rule

Current status: BLOCKED. The final filename is intentionally absent until this gate passes.
