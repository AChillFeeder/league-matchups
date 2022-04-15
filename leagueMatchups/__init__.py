
from leagueMatchups.player import Player
from leagueMatchups.user import User

# from leagueMatchups.database import GamesDatabase, UsersDatabase



# stays on __init__
class LeagueMatchups:

    def __init__(self) -> None:
        self.user = User()

    def initializePlayer(self, summonerName, region="NA"):
        self.player = Player(summonerName, region)


