import cassiopeia
import cassiopeia_championgg
import os
from leagueMatchups.database import GamesDatabase

class Player():

    def __init__(self, summonerName: str, region: str) -> None:

        self.gamesDatabase = GamesDatabase()

        try:
            with open(os.path.join('leagueMatchups' ,'data', 'api_key.txt'), "r") as file:
                self.apiKey = file.read()
        except FileNotFoundError:
            raise Exception("Create an api_key.txt that holds your api key")

        self.summonerName = summonerName.lower()

        ##### TESTING ######
        self.summonerName = "Allorim".lower()
        self.region = region

        cassiopeia.set_riot_api_key(self.apiKey) 
        cassiopeia.set_default_region(self.region) 

        self.summoner = cassiopeia.Summoner(name=self.summonerName)
        print("summoner's name: ", self.summoner.name)

    def getCurrentGame(self):
        self.currentMatch = self.summoner.current_match.to_dict()
        summoner_champion, enemy_team_champions = self.sanitizeCurrentMatchData()

        result = {
            "summoner_champion": {
                "name": summoner_champion.name,
                "image": summoner_champion.image.url
            },
            "enemy_team_champions": []
        }

        for champion in enemy_team_champions:
            result['enemy_team_champions'].append(
                {
                    "name": champion.name,
                    "image": champion.image.url
                }
            )

        return result

    def sanitizeCurrentMatchData(self):
        all_participants = self.currentMatch['participants']
        summoner_participant = [participant for participant in all_participants if participant["summonerName"].lower() == self.summonerName][0]
        summoner_champion = cassiopeia.Champion(id=summoner_participant['championId'])

        # splitting the teams => team array has champion ID only, no other data
        team_one, team_two = self.teamsFromCurrentGame(all_participants)

        # defining the enemy team
        enemy_team_champions = team_one if summoner_participant['teamId'] == 200 else team_two

        return summoner_champion, enemy_team_champions
        
    @staticmethod
    def teamsFromCurrentGame(all_participants):
        team_one = [cassiopeia.Champion(id=participant['championId']) for participant in all_participants if participant['teamId']==100]
        team_two = [cassiopeia.Champion(id=participant['championId']) for participant in all_participants if participant['teamId']==200]

        return team_one, team_two

    def saveGame(self, playerChampion, laneOpponent, win, id):
        self.gamesDatabase.addSummonerGame(playerChampion, laneOpponent, win, id)

    def getAllSummonerGames(self, id):
        return self.gamesDatabase.getAllSummonerGames(id)