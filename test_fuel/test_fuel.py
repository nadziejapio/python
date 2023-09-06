import fuel

def test_convert:
    assert fuel.convert("3/6") == 50
    with pytest.raises(ValueError):
        fuel.convert("5/4")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")

def test_gauge:
    assert fuel.gauge(0.5) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) =="F"
