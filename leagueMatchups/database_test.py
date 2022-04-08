
import unittest
from database import GamesDatabase, UsersDatabase
import database

userDatabase = UsersDatabase()
gameDatabase = GamesDatabase(1)

class TestUsersDatabase(unittest.TestCase):
    def test_checkCreditentials(self):
        username = "test_username"
        password = "test_password"
        # correct combination
        self.assertEqual(userDatabase.checkCreditentials(username, password), 1)

        # testing wrong combinations
        self.assertNotEqual(userDatabase.checkCreditentials(username, password), 2)
        self.assertNotEqual(userDatabase.checkCreditentials(username, "wrong_password"), 1)
        self.assertNotEqual(userDatabase.checkCreditentials("wrong_username", password), 1)

    def test_getUserData(self):
        self.assertEqual(userDatabase.getUserData(1), {
            "id": 1,
            "username": "test_username",
            "password": "test_password",
            "summonerName": "test_summonerName",
            "popularity": 5, 
        })

    def test_saveUser(self):
        data = {
            "username": "test_saveUser_username",
            "password": "test_saveUser_password",
            "summonerName": "test_saveUser_summonerName",
            "popularity": 0, 
        }
        userDatabase.saveUser(data)
        database.cursor.execute("SELECT * FROM users where username='{}'".format(data["username"]))
        result=database.cursor.fetchone()

        self.assertEqual(result[2], "test_saveUser_password")

    def test_changePopularity(self):
        userDatabase.changePopularity(1, 5)


class TestGamesDatabase(unittest.TestCase):
    def test_addSummonerGame(self):
        data = {
            "playerChampion": "test_summoner_champion",
            "laneOpponent": "test_opponent_champion",
            "win": 1
        }
        gameDatabase.addSummonerGame(data)

        database.cursor.execute("SELECT laneOpponent FROM GAMES where playerChampion='test_summoner_champion'")
        result = database.cursor.fetchall()
        self.assertEqual(result[0][0], "test_opponent_champion")


    def test_getAllSummonerGames(self):
        allSummonerGames = gameDatabase.getAllSummonerGames()
        self.assertTrue((2, 'test_summoner_champion', 'test_opponent_champion', 1, 1) in allSummonerGames)
        
    def test_getAllGamesByChampion(self):
        allGamesbyChampion = gameDatabase.getAllGamesByChampion("test_summoner_champion")
        self.assertTrue(len(allGamesbyChampion)>0)

    def test_getAllSummonerGamesByOpponentChampion(self):
        allSummonerGamesByOpponentChampion = gameDatabase.getAllSummonerGamesByOpponentChampion("test_opponent_champion")
        self.assertTrue(len(allSummonerGamesByOpponentChampion)>0)

    def test_getAllSummonerGamesByMatchup(self):
        allSummonerGamesByMatchup = gameDatabase.getAllSummonerGamesByMatchup("test_summoner_champion" , "test_opponent_champion")
        self.assertTrue(len(allSummonerGamesByMatchup)>0)

    def test_getAllGamesByChampion(self):
        allGamesByChampion = gameDatabase.getAllGamesByChampion("test_summoner_champion")
        self.assertTrue(len(allGamesByChampion)>0)

if __name__ == '__main__':
    unittest.main()
