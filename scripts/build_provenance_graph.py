"""Build a cryptographic provenance graph for SCDA evidence artifacts."""
from __future__ import annotations
import argparse,hashlib,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
def sha(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for x in iter(lambda:f.read(1024*1024),b""):h.update(x)
 return h.hexdigest()
def node(path,role):
 p=Path(path)
 return {"path":str(p),"role":role,"exists":p.exists(),"sha256":sha(p) if p.exists() and p.is_file() else None,
         "bytes":p.stat().st_size if p.exists() and p.is_file() else None}
def build(spec):
 s=json.loads(Path(spec).read_text(encoding="utf-8"));runs=[];errors=[]
 for job in s["jobs"]:
  inputs=[node(x,"input") for x in job.get("inputs",[])]
  outputs=[node(x,"output") for x in job.get("outputs",[])]
  script=node(job["script"],"producer")
  missing=[x["path"] for x in inputs+[script] if not x["exists"]]
  if missing:errors.append({"job":job["id"],"missing_required":missing})
  runs.append({"id":job["id"],"script":script,"inputs":inputs,"outputs":outputs,
               "parameters":job.get("parameters",{}),"paper_objects":job.get("paper_objects",[])})
 try: commit=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
 except Exception: commit=None
 return {"schema":"scda-provenance-v1","generated_utc":datetime.now(timezone.utc).isoformat(),
         "git_commit":commit,"jobs":runs,"errors":errors,"status":"pass" if not errors else "fail",
         "note":"Hashes establish artifact identity and lineage, not scientific correctness."}
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("spec");ap.add_argument("--out",default="artifacts/provenance/provenance_graph_v1.json");a=ap.parse_args()
 x=build(a.spec);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+"\n");print(json.dumps({"jobs":len(x["jobs"]),"errors":x["errors"],"status":x["status"]},indent=2));raise SystemExit(1 if x["errors"] else 0)
