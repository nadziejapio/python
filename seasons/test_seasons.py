from seasons import get_date
import pytest

def test_get_date():
    assert get_date("1993-01-04") == "1993-01-04"
    with pytest.raises(ValueError):
        get_date("January 4, 1993")