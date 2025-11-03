import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_init(self):
        self.assertIsInstance(self.stats.reader, PlayerReaderStub)

    def test_search(self):
        self.assertEqual(self.stats.search("Villevallaton"), None)
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
        self.assertEqual(len(self.stats.team("Eiole")), 0)

    def test_top(self):
        top = self.stats.top(3)
        self.assertEqual(len(top), 4)
        self.assertEqual(top[0].name, "Gretzky")
        top = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(len(top), 3)
        self.assertEqual(top[0].name, "Lemieux")
        top = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(len(top), 3)
        self.assertEqual(top[1].name, "Yzerman")

