import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        self.assertEqual(self.statistics.search("Kurri").name,"Kurri")
    
    def test_search_ei_loyda_olematonta_pelaajaa(self):
        self.assertFalse(self.statistics.search("Turri"))
    
    def test_team_palauttaa_tiimin_pelaajat(self):
        team = self.statistics.team("PIT")
        self.assertEqual(team[0].name,"Lemieux")
    
    def test_top_palauttaa_parhaan_pelaajan(self):
        top = self.statistics.top(1)[0].name
        self.assertEqual(top,"Gretzky")
    
    def test_sort_by_goals(self):
        top = self.statistics.top(1,SortBy.GOALS)[0].name
        self.assertEqual(top,"Lemieux")
    
    def test_sort_by_assists(self):
        top = self.statistics.top(1,SortBy.ASSISTS)[0].name
        self.assertEqual(top,"Gretzky")