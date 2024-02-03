import time
import config
import requests
import plyer
class player:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.current_game = None

headers = {'X-Riot-Token': config.RIOT_API_KEY}

def get_nicknames():
    is_ended = False
    nicks = []
    while is_ended == False:
        nicks.append(input('Enter nickname: '))
        is_last = False
        while is_last == False:
            check = input('Do you want to add more?(y/n) ')
            if check == 'y':
                is_last = True
            elif check == 'n':
                print(nicks)
                return nicks

players = []

def load_player(players_Name):
    url = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{players_Name}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        players.append(player(players_Name, response.json()['id']))
        return None
    else:
        raise Exception('Something is wrong')

def check_player_status():
    for p in players:
        if p.current_game == 'justEnded':
            p.current_game = None
            continue
        url = f'https://eun1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{p.id}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            if p.current_game == None:
                plyer.notification.notify(title='LoL', message=f'{p.name} is playing {p.current_game}', app_name='Lol_Checker')
            p.current_game = response.json()['gameId']
        elif response.status_code == 404:
            if p.current_game != None:
                get_info(p.id, p.name, p.current_game)
                p.current_game = None
    return 'checked'

def get_info(playerId, playerName, gameId):
    url = f'https://europe.api.riotgames.com/lol/match/v5/matches/EUN1_{gameId}'
    response = requests.get(url, headers=headers)
    r2 = requests.get(f'https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{playerId}', headers=headers)
    for i in r2.json():
        if i['queueType'] == 'RANKED_SOLO_5x5':
            tier = i['tier']
            rank = i['rank']
            lp = i['leaguePoints']
    print(response)
    if response.status_code == 200:
        for p in response.json()['info']['participants']:
            if p['summonerId'] == playerId:
                champ = p['championName']
                k = p['kills']
                d = p['deaths']
                a = p['assists']
                if p['win'] == True:
                    send_facebook_message(f'Gratulacje {playerName} ({tier} {rank} - {lp}LP)! Dobra robota :) {k}/{d}/{a} - {champ}')
                    print('win msg sent')
                elif p['win'] == False:
                    send_facebook_message(f'{playerName}, następnym razem Ci się uda!')
                    print('lost msg sent')
                for p in players:
                    if p.id == playerId:
                        p.current_game = 'justEnded'
                        break
                return
            else:
                print('something is not working')
    else:
        time.sleep(30)
        get_info(playerId, playerName, gameId)

def main():
    nicks = get_nicknames()
    for n in nicks:
        load_player(n)
    while True:
        check_player_status()
        time.sleep(5)

if __name__ == '__main__':
    main()
