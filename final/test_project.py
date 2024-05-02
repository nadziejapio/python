import pytest
import requests_mock
import project

def test_load_player():
    with requests_mock.Mocker() as m:
        m.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/test/test', json={'puuid': 'test_puuid'})
        project.load_player('test#test')
        assert len(project.players) == 1
        assert project.players[0].id == 'test_puuid'

def test_check_player_status():
    with requests_mock.Mocker() as m:
        m.get('https://eun1.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/test_puuid', json={'gameId': 'test_gameId'})
        player = project.player('test#test', 'test_puuid')
        project.players.append(player)
        project.check_player_status()
        assert project.players[0].current_game == 'test_gameId'

def test_get_info():
    with requests_mock.Mocker() as m:
        m.get('https://europe.api.riotgames.com/lol/match/v5/matches/test_gameId', json={
            'info': {
                'participants': [
                    {
                        'summonerId': 'test_puuid',
                        'championName': 'test_champion',
                        'kills': 10,
                        'deaths': 2,
                        'assists': 8,
                        'win': True
                    }
                ]
            },

        })
        m.get('https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/test_puuid', json=[
            {'queueType': 'RANKED_SOLO_5x5',
            'tier': 'test_tier',
            'rank': 'test_rank',
            'leaguePoints': 90
        }])
        player = project.player('test#test', 'test_puuid')
        project.players.append(player)
        project.get_info('test_puuid', 'test#test', 'test_gameId')
        assert project.players[0].current_game == 'justEnded'
