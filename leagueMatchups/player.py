import cassiopeia
import cassiopeia_championgg
import os

from datapipelines import NotFoundError
from leagueMatchups.database import GamesDatabase, NotesDatabase

class Player():

    def __init__(self, summonerName: str, region: str) -> None:

        self.gamesDatabase = GamesDatabase()
        self.notesDatabase = NotesDatabase()

        try:
            with open(os.path.join('leagueMatchups' ,'data', 'api_key.txt'), "r") as file:
                self.apiKey = file.read()
        except FileNotFoundError:
            raise Exception("Create an api_key.txt that holds your api key")

        self.summonerName = summonerName.lower()
        self.id: int = 0

        ##### TESTING ######
        self.summonerName = "LifeIsChocolate".lower()
        
        self.region = region

        cassiopeia.set_riot_api_key(self.apiKey) 
        cassiopeia.set_default_region(self.region) 

        self.summoner = cassiopeia.Summoner(name=self.summonerName)
        print("summoner's name: ", self.summoner.name)





    def getCurrentGame(self) -> dict:
        """
            Get current game information
            returns => {
                "summoner_champion": {name, image, id}
                "enemy_team_champion": [{name, image, id}, ...]
            }
        """
        try:
            self.currentMatch = self.summoner.current_match.to_dict()
        except NotFoundError:
            return {"success": False}

        summoner_champion, enemy_team_champions = self.sanitizeCurrentMatchData()

        result = {
            "success": True,
            "summoner_champion": {
                "name": summoner_champion.name,
                "image": summoner_champion.image.url,
                "full_image": summoner_champion.skins[0].loading_image_url,
                "id": summoner_champion.id
            },
            "enemy_team_champions": []
        }

        for champion in enemy_team_champions:
            result['enemy_team_champions'].append(
                {
                    "name": champion.name,
                    "image": champion.image.url,
                    "full_image": champion.skins[0].loading_image_url,
                    "id": champion.id,
                    "spells": [
                        {
                        "cooldowns": champion.spells[0].cooldowns,
                        "costs": champion.spells[0].costs,
                        "description": champion.spells[0].description,
                        "image_info": champion.spells[0].image_info.url,
                        },
                        {
                        "cooldowns": champion.spells[1].cooldowns,
                        "costs": champion.spells[1].costs,
                        "description": champion.spells[1].description,
                        "image_info": champion.spells[1].image_info.url,
                        },
                        {
                        "cooldowns": champion.spells[2].cooldowns,
                        "costs": champion.spells[2].costs,
                        "description": champion.spells[2].description,
                        "image_info": champion.spells[2].image_info.url,
                        },
                        {
                        "cooldowns": champion.spells[3].cooldowns,
                        "costs": champion.spells[3].costs,
                        "description": champion.spells[3].description,
                        "image_info": champion.spells[3].image_info.url,
                        },
                    ],
                    "enemy_tips": champion.enemy_tips
                }
            )

        return result

    def sanitizeCurrentMatchData(self):

        all_participants = self.currentMatch['participants']

        # Find summoner participant and turn him to a Champion object
        summoner_participant = [participant for participant in all_participants if participant["summonerName"].lower() == self.summonerName][0]
        summoner_champion = cassiopeia.Champion(id=summoner_participant['championId'])

        # splitting the teams => team array has champion ID only, no other data
        team_one, team_two = self.teamsFromCurrentGame(all_participants)

        # defining the enemy team
        enemy_team_champions = team_one if summoner_participant['teamId'] == 200 else team_two

        return summoner_champion, enemy_team_champions
        

        
    @staticmethod
    def teamsFromCurrentGame(all_participants):
        team_one = [cassiopeia.Champion(id=participant['championId']) for participant in all_participants if participant['teamId']==100]
        team_two = [cassiopeia.Champion(id=participant['championId']) for participant in all_participants if participant['teamId']==200]

        return team_one, team_two

    def saveGame(self, playerChampion, laneOpponent, win, id) -> int:
        """Saves the game and returns it's ID"""
        gameID = self.gamesDatabase.addSummonerGame(playerChampion, laneOpponent, win, id)
        return gameID

    def getAllSummonerGames(self, id):
        result = []

        # ID playerChampion laneOpponent win userID

        all_games = self.gamesDatabase.getAllSummonerGames(id)
        for game in all_games:
            summoner_champion = cassiopeia.Champion(id=game[1])
            opponent_champion = cassiopeia.Champion(id=game[2])
            result.append( {
                "playerChampion": {
                    "name": summoner_champion.name,
                    "image": summoner_champion.image.url,
                    "id": summoner_champion.id,
                    "full_image": summoner_champion.skins[0].loading_image_url,
                },
                "opponentChampion": {
                    "name": opponent_champion.name,
                    "image": opponent_champion.image.url,
                    "id": opponent_champion.id,
                    "full_image": opponent_champion.skins[0].loading_image_url,
                },
                "victory": game[3],
                "id": game[0]
            } )

        return result

    def saveNotes(self, notes, userID, gameID):
        # test blank table
        for note in notes:
            print("note: " + note)
            self.notesDatabase.addNote(note, userID, gameID)
            
    def getNotesByGameID(self, gameID) -> list:
        result = self.notesDatabase.getNotesByGame(gameID)
        return result

    def getNotesByUserID(self, userID) -> list:
        all_notes = self.notesDatabase.getNotesByUser(userID)
        result = []
        for note in all_notes:
            result.append( {
                "id": note[0],
                "noteContent": note[1], 
                "gameID": note[2],
                "userID": note[3]
            } )
        return result

    def deleteNoteByNoteID(self, noteID):
        pass

