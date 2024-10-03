import unittest
import module_12_2


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = module_12_2.Runner("Усэйн", 10)
        self.andrey = module_12_2.Runner("Андрей", 9)
        self.nick = module_12_2.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def test_tournament_1(self):
        tour_1 = module_12_2.Tournament(90, self.usain, self.nick)
        all_results = tour_1.start()
        self.assertTrue(all_results[2], self.nick)

    def test_tournament_2(self):
        tour_2 = module_12_2.Tournament(90, self.andrey, self.nick)
        all_results = tour_2.start()
        self.assertTrue(all_results[2], self.nick)

    def test_tournament_3(self):
        tour_3 = module_12_2.Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tour_3.start()
        self.assertTrue(all_results[3], self.nick)


if __name__ == "__main__":
    unittest.main()
