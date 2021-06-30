import requests
import json

from . import Interface

# correct patches: https://ddragon.leagueoflegends.com/api/versions.json
# champion information: http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json
# community dragon: https://www.communitydragon.org/docs


class Game(Interface):


    def __init__(self):
        super().__init__(self)
        
    
    def playersInCurrentGameData(self) -> list:
        # acquire summonerNames of all players in the current game
        playersInCurrentGameInformation = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{self.summonerID}?api_key={self.apiKey}'
        ).json()["participants"]

        playersSummonerNameAndChampionName = {
            player["summonerName"].lower() : self.champion_id_to_name[str(player["championId"])] for player in playersInCurrentGameInformation
            }

        return playersSummonerNameAndChampionName
        

    def playersInCurrentGameSorted(self):
        # Current game information
        self.allPlayersInCurrentGame = self.playersInCurrentGameData()

        self.firstTeam = dict(list(self.allPlayersInCurrentGame.items())[:5])
        self.secondTeam = dict(list(self.allPlayersInCurrentGame.items())[5:])
        
        self.summonerOpponents = self.secondTeam if self.summonerName in list(self.firstTeam.keys()) else self.firstTeam
        self.summonerChampionInCurrentGame = self.allPlayersInCurrentGame[self.summonerName]


    def mapOfCurrentGameData(self):
            pass


    def getPlayersInCurrentGameSorted(self):
        return json.dumps({
            'allPlayersInCurrentGame': self.allPlayersInCurrentGame,
            'firstTeam': self.firstTeam,
            'secondTeam': self.secondTeam,
            'summonerOpponents': self.summonerOpponents,
            'summonerChampionInCurrentGame': self.summonerChampionInCurrentGame,
            'summonerOpponentsChampions': list(self.summonerOpponents.values())
        })


    
    def getMapOfCurrentGameData(self):
        pass
        

    


    

    


