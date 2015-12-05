from Deck import Deck
from DiscardPile import DiscardPile
import random
import copy

class Dealer(object):
    def __init__(self, deck=None, discard_pile=None, payout_table=None):
        self.deck = Deck(52)
        self.discard_pile = DiscardPile()

    def shuffle_deck(self):
        temp_deck = Deck(0)
        for k in range(len(self.deck)):
            temp_deck.append(self.deck.pop(random.randint(0, len(self.deck)-1)))
        self.deck = temp_deck

    def deal_card(self):
        return self.deck.pop(0)

    def deal_indexed_card(self, index):
        return copy.copy(self.deck[index])
        # return self.deck.pop(index))

    def rate_hand(self):
        pass

    def collect_hand(self):
        pass




