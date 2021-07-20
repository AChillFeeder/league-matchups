import cassiopeia

class Player():

    def __init__(self, summonerName, region) -> None:

        self.apiKey = "RGAPI-24ecbda9-0cbe-452c-939b-3a1064571d64" # TEMPORARY API KEY, DONT BOTHER
        self.summonerName = summonerName
        self.region = region

        cassiopeia.set_riot_api_key(self.apiKey) #
        cassiopeia.set_default_region(self.region) #

        self.summoner = cassiopeia.get_summoner(name=self.summonerName)


    def getCurrentGame(self):
        class Game(Player):
            def __init__(self) -> None:
                super().__init__()
                self.current_match = self.summoner.current_match

                self.summonerChampion = self.summoner.current_match.champion
                self.opponents, self.teammates = self.setOpponentsAndTeammates()

            def setOpponentsAndTeammates(self):
                self.blueTeam = self.current_match.blue_team 
                self.redTeam = self.current_match.red_team

                self.opponents, self.teammates = self.blueTeam, self.redTeam if self.summoner not in self.blueTeam.participants else self.redTeam, self.blueTeam

        return Game().setOpponentsAndTeammates()

    def getUserGames(self, numberOfGames):
        pass

    def addUserGame(self):
        pass