import unittest
from Hand import Hand
from Card import Card
from HandEvaluator import HandEvaluator


class HandEvaluator_Tester(unittest.TestCase):
    def setUp(self, hand=None, eval=None):
        self.hand = Hand()
        self.eval = HandEvaluator()

    def test_hand_fullhouse(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(1, 1))
        self.hand.append(Card(2, 1))
        self.hand.append(Card(1, 2))
        self.hand.append(Card(0, 2))
        self.hand.append(Card(3, 1))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "FullHouse")

    def test_hand_straight(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(1, 1))
        self.hand.append(Card(2, 2))
        self.hand.append(Card(1, 5))
        self.hand.append(Card(0, 4))
        self.hand.append(Card(3, 3))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "Straight")

    def test_hand_two_pair(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(1, 2))
        self.hand.append(Card(2, 2))
        self.hand.append(Card(1, 4))
        self.hand.append(Card(0, 4))
        self.hand.append(Card(3, 10))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "TwoPair")

    def test_hand_pair(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(1, 12))
        self.hand.append(Card(2, 12))
        self.hand.append(Card(1, 6))
        self.hand.append(Card(0, 4))
        self.hand.append(Card(3, 9))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "Pair")

    def test_hand_pair_not(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(1, 1))
        self.hand.append(Card(2, 2))
        self.hand.append(Card(1, 6))
        self.hand.append(Card(0, 4))
        self.hand.append(Card(3, 10))

        self.assertFalse(self.eval.evaluate_hand(self.hand) == "Pair")

    def test_hand_trips(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(1, 2))
        self.hand.append(Card(2, 2))
        self.hand.append(Card(1, 2))
        self.hand.append(Card(0, 4))
        self.hand.append(Card(3, 10))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "Trips")

    def test_hand_quads(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(1, 2))
        self.hand.append(Card(2, 2))
        self.hand.append(Card(3, 2))
        self.hand.append(Card(0, 2))
        self.hand.append(Card(3, 10))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "Quads")

    def test_hand_flush(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(2, 2))
        self.hand.append(Card(2, 4))
        self.hand.append(Card(2, 6))
        self.hand.append(Card(2, 8))
        self.hand.append(Card(2, 10))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "Flush")

    def test_hand_straight_flush(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(2, 2))
        self.hand.append(Card(2, 3))
        self.hand.append(Card(2, 4))
        self.hand.append(Card(2, 5))
        self.hand.append(Card(2, 6))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "StraightFlush")

    def test_hand_nothing(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(0, 7))
        self.hand.append(Card(1, 6))
        self.hand.append(Card(2, 3))
        self.hand.append(Card(2, 13))
        self.hand.append(Card(3, 10))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "Nothing")

    def test_hand_not_straight_flush(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(2, 1))
        self.hand.append(Card(2, 10))
        self.hand.append(Card(2, 11))
        self.hand.append(Card(2, 12))
        self.hand.append(Card(2, 13))

        self.assertFalse(self.eval.evaluate_hand(self.hand) == "StraightFlush")

    def test_hand_royal_flush(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(2, 1))
        self.hand.append(Card(2, 10))
        self.hand.append(Card(2, 11))
        self.hand.append(Card(2, 12))
        self.hand.append(Card(2, 13))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "RoyalFlush")

    def test_hand_wheel_straight(self):
        for k in range(5):
            self.hand.pop(0)
        self.hand.append(Card(2, 1))
        self.hand.append(Card(3, 10))
        self.hand.append(Card(0, 11))
        self.hand.append(Card(2, 12))
        self.hand.append(Card(1, 13))

        self.assertTrue(self.eval.evaluate_hand(self.hand) == "Straight")

if __name__ == '__main__':
    unittest.main(exit=False)
