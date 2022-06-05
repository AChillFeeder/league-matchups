
from leagueMatchups.player import Player
from leagueMatchups.user import User


# stays on __init__
class LeagueMatchups:

    def __init__(self) -> None:
        self.user = User()

    def initializePlayer(self, summonerName, region="EUW"):
        self.player = Player(summonerName, region)


