
from leagueMatchups import LeagueMatchups

class User(LeagueMatchups):
    def __init__(self) -> None:
        self.summonerName: str = None
        self.region: str = "na1"

    def register(self, data):
        username, password = data

    def connect(self, data):
        pass

