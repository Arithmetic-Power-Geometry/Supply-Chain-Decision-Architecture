"""Static manuscript mechanics audit for LaTeX."""
import argparse,re,json
from pathlib import Path
def audit(path):
 t=Path(path).read_text(encoding="utf-8")
 labels=re.findall(r"\\label\{([^}]+)\}",t); refs=re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}",t)
 cites=re.findall(r"\\cite\w*\{([^}]+)\}",t)
 bad=["??","TODO","TBD","PLACEHOLDER","FIXME"]
 unresolved=[x for x in bad if x.lower() in t.lower()]
 dup=sorted(k for k in set(labels) if labels.count(k)>1)
 missing=sorted(set(refs)-set(labels));unused=sorted(set(labels)-set(refs))
 floats=[]
 for typ in ("figure","table","algorithm"):
  for m in re.finditer(r"\\begin\{"+typ+r"\}.*?\\end\{"+typ+r"\}",t,re.S):
   block=m.group(0);lab=re.search(r"\\label\{([^}]+)\}",block)
   floats.append({"type":typ,"label":lab.group(1) if lab else None,"has_caption":bool(re.search(r"\\caption\{",block))})
 errors=[]
 if unresolved:errors.append("placeholder/unresolved tokens present")
 if dup:errors.append("duplicate labels")
 if missing:errors.append("references to missing labels")
 if any(not x["label"] or not x["has_caption"] for x in floats):errors.append("float missing label/caption")
 return {"labels":len(labels),"references":len(refs),"citation_commands":len(cites),"unresolved_tokens":unresolved,
 "duplicate_labels":dup,"missing_labels":missing,"unused_labels":unused,"floats":floats,"errors":errors,"status":"pass" if not errors else "fail"}
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("tex");ap.add_argument("--out",default="artifacts/paper/mechanics_v1.json");a=ap.parse_args()
 x=audit(a.tex);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+"\n");print(json.dumps(x,indent=2));raise SystemExit(1 if x["errors"] else 0)
