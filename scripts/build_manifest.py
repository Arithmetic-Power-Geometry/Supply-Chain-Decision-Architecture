"""Build SHA-256 manifest for generated evidence artifacts."""

from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path("artifacts")
OUT=ROOT/"manifest.json"

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def main() -> None:
    ROOT.mkdir(exist_ok=True)
    files=[]
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p != OUT:
            files.append({"path":p.as_posix(),"bytes":p.stat().st_size,"sha256":sha256(p)})
    OUT.write_text(json.dumps({"schema_version":1,"files":files},indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
