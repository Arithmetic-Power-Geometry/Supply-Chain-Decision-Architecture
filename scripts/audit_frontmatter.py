"""Audit required manuscript front-matter sections and word counts."""
import argparse,re,json
from pathlib import Path
def words(x):return len(re.findall(r"\b[\w'-]+\b",re.sub(r"\\\w+(?:\[[^]]*\])?\{?|[{}]"," ",x)))
def grab(t,patterns):
 for p in patterns:
  m=re.search(p,t,re.I|re.S)
  if m:return m.group(1)
 return None
def audit(path):
 t=Path(path).read_text(encoding="utf-8")
 abstract=grab(t,[r"\\begin\{abstract\}(.*?)\\end\{abstract\}"])
 mgr=grab(t,[r"\\section\*?\{Managerial Relevance Statement\}(.*?)(?=\\section|\\begin\{IEEEkeywords\}|\\end\{document\})",
             r"\\section\*?\{Managerial Relevance\}(.*?)(?=\\section|\\begin\{IEEEkeywords\}|\\end\{document\})"])
 aw=words(abstract) if abstract is not None else None;mw=words(mgr) if mgr is not None else None
 issues=[]
 if abstract is None:issues.append("abstract missing")
 elif not 200<=aw<=250:issues.append(f"abstract word count {aw} outside frozen 200-250 gate")
 if mgr is None:issues.append("Managerial Relevance Statement missing")
 elif not 150<=mw<=200:issues.append(f"managerial relevance word count {mw} outside frozen 150-200 gate")
 return {"abstract_words":aw,"managerial_relevance_words":mw,"issues":issues,"status":"pass" if not issues else "fail",
 "note":"Word-count ranges are project submission gates and must be rechecked against the target journal instructions at submission time."}
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("tex");ap.add_argument("--out",default="artifacts/paper/frontmatter_v1.json");a=ap.parse_args()
 x=audit(a.tex);p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+"\n");print(json.dumps(x,indent=2));raise SystemExit(1 if x["issues"] else 0)
