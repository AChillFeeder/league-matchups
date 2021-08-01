
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
            self.player = Player(userData.summonerName, "na1") # connected
            self.gamesDatabase = GamesDatabase(userData.summonerName)

            return 1, userData

        else:
            return 0, ""


    def register(self, data):
        self.user.register(data)


    def getCurrentGame(self):
        return self.player.getCurrentGame()



# class Game():
#             def __init__(self, other) -> None:
#                 self.summoner = other.summoner
#                 self.current_match = other.currentMatch

#                 self.summonerChampion = self.summoner.current_match.champion
#                 self.opponents, self.teammates = self.setOpponentsAndTeammates()

#             def setOpponentsAndTeammates(self):
#                 self.blueTeam = self.current_match.blue_team 
#                 self.redTeam = self.current_match.red_team

#                 self.opponents, self.teammates = self.blueTeam, self.redTeam if self.summoner not in self.blueTeam.participants else self.redTeam, self.blueTeam

#         return Game(self)


    






    



