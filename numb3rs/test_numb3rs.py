from numb3rs import validate

def test_numb3rs_nums():
    assert validate("255.255.255.0") == True
    assert validate("275.0.3.68") == False

def test_numb3rs_words():
    assert validate("cat") == False