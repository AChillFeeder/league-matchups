import requests
import json

# correct patches: https://ddragon.leagueoflegends.com/api/versions.json
# champion information: http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json
# community dragon: https://www.communitydragon.org/docs


class Summoner:
    def __init__(self, summoner_name, region='na1') -> None:
        # General information
        
        self.apiKey = self.getApiKey()

        self.summoner_name = summoner_name.lower()
        self.region = region
        self.in_game = True
        self.patch = self.getPatch()

        
        # Current game information
        self.current_players = self.get_all_players_current_game()
        self.team1 = dict(list(self.current_players.items())[:5])
        self.team2 = dict(list(self.current_players.items())[5:])
        self.opponents = self.team2 if self.summoner_name in list(self.team1.keys()) else self.team1
        self.player_champion = self.current_players[self.summoner_name]
        
    def getApiKey():
        pass

    def getPatch():
        pass

    def useful_data(self) -> str:
        if self.in_game:
            return json.dumps({
                'summoner_name': self.summoner_name,
                'player_champion': self.player_champion,
                'enemy_champions': list(self.opponents.values()),
                'opponents': self.opponents,
            })
        else:
            return json.dumps({'error': 'summoner not in a game'})


    def get_summoner_id_from_name(self) -> list:
        data = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key={self.api_key}'
        ).json()

        return data['id'], data['accountId'], data['puuid']
        


    def get_champion_name_from_id(self):
        # ddragon imposes strict request limits, so I tap on them once and save relevant data
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


    def get_all_players_current_game(self) -> list:
        
        players_data = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{self.summoner_id}?api_key={self.api_key}'
        ).json()["participants"]

        player_name_to_champion = {player["summonerName"].lower() : self.champion_id_to_name[str(player["championId"])] for player in players_data}

        return player_name_to_champion
        

    


