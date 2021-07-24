from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import ForeignKey

engine = create_engine('sqlite:///E:\\Projects\\league-matchups\\leagueMatchups\\data\\database.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class GamesDatabase:
    def __init__(self, summonerName) -> None:
        self.summonerName = summonerName

    def addSummonerGame(self):
        pass
    def getAllSummonnerGames(self):
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
    def checkCreditentials(self):
        pass

    @staticmethod
    def getUserData(username):
        pass

    @staticmethod
    def saveUser(data):
        user = User(
            username = data["username"],
            password = data["password"],
            summonerName = data["summonerName"],
            popularity = 0
        )
        session.add(user)
        session.commit()



class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    summoner_champion = Column(String)
    opponent_champion = Column(String)
    # noteContent = Column(ARRAY(String))
    # noteCategory = Column(ARRAY(String))
    popularity = Column(Integer)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String) # hash pepper yada yada
    summonerName = Column(String)
    popularity = Column(Integer)

    games = relationship(Game, backref="users")

Base.metadata.create_all(engine)


