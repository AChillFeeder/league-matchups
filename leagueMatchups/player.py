import cassiopeia

class Player():

    def __init__(self, summonerName, region) -> None:

        self.apiKey = "RGAPI-d8180de0-d58f-4ea3-9e1f-0e6e7bf93aff" # put it in file after
        self.summonerName = "Godspeeds"
        self.region = "NA" # all caps

        cassiopeia.set_riot_api_key(self.apiKey) #
        cassiopeia.set_default_region(self.region) #

        self.summoner = cassiopeia.Summoner(name=self.summonerName)
        print("summoner's name: ",self.summoner.name)

    

    def getCurrentGame(self):
        self.currentMatch = cassiopeia.core.spectator.CurrentMatch(summoner=self.summonerName, region=self.region)

        self.opponents, self.teammates = (self.currentMatch.blue_team, self.currentMatch.red_team) if self.summoner in self.currentMatch.red_team.participants else (self.currentMatch.red_team, self.currentMatch.blue_team)
        self.summonerInGame = self.teammates.participants[self.summoner]

        print("Summoner champion: ", self.summonerInGame.champion.name)
        print("\nOpponents:")
        for opponent in self.opponents.participants:
            print(f"{opponent.summoner.name} playing as {opponent.champion.name}")


    def getUserGames(self, numberOfGames):
        pass

    def addUserGame(self, params):
        # params: GAMES[summoner played, opponent champion, notes, tags, *popularity]
        pass