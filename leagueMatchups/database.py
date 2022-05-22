
import mysql.connector
from sqlalchemy import null

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="league_matchups"
)



class GamesDatabase:
    def __init__(self) -> None:
        self.cursor = database.cursor(buffered=True)

    def addSummonerGame(self, playerChampion: str, laneOpponent: str, win: int, id: int, gameCreation: int, gameID: int): # update test
        """Win takes 1 or 0"""
        self.cursor.execute("""INSERT INTO games (playerChampion, laneOpponent, win, userID, gameCreation, gameID) VALUES ('{}','{}',{},{},{},{})""".format(
                playerChampion, laneOpponent, win, id, gameCreation, gameID
            ))
        database.commit()
        return self.cursor.lastrowid

    def getAllSummonerGames(self, id: int):
        self.cursor.execute("SELECT * FROM games WHERE userID='{}'".format(id))
        result = self.cursor.fetchall()
        return result

    def getAllSummonerGamesByChampion(self, playerChampion: str, id: int):
        self.cursor.execute("SELECT * FROM games WHERE userID='{}' AND playerChampion='{}'".format(id, playerChampion))
        result = self.cursor.fetchall()
        return result

    def getAllSummonerGamesByOpponentChampion(self, laneOpponentChampion: str, id: int):
        self.cursor.execute("SELECT * FROM games WHERE userID='{}' AND laneOpponent='{}'".format(id, laneOpponentChampion))
        result = self.cursor.fetchall()
        return result

    def getAllSummonerGamesByMatchup(self, playerChampion: str, laneOpponentChampion: str, id: int):
        self.cursor.execute("SELECT * FROM games WHERE userID='{}' AND playerChampion='{}' AND laneOpponent='{}'".format(id, playerChampion, laneOpponentChampion))
        result = self.cursor.fetchall()
        return result

    # @staticmethod
    def getAllGamesByChampion(self, champion):
        self.cursor.execute("SELECT * FROM games WHERE laneOpponent='{0}' OR playerChampion='{0}'".format(champion))
        result = self.cursor.fetchall()
        return result
    
    def getAllSummonerGamesByTag(self):
        pass

    @staticmethod
    def getAllGamesByTag(tag):
        pass

class UsersDatabase:

    def __init__(self) -> None:
        self.cursor = database.cursor(buffered=True)

    # @staticmethod
    def checkCreditentials(self, username: str, password: str):
        """Checks the validity of user creditentials
        => userID if correct
        => Null if incorrect
        """ 
        self.cursor.execute("SELECT password, id FROM users WHERE username='{}'".format(username))
        result = self.cursor.fetchone()

        if result:
            id = result[1] if result[0] == password else null
        else:
            id = null

        return id

    # @staticmethod
    def getUserData(self, id: int):
        """
            Get user's data from the database
            => {
                id: int,
                username: str,
                summonerName: str,
                popularity: int
            }
        """
        self.cursor.execute("SELECT * FROM users WHERE id='{}'".format(id))
        result = self.cursor.fetchone()

        organized_result = {
            "id": result[0],
            "username": result[1],
            # "password": result[2],
            "summonerName": result[3],
            "popularity": result[4]
        } if result else None

        return organized_result

    # @staticmethod
    def saveUser(self, data: dict):
        """
            Saves the user in the database
            {username:str, password:str, summonerName:str} =>
        """
        self.cursor.execute("INSERT INTO users (username, password, summonerName, popularity) VALUES ('{}', '{}', '{}', '{}')".format(
            data["username"], data["password"], data["summonerName"], data["popularity"]
        ))
        database.commit()

    # @staticmethod
    def changePopularity(self, id: int, popularity: int):
        """
            Change the user popularity
        """
        self.cursor.execute("UPDATE users SET popularity={} WHERE id={}".format(popularity, id))
        database.commit()
        print(self.cursor.rowcount, "record(s) affected.")


class NotesDatabase:
    
    def __init__(self) -> None:
        self.cursor = database.cursor(buffered=True)

    # @staticmethod
    def addNote(self, noteContent, userID, gameID):
        self.cursor.execute("INSERT INTO notes (noteContent, gameID, userID) VALUES ('{}', {}, {})".format(noteContent, gameID, userID))
        database.commit() # might have to delete '' for integers
            
    # @staticmethod
    def getNotesByUser(self, userID) -> list:
        self.cursor.execute("SELECT * FROM notes WHERE userID={}".format(userID))
        result = self.cursor.fetchall()
        return result

    # @staticmethod
    def getNotesByGame(self, gameID):
        self.cursor.execute("SELECT * FROM notes WHERE gameID={}".format(gameID))
        result = self.cursor.fetchall()
        return result

class tags:
    pass


