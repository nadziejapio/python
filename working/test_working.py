import pytest
from working import convert

def test_convert_ve():
    with pytest.raises(ValueError):
        convert("8:61 AM to 11 AM")
    with pytest.raises(ValueError):
        convert("8:00 AM to 11:65 AM")

def test_convert_