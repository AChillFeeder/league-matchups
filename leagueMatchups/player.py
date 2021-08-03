import cassiopeia

class Player():

    def __init__(self, summonerName, region) -> None:

        self.apiKey = "RGAPI-32449df4-8989-47db-a52d-d087bcc3f108" # put it in file after
        self.summonerName = summonerName
        self.region = region # ALL CAPS

        cassiopeia.set_riot_api_key(self.apiKey) #
        cassiopeia.set_default_region(self.region) #

        self.summoner = cassiopeia.Summoner(name=self.summonerName)
        print("summoner's name: ",self.summoner.name)

    

    def getCurrentGame(self):
        self.currentMatch = cassiopeia.core.spectator.CurrentMatch(summoner=self.summonerName, region=self.region)
        print(self.currentMatch.to_json())

        self.opponents, self.teammates = (self.currentMatch.blue_team, self.currentMatch.red_team) if self.summoner in self.currentMatch.red_team.participants else (self.currentMatch.red_team, self.currentMatch.blue_team)
        self.summonerInGame = self.teammates.participants[self.summoner]

        return {
            "currentMatch": self.currentMatch.to_json()
            ,
            # "opponents": self.opponents,
            # "teammates": self.teammates,
            # "summonerInGame": self.summonerInGame
            }




    def getUserGames(self, numberOfGames):
        pass

    def addUserGame(self, params):
        # params: GAMES[summoner played, opponent champion, notes, tags, *popularity]
        pass