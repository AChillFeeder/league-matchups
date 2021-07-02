from leagueMatchups import LeagueMatchups

from account_management import Account, Usables



class Main(LeagueMatchups):

    def __init__(self) -> None:        
        self.account = Account()
        self.usables = Usables()

    def connect(self, request):
        self.account.connect(request)

    def register(self, request):
        self.account.register(request)


