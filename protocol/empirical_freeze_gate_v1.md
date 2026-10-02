# Production evidence gate status

The architecture competition is fail-closed.

K4, KS7, KSV8 and SCDA9 headline analyses must not be treated as manuscript results until:
1. retained-primary source acquisition/extraction is declared complete;
2. production claims pass the frozen coding/provenance validators;
3. pre-reliability adjudications are resolved;
4. the production claim corpus is frozen with a digest;
5. a blinded publication-clustered >=20% claim sample is independently coded by Coder B;
6. pre-adjudication reliability is frozen;
7. any reliability-triggered codebook action is documented.

`scripts/check_empirical_freeze_gate.py` intentionally exits non-zero while these conditions remain unmet.
