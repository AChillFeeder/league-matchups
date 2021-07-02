from . import Main
import requests, json, os

class Usables(Main):
    
    def getChampionKeyFromId(self):
        # ddragon imposes strict request limits, so I tap into them once and save relevant data
        try:
            with open( os.path.join('data', f'champion_{self.patch}.json') , 'r') as file:
                champions_data = json.load(file)
        except Exception:
            champions_data = requests.get(
                f'http://ddragon.leagueoflegends.com/cdn/{self.patch}/data/en_US/champion.json'
            ).json()["data"]
            with open( os.path.join('data', f'champion_{self.patch}.json') , 'w') as file:
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


    def playerGamesHistory(self, formValues):
        database = league_api.usables.openDatabase()

        # if the player already has other games
        # generate an ID by incrementing last game's ID
        # otherwise it's 1
        formValues["id"] = database[summoner_name]["games"][-1]['id'] + 1 if database[summoner_name]["games"] else 1

        tags = set()
        for note in formValues["notes"]:
            for word in note.split(' '):
                try:
                    if word[0] == '@':
                        tags.add(word)
                except IndexError:
                    continue

        formValues["tags"] = list(tags)

        database[summoner_name]['games'].append(formValues) # add new data to the database
        
        league_api.usables.saveToDatabase(database) # update the database

        return json.dumps({'saved': True, 'message': 'game saved successfully'})
