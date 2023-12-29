import project
import pytest

def test_load_player():
    assert project.load_player('Nadzieja') == 'something is wrong'

def test_login_to_facebook():
    with pytest.raises(Exception):
        project.login_to_facebook('test', 'test')
    assert project.login_to_facebook('test', 'test') == 'something went wrong with logging in'

def test_check_player_status():
    assert project.check_player_status() == 'checked'