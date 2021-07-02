
from leagueMatchups import LeagueMatchups

from league_api.Game import Game
from league_api.Usables import Usables
from league_api.Assets import Assets



class Main(LeagueMatchups):
    
    def __init__(self, region="na") -> None:

        super().__init__()

        self.region = region
        
        self.patch = "11.9.1" # should be found automatically

        self.summonerIsInGame = False
        self.summonerID: str
        self.apiKey: str
         
        self.game = Game()
        self.usables = Usables()
        self.assests = Assets()

    
    


