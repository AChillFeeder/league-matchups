

import league_api
from account_management import Main
import json


class Account(Main):
    
    def __init__(self) -> None:
        super().__init__()

    def connect(self, request):
        data = request.json
        username = data['username']
        password = data['password']
        database = Main.usables.open_database()
        for player in database:
            if (
                database[player]["settings"]["username"] == username 
                and 
                database[player]["settings"]["password"] == hash(password)
            ):
                return json.dumps({'connected': True, 'summoner-name': player})
        
        return json.dumps({'connected': False, 'summoner-name': ''})

    def register(self, request):
        data = request.json
        username = data['username']
        password = data['password']
        summoner_name = data['summoner-name']

        database = Main.usables.open_database()

        # check if username is duplicate
        for summoner in database:
            if username == database[summoner]["settings"]["username"]:
                return json.dumps({'registered': False, 'message': 'duplicate username'})

        if summoner_name not in database: # check if summoner name is duplicate
            database[summoner_name] = {"games": [], "settings": {'username': username, 'password': hash(password)}}
            Main.usables.save_to_database(database)
            return json.dumps({'registered': True, 'message': 'success'})

        return json.dumps({'registered': False, 'message': 'duplicate summoner name'})