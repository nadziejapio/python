from plates import is_valid

def test_is_valid_two_letters():
    assert is_valid("AAbcd1") == True
    assert is_valid("12abcd") == False

def test_is_valid_min_max():
    assert is_valid("A") == False
    assert is Valid("ABDCSD2") == False

def test_is_valid_numbers():
    assert is valid("")