
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
            "popularity": 0, 
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


class TestGamesDatabase(unittest.TestCase):
    def test_addSummonerGame(self):
        data = {
            "player-champion-test",
            "lane-opponent-test",
            "win"
        }
        GamesDatabase.addSummonerGame(data)


if __name__ == '__main__':
    unittest.main()
