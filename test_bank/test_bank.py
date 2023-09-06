from bank import value

def test_value_0():
    assert value("hello my friend") == 0

def test_value_20():
    assert value("hi my friend") == 20

def test_vaalue_100():
    assert value("good morning") == 100