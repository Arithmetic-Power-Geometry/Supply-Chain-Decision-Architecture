#!/usr/bin/env python3
"""Verify the frozen Stage-1 metadata snapshot after it has been restored."""
import argparse,csv,hashlib
from pathlib import Path

EXPECTED_ROWS=705
EXPECTED_SHA256="6bdcc48b9c38b37709c01474237e0650b247891449b72d4c5b2094e26845b3a9"
SENTINEL="SCDA-28ADCDD54D899FD6"

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--input",default="artifacts/frozen/stage1_openalex_candidate_corpus_stable_v1.csv")
 a=p.parse_args(); path=Path(a.input)
 if not path.exists(): raise SystemExit(f"FAIL frozen metadata snapshot missing: {path}")
 raw=path.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
 if digest!=EXPECTED_SHA256: raise SystemExit(f"FAIL frozen snapshot sha256={digest}, expected={EXPECTED_SHA256}")
 with path.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
 ids=[x["record_id"] for x in rows]
 if len(rows)!=EXPECTED_ROWS or len(set(ids))!=EXPECTED_ROWS: raise SystemExit("FAIL frozen snapshot must contain 705 unique record_ids")
 if SENTINEL not in set(ids): raise SystemExit(f"FAIL sentinel record absent: {SENTINEL}")
 print(f"PASS frozen Stage-1 metadata: rows={len(rows)} unique={len(set(ids))} sha256={digest} sentinel={SENTINEL}")

if __name__=="__main__": main()
