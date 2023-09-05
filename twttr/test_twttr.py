from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("o") == ""
    assert shorten("123") == "123"
    assert shorten("cd.fg") == "cd.fg"