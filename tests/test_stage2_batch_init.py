import csv,hashlib
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess,sys

def test_batch_membership_matches_builder_order():
    with TemporaryDirectory() as td:
        td=Path(td)
        ledger=td/"ledger.csv"; corpus=td/"corpus.csv"; out=td/"out"
        rows=[{"record_id":f"R{i:03d}"} for i in range(659)]
        with ledger.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=["record_id"]);w.writeheader();w.writerows(rows)
        with corpus.open("w",newline="",encoding="utf-8") as f:
            fields=["record_id","openalex_id","doi","title","year","search_family","abstract"]
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
            for r in rows:w.writerow({"record_id":r["record_id"],"title":r["record_id"]})
        subprocess.run([sys.executable,"scripts/init_stage2_batch.py","--batch-id","B02","--ledger",str(ledger),"--corpus",str(corpus),"--output-dir",str(out)],check=True)
        with (out/"B02_source_verification_enriched.csv").open(newline="",encoding="utf-8") as f: got=[r["record_id"] for r in csv.DictReader(f)]
        expected=[r["record_id"] for r in sorted(rows,key=lambda x:hashlib.sha256(x["record_id"].encode()).hexdigest())][25:50]
        assert got==expected
