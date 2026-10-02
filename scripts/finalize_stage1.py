#!/usr/bin/env python3
import argparse,csv,glob,json
from pathlib import Path

VALID_DECISIONS={"include","exclude"}
VALID_TYPES={"primary","review"}
VALID_EXCLUSIONS={f"E{i:02d}" for i in range(1,11)}

def rows(path):
    with open(path,newline="",encoding="utf-8-sig") as f:return list(csv.DictReader(f))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--base",required=True)
    p.add_argument("--batches",default="data/screening/adjudication_source_batch*_v1.csv")
    p.add_argument("--ledger",default="artifacts/screening/stage1_final_ledger.csv")
    p.add_argument("--stage2",default="artifacts/screening/stage2_queue.csv")
    p.add_argument("--audit",default="artifacts/screening/stage1_final_audit.json")
    a=p.parse_args()
    base=rows(a.base)
    if len(base)!=705: raise SystemExit(f"FAIL base rows={len(base)} expected=705")
    ids=[x["record_id"] for x in base]
    if len(set(ids))!=705: raise SystemExit("FAIL duplicate base record_id")

    upd={}
    for fn in sorted(glob.glob(a.batches)):
        for x in rows(fn):
            rid=x["record_id"]
            if rid in upd: raise SystemExit(f"FAIL duplicate adjudication {rid}")
            upd[rid]=x
    if len(upd)!=147: raise SystemExit(f"FAIL adjudications={len(upd)} expected=147")
    if set(upd)-set(ids): raise SystemExit("FAIL adjudication ID absent from base")

    for x in base:
        u=upd.get(x["record_id"])
        if u:
            x["decision"]=u["decision"]
            x["exclusion_reason"]=u.get("exclusion_reason","")
            x["study_type"]=u.get("study_type","")
            x["adjudication_required"]="no"
            x["confidence"]="source-verified"
        d=x["decision"]
        if d not in VALID_DECISIONS: raise SystemExit(f"FAIL nonterminal decision {x['record_id']}={d}")
        if d=="include" and x.get("study_type","") not in VALID_TYPES:
            raise SystemExit(f"FAIL included record without primary/review routing {x['record_id']}")
        if d=="exclude" and x.get("exclusion_reason","") not in VALID_EXCLUSIONS:
            raise SystemExit(f"FAIL excluded record without valid E-code {x['record_id']}")

    inc=[x for x in base if x["decision"]=="include"]
    exc=[x for x in base if x["decision"]=="exclude"]
    if (len(inc),len(exc))!=(659,46):
        raise SystemExit(f"FAIL expected 659/46, got {len(inc)}/{len(exc)}")

    Path(a.ledger).parent.mkdir(parents=True,exist_ok=True)
    fields=list(base[0])
    for fn,data in [(a.ledger,base),(a.stage2,inc)]:
        with open(fn,"w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)

    audit={"candidate_records":705,"unique_record_ids":705,"adjudications":147,
           "include":659,"exclude":46,"uncertain":0,"stage2_queue":659,
           "duplicate_adjudication_ids":0,"conflicting_adjudications":0,
           "routing_complete":True,"terminal_decisions_complete":True}
    with open(a.audit,"w",encoding="utf-8") as f:json.dump(audit,f,indent=2)
    print(json.dumps(audit,indent=2))

if __name__=="__main__": main()
