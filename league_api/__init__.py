
from league_api.game import Game
from league_api.usables import Usables
from league_api.assets import Assets



class Interface:
    
    def __init__(self, summonerName) -> None:
        self.summonerName = summonerName
        self.patch = "11.9.1" # should be found automatically
        self.summonerInGame = False
        self.summonerID = ""
        self.apiKey = ""
         

        self.game = Game()
        self.usables = Usables()
        self.assests = Assets()

    
    


