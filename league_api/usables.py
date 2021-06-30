from . import Interface
import requests, json

class Usables(Interface):
    
    def getChampionNameFromId(self):
        # ddragon imposes strict request limits, so I tap into them once and save relevant data
        try:
            with open(f'champion_{self.patch}.json', 'r') as file:
                champions_data = json.load(file)
        except Exception:
            champions_data = requests.get(
                f'http://ddragon.leagueoflegends.com/cdn/{self.patch}/data/en_US/champion.json'
            ).json()["data"]
            with open(f'champion_{self.patch}.json', 'w') as file:
                json.dump(champions_data, file)

        return {champion["key"] : champion["id"].lower() for champion in champions_data.values()}


    def getSummonerIdsFromSummonerName(self) -> list:
        data = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summonerName}?api_key={self.api_key}'
        ).json()

        return data['id'], data['accountId'], data['puuid']


    def setApiKey(self):
        pass

    def setCurrentPatch(self):
        pass
