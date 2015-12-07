import unittest
from OddsSimulator import OddsSimulator


class OddsSimulator_Tester(unittest.TestCase):
    def setUp(self, o=None):
        self.o = OddsSimulator([250, 50, 25, 8, 5, 4, 3, 2, 1])
        # self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])

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

    def test_take_zero_strategy_straight_royal_flush(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 9, 10, 11, 12])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 250)

    def test_take_zero_strategy_straight_flush(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 50)
    def test_take_zero_strategy_quads(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 13, 26, 39, 3])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 25)

    def test_take_zero_strategy_fullhouse(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 13, 26, 1, 14])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 8)

    def test_take_zero_strategy_straight(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 14, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 5)

    def test_take_zero_strategy_flush(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 7])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 4)

    def test_take_zero_strategy_trips(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 13, 26, 6, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 3)

    def test_take_zero_strategy_twopair(self):
        self.o.populate_list_to_object(self.o.video_poker, [25, 12, 0, 13, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 2)

    def test_take_zero_strategy_payingpair(self):
        self.o.populate_list_to_object(self.o.video_poker, [12, 25, 1, 13, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[0],
                                             self.o.payout_table, self.o.video_poker) == 1)

    def test_take_one_strategy(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[1],
                                             self.o.payout_table, self.o.video_poker) == 1.063829787)
    """
    def test_take_two_strategy(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[6],
                                             self.o.payout_table, self.o.video_poker) > 0)

    def test_take_three_strategy(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[16],
                                             self.o.payout_table, self.o.video_poker) > 0)


    def test_take_four_strategy(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[26],
                                             self.o.payout_table, self.o.video_poker) > 0)

    def test_take_five_strategy(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o._run_strategy(self.o.video_poker.player.hand, self.o.strategies[31],
                                             self.o.payout_table, self.o.video_poker) > 0)
    """

    def test_simulation(self):
        self.o.populate_list_to_object(self.o.video_poker, [0, 1, 2, 3, 4])
        self.o.video_poker.player.hand.print_hand()
        self.assertTrue(self.o.run_simulation(self.o.video_poker.player.hand) > 0)

if __name__ == '__main__':
    unittest.main(exit=False)
