import requests
import json

# correct patches: https://ddragon.leagueoflegends.com/api/versions.json
# champion information: http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json
# community dragon: https://www.communitydragon.org/docs


class Summoner:
    def __init__(self, summoner_name, region='na1') -> None:
        # General information
        self.api_key = "RGAPI-456e8e78-aa2c-4efd-a676-c128986caa39"
        self.summoner_name = summoner_name.lower()
        self.region = region # don't forget to change it
        self.in_game = True
        self.patch = "11.9.1"
        self.error = ""

        # Summoner and champion ID<=>Name conversions
        self.summoner_id, self.account_id, self.puuid = self.get_summoner_id_from_name()
        self.champion_id_to_name = self.get_champion_name_from_id()

        # Current game information
        self.current_players = self.get_all_players_current_game()
        self.team1 = dict(list(self.current_players.items())[:5])
        self.team2 = dict(list(self.current_players.items())[5:])
        self.opponents = self.team2 if self.summoner_name in list(self.team1.keys()) else self.team1
        self.player_champion = self.current_players[self.summoner_name]
        
    def useful_data(self) -> str:
        if self.in_game:
            return json.dumps({
                'summoner_name': self.summoner_name,
                'player_champion': self.player_champion,
                'enemy_champions': list(self.opponents.values()),
                'opponents': self.opponents,
            })
        else:
            return json.dumps({'error': 'summoner not in a game'})


    def get_summoner_id_from_name(self) -> list:
        """
            {
                "id": "ZIMHUx81SqvxNMZYZ9FKwUCmHD_2YyOnnDXVwHnY3uP8PqY",
                "accountId": "Xcq4VnTKWmg29AUULFKa3yDaFi9easUPl0PDpVKw3qhZ-5Q",
                "puuid": "wobtCDNmeldz7yWG88dNUEyMApT2jobRyNTw8pDpwgZsW-hEauP1SJedTQNxJ7PXwIjuBvB1MHHX9w",
                "name": "Okalu",
                "profileIconId": 1590,
                "revisionDate": 1618674262487,
                "summonerLevel": 270
            }
        """
        data = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key={self.api_key}'
        ).json()

        return data['id'], data['accountId'], data['puuid']
        


    def get_champion_name_from_id(self):
        # ddragon imposes strict request limits, so I tap on them once and save relevant data
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


    def get_all_players_current_game(self) -> list:
        """
        {
            "gameId": 3873295464,
            "mapId": 12,
            "gameMode": "ARAM",
            "gameType": "MATCHED_GAME",
            "gameQueueConfigId": 450,
            "participants": [
                {
                    "teamId": 100,
                    "spell1Id": 4,
                    "spell2Id": 32,
                    "championId": 518,
                    "profileIconId": 603,
                    "summonerName": "Stokers Chew",
                    "bot": false,
                    "summonerId": "vlGpCwxPlIT4GxAeekNj4P3JB5zUzcBI_56xnwBfHtGNZNg",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8128,
                            8139,
                            8138,
                            8135,
                            8210,
                            8236,
                            5008,
                            5008,
                            5001
                        ],
                        "perkStyle": 8100,
                        "perkSubStyle": 8200
                    }
                },
                {
                    "teamId": 100,
                    "spell1Id": 32,
                    "spell2Id": 4,
                    "championId": 104,
                    "profileIconId": 4904,
                    "summonerName": "Rance",
                    "bot": false,
                    "summonerId": "tlnwB8L3ANMCWKtmjZ2QaBEhecjcVUoSPJYMo7wgUIxQOKY",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8005,
                            9111,
                            9103,
                            8299,
                            8233,
                            8236,
                            5008,
                            5008,
                            5003
                        ],
                        "perkStyle": 8000,
                        "perkSubStyle": 8200
                    }
                },
                {
                    "teamId": 100,
                    "spell1Id": 4,
                    "spell2Id": 7,
                    "championId": 267,
                    "profileIconId": 3179,
                    "summonerName": "kissabee",
                    "bot": false,
                    "summonerId": "v4z9ayuRJ1zg4w8_dHlpXwePImaLoZ7TllPITYonel4fQbA",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8214,
                            8275,
                            8234,
                            8236,
                            8009,
                            9105,
                            5007,
                            5008,
                            5003
                        ],
                        "perkStyle": 8200,
                        "perkSubStyle": 8000
                    }
                },
                {
                    "teamId": 100,
                    "spell1Id": 32,
                    "spell2Id": 4,
                    "championId": 9,
                    "profileIconId": 1110,
                    "summonerName": "Patapown64",
                    "bot": false,
                    "summonerId": "lpmJKEwY3OAF6O2A10CjBCQgcx2YKtd-t4lBtzKZ0-oTi8I",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8439,
                            8463,
                            8429,
                            8451,
                            8106,
                            8126,
                            5007,
                            5002,
                            5001
                        ],
                        "perkStyle": 8400,
                        "perkSubStyle": 8100
                    }
                },
                {
                    "teamId": 100,
                    "spell1Id": 21,
                    "spell2Id": 4,
                    "championId": 101,
                    "profileIconId": 4904,
                    "summonerName": "iCertainDeath",
                    "bot": false,
                    "summonerId": "K6_YYb_SDE0xH2rjGffJ1HskvbQBL-LE1vhpL-VryEDU6qA",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8229,
                            8226,
                            8210,
                            8236,
                            8126,
                            8106,
                            5008,
                            5008,
                            5002
                        ],
                        "perkStyle": 8200,
                        "perkSubStyle": 8100
                    }
                },
                {
                    "teamId": 200,
                    "spell1Id": 4,
                    "spell2Id": 32,
                    "championId": 31,
                    "profileIconId": 983,
                    "summonerName": "EFGGuy",
                    "bot": false,
                    "summonerId": "RuDpSokDFOZgDmHEukra0zIZKZB4G5NR3pDl4Sw7dMJICgg",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8229,
                            8226,
                            8210,
                            8236,
                            8106,
                            8126,
                            5007,
                            5008,
                            5001
                        ],
                        "perkStyle": 8200,
                        "perkSubStyle": 8100
                    }
                },
                {
                    "teamId": 200,
                    "spell1Id": 32,
                    "spell2Id": 4,
                    "championId": 266,
                    "profileIconId": 3788,
                    "summonerName": "How I Met Faker",
                    "bot": false,
                    "summonerId": "tYhiyPxplLmYwRmKgZZ7rlwEcHnQseDf6lpkyMGmrKBZWmo",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8010,
                            9111,
                            9105,
                            8299,
                            8139,
                            8135,
                            5008,
                            5008,
                            5002
                        ],
                        "perkStyle": 8000,
                        "perkSubStyle": 8100
                    }
                },
                {
                    "teamId": 200,
                    "spell1Id": 32,
                    "spell2Id": 4,
                    "championId": 82,
                    "profileIconId": 554,
                    "summonerName": "Bacon Bot",
                    "bot": false,
                    "summonerId": "DtsgXpxb6dpt3vW0IdtGSELx9hjiHlN1oDx2ZH7pAINUBcQ",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8439,
                            8463,
                            8444,
                            8453,
                            9105,
                            9111,
                            5008,
                            5008,
                            5003
                        ],
                        "perkStyle": 8400,
                        "perkSubStyle": 8000
                    }
                },
                {
                    "teamId": 200,
                    "spell1Id": 32,
                    "spell2Id": 4,
                    "championId": 517,
                    "profileIconId": 4018,
                    "summonerName": "SICK OF LOSING",
                    "bot": false,
                    "summonerId": "UDMsKRg4oYU3QPIODHkJo5EA5Q_3ijwGB9SZMOZmRAPRp-A",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8010,
                            8009,
                            9105,
                            8299,
                            8429,
                            8453,
                            5007,
                            5002,
                            5001
                        ],
                        "perkStyle": 8000,
                        "perkSubStyle": 8400
                    }
                },
                {
                    "teamId": 200,
                    "spell1Id": 3,
                    "spell2Id": 4,
                    "championId": 22,
                    "profileIconId": 585,
                    "summonerName": "Scarlemm",
                    "bot": false,
                    "summonerId": "n0kbFLMCgdN1it4qO5DFW4kAoaBqfMOJpXn01r2plJUY5vE",
                    "gameCustomizationObjects": [],
                    "perks": {
                        "perkIds": [
                            8229,
                            8226,
                            8210,
                            8237,
                            8009,
                            8014,
                            5007,
                            5008,
                            5001
                        ],
                        "perkStyle": 8200,
                        "perkSubStyle": 8000
                    }
                }
            ],
            "observers": {
                "encryptionKey": "fYSnyIoIK1EF4wUxhJISyOQMqODLq2AG"
            },
            "platformId": "NA1",
            "bannedChampions": [],
            "gameStartTime": 1618845424491,
            "gameLength": 263
        }
        """
        
        players_data = requests.get(
            f'https://{self.region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{self.summoner_id}?api_key={self.api_key}'
        ).json()["participants"]

        player_name_to_champion = {player["summonerName"].lower() : self.champion_id_to_name[str(player["championId"])] for player in players_data}

        return player_name_to_champion
        

    


