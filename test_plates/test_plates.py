from plates import is_valid

def test_is_valid_two_letters():
    assert is_valid("AAbcd1") == True
    assert is_valid("12abcd") == False

def test_is_valid_min_max():
    assert is_valid("A") == False
    assert is_valid("ABDCSD2") == False

def test_is_valid_numbers():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

def test_is_valid_puntuation():
    assert is_valid("AA,,22") == False