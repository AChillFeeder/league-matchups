
import mysql.connector
from sqlalchemy import null

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="league_matchups"
)

global cursor
cursor = database.cursor()

class GamesDatabase:
    def __init__(self, id) -> None:
        self.id = id

    def addSummonerGame(self, data):
        cursor.execute("""INSERT INTO games (player-champion, lane-opponent, win) 
            VALUES ('{}','{}','{}','{}')""".format(
                data["player-champion"], data["lane-opponent"], data["win"], id
            ))

    def getAllSummonerGames(self):
        pass
    def getSummonerGamesByChampion(self):
        pass
    def getSummonerGamesByTag(self):
        pass

    def getAllGamesByChampion(self):
        pass
    def getAllGamesByTag(self):
        pass


class UsersDatabase:

    @staticmethod
    def checkCreditentials(username, password): # tested
        cursor.execute("SELECT password, id FROM users WHERE username='{}'".format(username))
        result = cursor.fetchone()

        if result:
            id = result[1] if result[0] == password else null
        else:
            id = null

        return id

    @staticmethod
    def getUserData(id):
        cursor.execute("SELECT * FROM users WHERE id='{}'".format(id))
        result = cursor.fetchone()

        organized_result = {
            "id": result[0],
            "username": result[1],
            "password": result[2],
            "summonerName": result[3],
            "popularity": result[4]
        } if result else None

        return organized_result

    @staticmethod
    def saveUser(data):
        cursor.execute("INSERT INTO users (username, password, summonerName, popularity) VALUES ('{}', '{}', '{}', '{}')".format(
            data["username"], data["password"], data["summonerName"], data["popularity"]
        ))
        database.commit()
        print(cursor.rowcount, "record inserted.")







