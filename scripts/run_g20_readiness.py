"""G20 adversarial submission-readiness gate."""
import argparse,json
from pathlib import Path
CHECKS=[
("retrieval_integrity","artifacts/corpus/retrieval_integrity_v1.json",True),
("screening_flow","artifacts/corpus/screening_flow_v1.json",True),
("reliability","artifacts/reliability/reliability_v1.json",True),
("nested_models","artifacts/model_competition/nested_primary_v1.json",True),
("generalization","artifacts/generalization/generalization_report_v1.json",True),
("evidence_layer","artifacts/evidence_layer/matched_case_v1.json",True),
("context_layer","artifacts/context_layer/matched_case_v1.json",True),
("robustness","artifacts/robustness/robustness_v1.json",True),
("managerial_value","artifacts/managerial/decision_usefulness_v1.json",True),
("claim_provenance","artifacts/integrity/claim_provenance_validation_v1.json",True),
("reference_audit","artifacts/integrity/reference_audit_v1.json",True),
("provenance_graph","artifacts/provenance/provenance_graph_v1.json",True),
("claim_alignment","artifacts/paper/claim_alignment_v1.json",True)]
def state(path):
 p=Path(path)
 if not p.exists():return "NOT-YET-EVALUABLE",None
 try:o=json.loads(p.read_text(encoding="utf-8"))
 except Exception:return "BLOCKED","unreadable artifact"
 s=str(o.get("status","")).lower()
 if s in {"pass","passed","ok"}:return "PASS",None
 if s in {"fail","failed","blocked"}:return "BLOCKED",s
 return "NOT-YET-EVALUABLE",f"artifact status={s or 'unspecified'}"
def run():
 rows=[];blocked=[];pending=[]
 for name,path,required in CHECKS:
  s,n=state(path);rows.append({"gate":name,"artifact":path,"state":s,"note":n})
  if required and s=="BLOCKED":blocked.append(name)
  if required and s=="NOT-YET-EVALUABLE":pending.append(name)
 overall="BLOCKED" if blocked else ("NOT-YET-EVALUABLE" if pending else "PASS")
 return {"overall":overall,"checks":rows,"blocked":blocked,"not_yet_evaluable":pending,
 "paper_construction_authorized":overall=="PASS",
 "note":"PASS means the registered evidence gates are satisfied; it is not a guarantee of journal acceptance."}
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("--out",default="artifacts/final/g20_readiness_v1.json");a=ap.parse_args()
 x=run();p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+"\n");print(json.dumps(x,indent=2));raise SystemExit(1 if x["overall"]=="BLOCKED" else 0)
