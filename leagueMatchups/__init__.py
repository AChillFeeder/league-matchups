
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
            # self.user.summonerName = userData.summonnerName
            self.user.summonerName = "max0"
            self.player = Player(self.user.summonerName, "NA") # connected
            self.gamesDatabase = GamesDatabase(self.user.summonerName)

            return True, userData

        else:
            return False, ""


    def register(self, data):
        self.user.register(data)


    def getCurrentGame(self):
        return self.player.getCurrentGame()




