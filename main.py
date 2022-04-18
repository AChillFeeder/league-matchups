from flask import Flask, request, session
from flask_cors import CORS
import json
import secrets

from leagueMatchups import LeagueMatchups
from leagueMatchups import LeagueMatchups as LM



app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app)
LeagueMatchups = LM()

# USER AND SESSION MANAGEMENT

@app.route('/register', methods=['POST'])
def register(): #
    form_data = request.json # username, password, summonerName
    LeagueMatchups.user.register(form_data['username'], form_data['password'], form_data['summonerName'])
    
@app.route('/connect', methods=["POST"])
def connect(): #
    form_data = request.json # username, password
    userData = LeagueMatchups.user.connect(form_data['username'], form_data['password'])
    LeagueMatchups.initializePlayer(userData["summonerName"])
    session['userID'] = userData["id"]
    return json.dumps(userData)

@app.route('/getSession', methods=["GET"])
def getSession() -> str: # 
    # maybe return summoner_name too
    """Returns the ID of the currect User"""
    if 'userID' in session:
        return str(session['userID'])
    else:
        return 0

@app.route('/logout', methods=["GET"])
def logout(): #
    try:
        session.pop('userID')
        return "Logged out"
    except KeyError:
        return "No user is connected"

# # # # # # # # # # # # # # # # # # # #




@app.route('/gamesHistory', methods=['GET', 'POST'])
def gamesHistory(): # 
    """shows previous games and allows to add new ones"""

    # ADD GAME TO DATABASE
    if request.method == 'POST': #
        form_data = request.json #playerChampion:int [ID], laneOpponent:int [ID], win:int [0/1], notes
        id = getSession()
        gameID = LeagueMatchups.player.saveGame(form_data["playerChampion"], form_data["laneOpponent"], form_data["win"], id)
        LeagueMatchups.player.saveNotes(form_data["notes"], int(getSession()), gameID)
        return "Done"
    
    # GET ALL GAMES FROM DATABASE - add number of games fetched option
    elif request.method == 'GET': #
        id = getSession()
        allSummonerGames = LeagueMatchups.player.getAllSummonerGames(id)
        allUserNotes = LeagueMatchups.player.getNotesByUserID(id)
        return json.dumps([allSummonerGames, allUserNotes])

@app.route('/currentGame', methods=["POST", "GET"])
def currentGame(): #
    if request.method == "GET":
        result = LeagueMatchups.player.getCurrentGame()
        return result

@app.route('/getNotesByGame/<gameID>')
def getNotesByGameId(gameID) -> json:
    result = LeagueMatchups.player.getNotesByGameID(int(gameID))
    return json.dumps(result)

@app.route('/deleteNote/<noteID>')
def deleteNote():
    pass #noteID

@app.route('/getChampionAbilities')
def getChampionAbilities():
    pass

@app.route('/set_riot_api_key', methods=["POST"])
def set_riot_api_key():
    pass









if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)