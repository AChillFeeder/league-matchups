
from leagueMatchups.database import UsersDatabase

class User():

    def __init__(self) -> None:
        self.usersDatabase = UsersDatabase()   
        self.defaultPopularity = 0
    
    def register(self, username: str, password: str, summonerName: str) -> None:
        self.usersDatabase.saveUser(
            {
                "username": username,
                "password": password,
                "summonerName": summonerName,
                "popularity": self.defaultPopularity
            }
        )

    def connect(self, username: str, password: str) -> dict:
        user_id = self.usersDatabase.checkCreditentials(username, password)

        if user_id:
            player_data = self.usersDatabase.getUserData(user_id) # {}: id, username, password, summoner, popularity

        else:
            return None

        return player_data

    def change_popularity(self, id: int, popularity: int):
        self.usersDatabase.changePopularity(id, popularity)


