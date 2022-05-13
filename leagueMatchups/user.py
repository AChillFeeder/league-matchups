
from django.db import IntegrityError
from leagueMatchups.database import UsersDatabase
import mysql

class User():

    def __init__(self) -> None:
        self.usersDatabase = UsersDatabase()   
        self.defaultPopularity = 0
    
    def register(self, username: str, password: str, summonerName: str) -> None:

        if not username or not password: # in case of empty username and password
            return 0
             
        try:
            self.usersDatabase.saveUser(
                {
                    "username": username,
                    "password": password,
                    "summonerName": summonerName,
                    "popularity": self.defaultPopularity
                }
            )
            return 1
        except mysql.connector.errors.IntegrityError:
            return 0

    def connect(self, username: str, password: str) -> dict:
        """
            "id": 26,
            "username": "nagakabouros",
            "summonerName": "a chill feeder",
            "popularity": 0
        """
        user_id = self.usersDatabase.checkCreditentials(username, password)

        if user_id:
            player_data = self.usersDatabase.getUserData(user_id) # {}: id, username, password, summoner, popularity

        else:
            return 0

        return player_data

    def change_popularity(self, id: int, popularity: int):
        self.usersDatabase.changePopularity(id, popularity)


