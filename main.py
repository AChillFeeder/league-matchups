from flask import Flask, request
from flask_cors import CORS
import json
import league_api


app = Flask(__name__)
CORS(app)




@app.route('/connect', methods=["POST"])
def connect():
    data = request.json

@app.route('/register', methods=['POST'])
def register():
    pass

@app.route('/<summoner_name>/games', methods=['GET', 'POST'])
def playerGamesHistory(summoner_name):
    
    if request.method == 'POST':
        formValues = request.json


        


    try:
        return league_api.usables.openDatabase()[summoner_name]
    except KeyError:
        return json.dumps({'status': False, 'message': 'user not registered'})
    
@app.route('/<summoner_name>/current-game', methods=["GET"])
def currentGame(summoner_name):
    pass



if __name__ == '__main__':
    app.run('0.0.0.0', 8000, True)