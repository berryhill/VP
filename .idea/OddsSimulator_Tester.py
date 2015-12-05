import unittest
from OddsSimulator import OddsSimulator


class OddsSimulator_Tester(unittest.TestCase):
    def setUp(self, o=None):
        self.o = OddsSimulator()

    def test_num_strategies(self):
        self.assertTrue(len(self.o.strategies) == 32)

    def test_num_take_zero(self):
        self.assertTrue(self.o.strategies[0].get_take_type() == "Take Zero")

    def test_num_take_one(self):
        for k in range(1, 6, 1):
            self.assertTrue(self.o.strategies[k].get_take_type() == "Take One")

    def test_num_take_two(self):
        for k in range(6, 16, 1):
            self.assertTrue(self.o.strategies[k].get_take_type() == "Take Two")

    def test_num_take_three(self):
        for k in range(16, 26, 1):
            self.assertTrue(self.o.strategies[k].get_take_type() == "Take Three")

    def test_num_take_four(self):
        for k in range(26, 31, 1):
            self.assertTrue(self.o.strategies[k].get_take_type() == "Take Four")

    def test_num_take_five(self):
        self.assertTrue(self.o.strategies[31].get_take_type() == "Take Five")

    def test_run_strategy(self):
        for k in range(32):
            self.assertTrue(self.o.run_strategy(self.o.strategies[k]) == -1)


if __name__ == '__main__':
    unittest.main(exit=False)

