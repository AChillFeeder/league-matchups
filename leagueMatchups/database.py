
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
    def __init__(self) -> None:
        pass

    def addSummonerGame(self, playerChampion: str, laneOpponent: str, win: int, id: int): # update test
        """Win takes 1 or 0"""
        cursor.execute("""INSERT INTO games (playerChampion, laneOpponent, win, userID) VALUES ('{}','{}','{}','{}')""".format(
                playerChampion, laneOpponent, win, id
            ))

    def getAllSummonerGames(self, id: int):
        cursor.execute("SELECT * FROM games WHERE userID='{}'".format(id))
        result = cursor.fetchall()
        return result

    def getAllSummonerGamesByChampion(self, playerChampion: str, id: int):
        cursor.execute("SELECT * FROM games WHERE userID='{}' AND playerChampion='{}'".format(id, playerChampion))
        result = cursor.fetchall()
        return result

    def getAllSummonerGamesByOpponentChampion(self, laneOpponentChampion: str, id: int):
        cursor.execute("SELECT * FROM games WHERE userID='{}' AND laneOpponent='{}'".format(id, laneOpponentChampion))
        result = cursor.fetchall()
        return result

    def getAllSummonerGamesByMatchup(self, playerChampion: str, laneOpponentChampion: str, id: int):
        cursor.execute("SELECT * FROM games WHERE userID='{}' AND playerChampion='{}' AND laneOpponent='{}'".format(id, playerChampion, laneOpponentChampion))
        result = cursor.fetchall()
        return result

    @staticmethod
    def getAllGamesByChampion(champion):
        cursor.execute("SELECT * FROM games WHERE laneOpponent='{0}' OR playerChampion='{0}'".format(champion))
        result = cursor.fetchall()
        return result
    
    def getAllSummonerGamesByTag(self):
        pass

    @staticmethod
    def getAllGamesByTag(tag):
        pass

class UsersDatabase:

    @staticmethod
    def checkCreditentials(username: str, password: str):
        """Checks the validity of user creditentials
        => userID if correct
        => Null if incorrect
        """ 
        cursor.execute("SELECT password, id FROM users WHERE username='{}'".format(username))
        result = cursor.fetchone()

        if result:
            id = result[1] if result[0] == password else null
        else:
            id = null

        return id

    @staticmethod
    def getUserData(id: int):
        """
            Get user's data from the database
            => {
                id: int,
                username: str,
                summonerName: str,
                popularity: int
            }
        """
        cursor.execute("SELECT * FROM users WHERE id='{}'".format(id))
        result = cursor.fetchone()

        organized_result = {
            "id": result[0],
            "username": result[1],
            # "password": result[2],
            "summonerName": result[3],
            "popularity": result[4]
        } if result else None

        return organized_result

    @staticmethod
    def saveUser(data: dict):
        """
            Saves the user in the database
            {username:str, password:str, summonerName:str} =>
        """
        cursor.execute("INSERT INTO users (username, password, summonerName, popularity) VALUES ('{}', '{}', '{}', '{}')".format(
            data["username"], data["password"], data["summonerName"], data["popularity"]
        ))
        database.commit()

    @staticmethod
    def changePopularity(id: int, popularity: int):
        """
            Change the user popularity
        """
        cursor.execute("UPDATE users SET popularity={} WHERE id={}".format(popularity, id))
        database.commit()
        print(cursor.rowcount, "record(s) affected.")

class NotesDatabase:

    def addNote(noteContent, userID, gameID):
        cursor.execute("INSERT INTO notes (noteContent, gameID, userID) VALUES ('{}', '{}', '{}')".format(noteContent, userID, gameID))
        database.commit()
            
    def getNotesByUser(userID):
        cursor.execute("SELECT * FROM notes WHERE userID='{}'".format(userID))
        result = cursor.fetchall()
        return result

    def getNotesByGame(gameID):
        cursor.execute("SELECT * FROM notes WHERE gameID='{}'".format(gameID))
        result = cursor.fetchall()
        return result

class tags:
    pass


