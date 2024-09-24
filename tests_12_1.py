import module_12_1
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = module_12_1.Runner("walker")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = module_12_1.Runner("runner")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = module_12_1.Runner("Begun_1")
        runner_2 = module_12_1.Runner("Begun_2")

        for i in range(10):
            runner_1.run()
            runner_2.walk()

        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
