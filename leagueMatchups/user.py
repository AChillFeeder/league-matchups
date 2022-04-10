
from leagueMatchups.database import UsersDatabase

class User():

    def __init__(self) -> None:
        self.usersDatabase = UsersDatabase()   
        self.defaultPopularity = 0
    
    def register(self, username, password, summonerName):
        self.usersDatabase.saveUser(
            {
                "username": username,
                "password": password,
                "summonerName": summonerName,
                "popularity": self.defaultPopularity
            }
        )

    def connect(self, username, password):
        user_id = self.usersDatabase.checkCreditentials(username, password)

