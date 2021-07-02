
import account_management
import league_api

class LeagueMatchups:

    def __init__(self) -> None:
        self.session = {"connected": False, "summonerName": None} 
        self.accountManagement = account_management()

        if self.session["summonerName"]:
            self.leagueApi = league_api(self.summonerName)

        account = account_management()
        game = league_api()
    


    







    



