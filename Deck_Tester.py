from Deck import Deck
import unittest

class Deck_Tester(unittest.TestCase):
    def setUp(self):
        self.deck = Deck(52)

    def test_contains_cards(self):
        self.assertTrue(len(self.deck) == 53)

if __name__ == '__main__':
    unittest.main(exit=False)

