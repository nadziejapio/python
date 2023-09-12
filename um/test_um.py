from um import count

def test_word():
    assert count("sodium") == 0

def test_space():
    assert count(" Um.") == 1

def test_nospace():
    assert count(",um,") == 1