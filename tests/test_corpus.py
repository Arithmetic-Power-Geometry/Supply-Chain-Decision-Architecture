from scda.corpus import CorpusRecord, exact_duplicates, normalize_doi, normalize_title

def test_normalize_doi():
    assert normalize_doi("https://doi.org/10.1000/ABC.1") == "10.1000/abc.1"

def test_normalize_title():
    assert normalize_title("Supply-Chain: Decisions!") == "supply chain decisions"

def test_duplicate_by_doi():
    rs=[CorpusRecord("a","One",doi="10.1/x"),CorpusRecord("b","Different",doi="https://doi.org/10.1/X")]
    ds=exact_duplicates(rs)
    assert len(ds)==1 and ds[0].rule=="exact_doi"

def test_duplicate_by_title():
    rs=[CorpusRecord("a","Supply Chain Decisions"),CorpusRecord("b","Supply-chain decisions!")]
    ds=exact_duplicates(rs)
    assert len(ds)==1 and ds[0].rule=="exact_title"

def test_distinct_records_remain_distinct():
    rs=[CorpusRecord("a","Alpha"),CorpusRecord("b","Beta")]
    assert exact_duplicates(rs)==[]
