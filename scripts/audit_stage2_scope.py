#!/usr/bin/env python3
import argparse,csv,re
from pathlib import Path

SCM=re.compile(r"\b(supply chain|logistics|procurement|sourcing|inventory|distribution|supplier|production|manufactur|operations|transport|warehous|fulfil|fulfill)\b",re.I)
BROAD=re.compile(r"\b(smart cit|healthcare|building|cyber|network security|energy system|construction|medical|wireless|image processing)\b",re.I)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--corpus",default="artifacts/corpus/openalex_candidate_corpus_stable.csv")
    p.add_argument("--stage2",default="artifacts/screening/stage2_screening_ledger.csv")
    p.add_argument("--output",default="artifacts/screening/stage2_scope_audit_queue.csv")
    a=p.parse_args()
    with open(a.corpus,newline="",encoding="utf-8") as f: corpus={r["record_id"]:r for r in csv.DictReader(f)}
    with open(a.stage2,newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    out=[]
    for r in rows:
        m=corpus.get(r["record_id"],{})
        title=m.get("title",""); abstract=m.get("abstract","")
        text=title+" "+abstract
        reasons=[]
        if not SCM.search(text): reasons.append("no_explicit_scm_signal")
        if BROAD.search(title) and not SCM.search(title): reasons.append("broad_domain_title")
        prov=(m.get("search_family") or m.get("search_id") or "")
        if "O004" in prov: reasons.append("broad_technology_query")
        if reasons:
            out.append({"record_id":r["record_id"],"study_type":r.get("study_type",""),"audit_reasons":";".join(reasons),"title":title,"audit_decision":"","audit_notes":""})
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        fields=["record_id","study_type","audit_reasons","title","audit_decision","audit_notes"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
    print(f"Scope audit flagged {len(out)} of {len(rows)} Stage-2 entries for semantic review; no eligibility decisions changed.")

if __name__=="__main__": main()
