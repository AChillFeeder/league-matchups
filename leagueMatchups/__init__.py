
from leagueMatchups.player import Player
from leagueMatchups.user import User
from leagueMatchups.database import GamesDatabase, UsersDatabase



# stays on __init__
class LeagueMatchups:

    def __init__(self) -> None:
        self.usersDatabase = UsersDatabase()
        self.user = User()

        self.summonerName: str
        self.player: Player

    def connect(self, data):
        connected, userData = self.user.connect(data)

        if connected:
            self.player = Player(userData["summonerName"]) # connected
            self.gamesDatabase = GamesDatabase(userData["summonerName"])

        else:
            pass # not connected


    def register(self, data):
        self.user.register(data)






    






    



