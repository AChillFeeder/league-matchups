
from leagueMatchups.database import Game
from player import Player
from user import User
from database import GamesDatabase, UsersDatabase



# stays on __init__
class LeagueMatchups:

    def __init__(self) -> None:
        self.gamesDatabase = GamesDatabase()
        self.usersDatabase = UsersDatabase()
        self.user = User()

        self.summonerName: str
        self.player: Player

    def connect(self, data):
        connected, userData = self.user.connect(data)

        if connected:
            self.player = Player(userData["summonerName"]) # connected
        else:
            pass # not connected


    def register(self, data):
        self.user.register(data)






    






    



