from leagueMatchups import LeagueMatchups, user
from flask import Flask, request

from leagueMatchups import LeagueMatchups as LM

app = Flask(__name__)
LeagueMatchups = LM()

# @userSession check if user is connected

@app.route('/games-history', methods=['GET', 'POST'])
def gamesHistory(summoner_name): # shows previous games and allows to add new ones
    if request.method == 'POST':
        # add game to database
        pass
    
    elif request.method == 'GET':
        # get all games from database [number of games]
        pass


@app.route('/register', methods=['POST'])
def register():
    data = request.json # username, password, summonerName
    LeagueMatchups.register(data)
    

@app.route('/connect', methods=["POST"])
def connect():
    data = request.json # username, password
    connected, userData = LeagueMatchups.connect(data)
    return str(userData.id)


@app.route('/current-game', methods=["POST", "GET"])
def currentGame():
    if request.method == "GET":
        currentGame = LeagueMatchups.getCurrentGame()
        return currentGame # currentMatch, opponents, teammates, summonerInGame


if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)