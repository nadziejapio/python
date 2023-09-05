from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("o") == ""
    assert shorten("123") == "123"
    assert shorten("cdfg") == "cdfg"