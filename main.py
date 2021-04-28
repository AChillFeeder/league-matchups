from flask import Flask, request
from flask_cors import CORS
import json
from league_api import Summoner


app = Flask(__name__)
CORS(app)

def open_database():
    with open('data/db.json', 'r') as file:
        return json.loads(file.read()) 
    
def save_to_database(data):
    with open('data/db.json', 'w') as file:
        json.dump(data, file)



@app.route('/<summoner_name>/games', methods=['GET', 'POST'])
def player(summoner_name):
    """
        Contains a list of all games played by 'summoner-name'
        go through the games and filter those whom ID is in the player games array
    """
    if request.method == 'POST':
        # add the game to DB
        database = open_database() # get previous content

        content = request.json # get form values
        
        # if the player already has other games
        # generate an ID by incrementing last game's ID
        # otherwise it's 1
        content["id"] = database[summoner_name]["games"][-1]['id'] + 1 if database[summoner_name]["games"] else 1

        database[summoner_name]['games'].append(content) # add new data to the database
        
        save_to_database(database) # update the database

        return json.dumps({'saved': True, 'message': 'game saved successfully'})


    try:
        return open_database()[summoner_name]
    except KeyError:
        return json.dumps({'status': False, 'message': 'user not registered'})


        
@app.route('/<summoner_name>/current-game', methods=["GET"])
def new_game(summoner_name):
    try:
        Game = Summoner(summoner_name)
        return f"{Game.useful_data()}"
    except Exception as exc:
        return {"error": "Player isn't in a game or API key expired - Error code: " + str(exc)}



@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    summoner_name = data['summoner-name']

    database = open_database()

    # check if username is duplicate
    for summoner in database:
        if username == database[summoner]["settings"]["username"]:
            return json.dumps({'registered': False, 'message': 'duplicate username'})

    if summoner_name not in database: # check if summoner name is duplicate
        database[summoner_name] = {"games": [], "settings": {'username': username, 'password': password}}
        save_to_database(database)
        return json.dumps({'registered': True, 'message': 'success'})

    return json.dumps({'registered': False, 'message': 'duplicate summoner name'})

@app.route('/connect', methods=["POST"])
def connect():
    data = request.json
    username = data['username']
    password = data['password']
    database = open_database()
    for player in database:
        if database[player]["settings"]["username"] == username and database[player]["settings"]["password"] == password:
            return json.dumps({'connected': True, 'summoner-name': player})
    
    return json.dumps({'connected': False, 'summoner-name': ''})

app.run('0.0.0.0', 8000, True)

