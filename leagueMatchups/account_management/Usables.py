import json
import os

def openDatabase():
    with open(os.path.join('leagueMatchups', 'data', 'db.json'), 'r') as file:
        return json.loads(file.read()) 
    
def saveToDatabase(data):
    with open(os.path.join('leagueMatchups', 'data', 'db.json'), 'w') as file:
        json.dump(data, file)