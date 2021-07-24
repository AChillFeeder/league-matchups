from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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

    def getUserData(self):
        pass

    def saveUser(self):
        pass



class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    summoner_champion = Column(String)
    opponent_champion = Column(String)
    notes = Column(ARRAY(String))
    tags = Column(ARRAY(String))
    popularity = Column(Integer)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String) # hash pepper yada yada
    name = Column(String)
    popularity = Column(Integer)
