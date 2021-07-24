
from leagueMatchups.database import UsersDatabase

class User():
    def __init__(self) -> None:
        self.summonerName: str
        self.region: str

    def register(self, data):
        # data handling here

        # save user
        # sqlalchemy.exc.IntegrityError | duplicate exception
        UsersDatabase.saveUser({
            "username": data["username"],
            "password": data["password"],
            "summonerName": data["summonerName"],
        })

    def connect(self, data):
        pass

