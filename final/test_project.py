import project
import pytest

def test_load_player():
    assert project.load_player('Nadzieja') == 'something is wrong'

def 