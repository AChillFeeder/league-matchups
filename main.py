from flask import Flask, request
from flask_cors import CORS
import json
import secrets

from leagueMatchups import LeagueMatchups, player
from leagueMatchups import LeagueMatchups as LM
import leagueMatchups



app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = secrets.token_hex(16)
LeagueMatchups = LM()



def flash_message(success=True, message=""):
    return json.dumps({
        "success": success,
        "message": message
        })

# USER AND SESSION MANAGEMENT

@app.route('/register', methods=['POST'])
def register(): #
    form_data = request.json # username, password, summonerName
    success = LeagueMatchups.user.register(form_data['username'], form_data['password'], form_data['summonerName'])
    if success:
        return flash_message(
            success = True,
            message = "Account created successfully"
        )
    else:
        return flash_message(
            success = False,
            message = "Username already exists"
        )

@app.route('/connect', methods=["POST"])
def connect(): #
    form_data = request.json # username, password

    userData = LeagueMatchups.user.connect(form_data['username'], form_data['password'])
    if userData:
        LeagueMatchups.initializePlayer(userData["summonerName"])
        LeagueMatchups.player.id = userData["id"]
        return flash_message(
            success= True,
            message= userData
        )
        # return json.dumps(userData)

    return flash_message(
        success = False,
        message = "Bad username or password"
    )




@app.route('/getSession', methods=["GET"])
def getSession() -> dict: # 
    # maybe return summoner_name too
    """Returns the ID of the currect User"""
    id = LeagueMatchups.player.id
    if id:
        return flash_message(success=True, message=id)
    else: # attribute error
        return flash_message(success=False, message="No session")

@app.route('/logout', methods=["GET"])
def logout(): #
    LeagueMatchups.player.id = 0
    return flash_message(success=True, message="user logged out")

# # # # # # # # # # # # # # # # # # # #




@app.route('/gamesHistory', methods=['GET', 'POST'])
def gamesHistory(): # 
    """shows previous games and allows to add new ones"""

    # ADD GAME TO DATABASE
    if request.method == 'POST': #
        form_data = request.json #playerChampion:int [ID], laneOpponent:int [ID], win:int [0/1], gameCreation and gameID, notes
        print(form_data)
        id = int(json.loads(getSession())["message"])
        gameID = LeagueMatchups.player.saveGame(
            form_data["playerChampion"], 
            form_data["laneOpponentChampion"], 
            form_data["laneOpponentSummonerID"], 
            form_data["laneOpponentSummonerName"], 
            form_data["win"], 
            id, 
            form_data["gameCreation"], 
            form_data["gameID"],
            form_data["summonerName"],
            form_data["summonerID"],
        )

        LeagueMatchups.player.saveNotes(form_data["notes"], int(id), gameID)
        return "Done"
    
    # GET ALL GAMES FROM DATABASE - add number of games fetched option
    elif request.method == 'GET': #
        id = int(json.loads(getSession())["message"])
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

@app.route('/set_riot_api_key', methods=["POST"])
def set_riot_api_key():
    pass

@app.route('/gameInformation/<gameID>')
def gameInformation(gameID):
    # playerChampion, opponentChampion = champions.split(";")
    return LeagueMatchups.player.getMatchInformation(gameID) #, playerChampion, opponentChampion)



if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)