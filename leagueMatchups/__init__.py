
from typing import List
import cassiopeia 


# stays on __init__
class LeagueMatchups:

    def __init__(self) -> None:
        self.session = {"connected": False, "summonerName": "ashric", "region": "na"} 

    


# moves to player
class Player(LeagueMatchups):

    def __init__(self) -> None:
        super().__init__()

        # function that sets API key here
        self.apiKey = "RGAPI-24ecbda9-0cbe-452c-939b-3a1064571d64" # TEMPORARY API KEY, DONT BOTHER
        self.region = self.session["region"]

        cassiopeia.set_riot_api_key(self.apiKey)
        cassiopeia.set_default_region(self.region)

        self.summoner = cassiopeia.get_summoner(name=self.session["summonerName"])


    def getCurrentGame(self):
        class Game(Player):
            def __init__(self) -> None:
                super().__init__()
                self.current_match = self.summoner.current_match
                print("champion: ", self.summoner.current_match.champion)
                self.opponents, self.teammates

            def setOpponentsAndTeammates(self):
                self.blueTeam = self.current_match.blue_team 
                self.redTeam = self.current_match.red_team

                self.opponents, self.teammates = self.blueTeam, self.redTeam if self.summoner not in self.blueTeam.participants else self.redTeam, self.blueTeam

        return Game().setOpponentsAndTeammates()


    






    



