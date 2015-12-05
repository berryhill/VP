import unittest
from PayoutTable import PayoutTable

class PayoutTable_Tester(unittest.TestCase):
    def setUp(self, payout_table=None, payout_list=None):
        self.payout_list = [250, 50, 6, 5, 4, 3, 2, 1, 0]
        self.payout_table = PayoutTable(self.payout_list)

    def test_populate_payout(self):
        for k in range(9):
            self.assertTrue(self.payout_table[k].get_payout_value() == self.payout_list[k])


if __name__ == '__main__':
    unittest.main(exit=False)
