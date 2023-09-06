from plates import is_valid

def test_is_valid_two_letters():
    assert is_valid("-/dsvc") == False
    assert is_valid("A12acd") == False
    assert is_valid("1A2acd") == False

def test_is_valid_min_max():
    assert is_valid("A") == False
    assert is_valid("ABDCSD2") == False
    assert is_valid("") == False

def test_is_valid_numbers():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAAB02") == False

def test_is_valid_puntuation():
    assert is_valid("AA,,22") == False