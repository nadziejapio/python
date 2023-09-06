import fuel

def test_convert:
    assert fuel.convert() ==

def test_gauge:
    assert fuel.gauge(0.5) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F