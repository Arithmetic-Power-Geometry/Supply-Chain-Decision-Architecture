import csv
from pathlib import Path
from tempfile import TemporaryDirectory
from scda.ingest import ingest_csv, stable_record_id

def test_stable_record_id():
    a=stable_record_id("Scopus","S001","10.1/X","Alpha",1)
    b=stable_record_id("Scopus","S001","https://doi.org/10.1/x","Different",9)
    assert a==b

def test_scopus_like_csv_ingest():
    with TemporaryDirectory() as d:
        p=Path(d)/"x.csv"
        with p.open("w",encoding="utf-8",newline="") as f:
            w=csv.DictWriter(f,fieldnames=["Title","Year","DOI","Authors","Abstract"])
            w.writeheader(); w.writerow({"Title":"A Study","Year":"2024","DOI":"10.1/a","Authors":"A","Abstract":"Text"})
        rows,meta=ingest_csv(p,"Scopus","S001")
        assert rows[0]["title"]=="A Study"
        assert rows[0]["database"]=="Scopus"
        assert meta["rows"]==1
        assert len(meta["sha256"])==64

def test_wos_like_csv_ingest():
    with TemporaryDirectory() as d:
        p=Path(d)/"x.csv"
        with p.open("w",encoding="utf-8",newline="") as f:
            w=csv.DictWriter(f,fieldnames=["Article Title","Publication Year","DOI","Author Full Names","Times Cited"])
            w.writeheader(); w.writerow({"Article Title":"B Study","Publication Year":"2023","DOI":"","Author Full Names":"B","Times Cited":"4"})
        rows,_=ingest_csv(p,"WoS","S002")
        assert rows[0]["title"]=="B Study"
        assert rows[0]["cited_by"]=="4"
