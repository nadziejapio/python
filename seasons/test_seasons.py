from seasons import get_date
import pytest
import datetime

def test_get_date():
    assert get_date("1993-01-04") == datetime.date(1993,1,4)
    with pytest.raises(ValueError):
        get_date("January 4, 1993")