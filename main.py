from leagueMatchups import LeagueMatchups, user
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from leagueMatchups import LeagueMatchups as LM

app = Flask(__name__)
CORS(app)
LeagueMatchups = LM()

# @userSession check if user is connected


@app.route('/register', methods=['POST'])
def register():
    form_data = request.json # username, password, summonerName
    LeagueMatchups.user.register(form_data['username'], form_data['password'], form_data['summonerName'])
    


@app.route('/connect', methods=["POST"])
def connect():
    form_data = request.json # username, password
    userData = LeagueMatchups.user.connect(form_data['username'], form_data['password'])
    LeagueMatchups.initializePlayer(userData["summonerName"])
    return json.dumps(userData)



@app.route('/getSession')
def getSession():
    """Returns the ID of the currect User"""
    return 26 # temporary


@app.route('/gamesHistory', methods=['GET', 'POST'])
def gamesHistory(): # shows previous games and allows to add new ones
    if request.method == 'POST':
        # add game to database
        form_data = request.json #playerChampion, laneOpponent, win
        id = getSession()
        LeagueMatchups.player.saveGame(form_data["playerChampion"], form_data["laneOpponent"], form_data["win"], id)
        return True #
    
    elif request.method == 'GET':
        # get all games from database [number of games]
        id = getSession()
        allSummonerGames = LeagueMatchups.player.getAllSummonerGames(id)
        return json.dumps(allSummonerGames)


@app.route('/currentGame', methods=["POST", "GET"])
def currentGame():
    if request.method == "GET":
        currentGame = LeagueMatchups.getCurrentGame()
        return currentGame["currentMatch"] #  opponents, teammates, summonerInGame


@app.route('/set_riot_api_key', methods=["POST"])
def set_riot_api_key():
    pass

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)