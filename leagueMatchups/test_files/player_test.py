import unittest
import json

from player import Player

summonerName = "Skki"
region = "NA"

player = Player(summonerName, region)

class TestPlayer(unittest.TestCase):

    def testGetCurrentGame(self):
        summonerChampion, enemyTeamChampions = player.getCurrentGame()
        
        self.assertTrue(len(enemyTeamChampions)==5)
        self.assertIsNotNone(summonerChampion)

        self.assertIsNotNone(summonerChampion.name)
        self.assertIsNotNone(summonerChampion.key)
        self.assertIsNotNone(summonerChampion.image.url)

        self.assertTrue(len([spell.cooldowns for spell in summonerChampion.spells])==4)
            
        
        # champion spells cooldown

if __name__ == '__main__':
    unittest.main()
