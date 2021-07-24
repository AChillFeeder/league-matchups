from leagueMatchups import LeagueMatchups
from flask import Flask, request

from leagueMatchups import LeagueMatchups as LM

app = Flask(__name__)
LeagueMatchups = LM()

# @userSession check if user is connected

@app.route('/<summoner_name>/games-history', methods=['GET', 'POST'])
def gamesHistory(summoner_name): # shows previous games and allows to add new ones
    if request.method == 'POST':
        # add game to database
        pass
    
    elif request.method == 'GET':
        # get all games from database [number of games]
        pass



@app.route('/<summoner_name>/current-game', methods=["GET"])
def currentGame(summoner_name):
    # current game information
    pass


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    LeagueMatchups.register(data)

@app.route('/connect', methods=["POST"])
def connect():
    pass



if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)