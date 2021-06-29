
from league_api.game import Game
from league_api.player import Player
from league_api.assets import Assets

class Interface:

    def __init__(self, username) -> None:
        self.username = username
        self.patch = ""

    game = Game()
    player = Player()
    assests = Assets()

    


