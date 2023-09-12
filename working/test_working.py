import pytest
from working import convert

def test_convert_ve():
    with pytest.raises(ValueError):
        convert("8:61 AM to 11 AM")
    with pytest.raises(ValueError):
        convert("8:00 AM to 11:65 AM")

def test_convert_minutes():
    assert convert("8 AM to 11 AM") == "08:00 to 11:00"

def test_convert_pm():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"