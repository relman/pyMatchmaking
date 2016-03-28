import unittest
from midterm import matchmaking


class TestSolution(unittest.TestCase):
    players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]

    def test1(self):
        self.assertSequenceEqual(matchmaking(self.players, teams=1, min_team=1, max_team=1), [['a']])

    def test2(self):
        self.assertSequenceEqual(matchmaking(self.players, teams=2, min_team=1, max_team=1), [['a'], ['c']])

    def test3(self):
        self.assertSequenceEqual(matchmaking(self.players, teams=2, min_team=1, max_team=2), [['a', 'd'], ['c', 'e']])

    def test4(self):
        self.assertEqual(matchmaking(self.players, teams=2, min_team=3), False)

    def test5(self):
        self.assertEqual(matchmaking(self.players, teams=6, min_team=1), False)

    def test6(self):
        self.assertSequenceEqual(matchmaking(self.players, teams=1, min_team=1), [['a', 'c', 'd', 'e', 'f']])

if __name__ == '__main__':
    unittest.main()
