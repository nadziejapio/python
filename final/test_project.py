import project
import pytest

def test_load_player():
    assert project.load_player('Nadzieja') == 'something is wrong'

def test_login_to_facebook():
    assert project.login_to_facebook()

def test_check_player_status():
    assert project.check_player_status() == 'checked'