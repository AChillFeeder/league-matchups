import requests
import json

from . import Interface

# correct patches: https://ddragon.leagueoflegends.com/api/versions.json
# champion information: http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json
# community dragon: https://www.communitydragon.org/docs


class Game(Interface):
    
    def getPlayers(self):
        # Current game information
        self.current_players = self.get_all_players_current_game()
        self.team1 = dict(list(self.current_players.items())[:5])
        self.team2 = dict(list(self.current_players.items())[5:])
        self.opponents = self.team2 if self.summoner_name in list(self.team1.keys()) else self.team1
        self.player_champion = self.current_players[self.summoner_name]
        
    def getUsefulData(self) -> str:
        if self.in_game:
            return json.dumps({
                'summoner_name': self.summoner_name,
                'player_champion': self.player_champion,
                'enemy_champions': list(self.opponents.values()),
                'opponents': self.opponents,
            })
        else:
            return json.dumps({'error': 'summoner not in a game'})


    def GetSummonerIdFromName(self) -> list:
        """
            {
                "id": "ZIMHUx81SqvxNMZYZ9FKwUCmHD_2YyOnnDXVwHnY3uP8PqY",
                "accountId": "Xcq4VnTKWmg29AUULFKa3yDaFi9easUPl0PDpVKw3qhZ-5Q",
                "puuid": "wobtCDNmeldz7yWG88dNUEyMApT2jobRyNTw8pDpwgZsW-hEauP1SJedTQNxJ7PXwIjuBvB1MHHX9w",
                "name": "Okalu",
                "profileIconId": 1590,
                "revisionDate": 1618674262487,
                "summonerLevel": 270
            }
        """
        data = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key={self.api_key}'
        ).json()

        return data['id'], data['accountId'], data['puuid']
        

    def getChampionNameFromId(self): # move this to INIT
        # ddragon imposes strict request limits, so I tap into them once and save relevant data
        try:
            with open(f'champion_{self.patch}.json', 'r') as file:
                champions_data = json.load(file)
        except Exception:
            champions_data = requests.get(
                f'http://ddragon.leagueoflegends.com/cdn/{self.patch}/data/en_US/champion.json'
            ).json()["data"]
            with open(f'champion_{self.patch}.json', 'w') as file:
                json.dump(champions_data, file)

        return {champion["key"] : champion["id"].lower() for champion in champions_data.values()}


    def getAllPlayersCurrentGame(self) -> list:

        players_data = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{self.summoner_id}?api_key={self.api_key}'
        ).json()["participants"]

        player_name_to_champion = {player["summonerName"].lower() : self.champion_id_to_name[str(player["championId"])] for player in players_data}

        return player_name_to_champion
        

    


