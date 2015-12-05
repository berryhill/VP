from Hand import Hand
from Card import Card
from DiscardPile import DiscardPile

class Player(object):
    def __init__(self, hand=None, cash=None, holds=None):
        self.hand = Hand()
        self.cash = 100
        self.holds = [0, 0, 0, 0, 0]

    def add_card(self, card):
        for k in range(5):
            if self.hand[k].get_suite() == -1:
                self.hand.pop(k)
                self.hand.insert(k, card)
                break

    def hold_card(self, selection):
        self.holds[selection] = 1

    def add_holds(self, holds):
        self.holds = holds

    def submit_play(self, temp=None):
        temp = DiscardPile()
        for k in range(len(self.holds)):
            if self.holds[k] == 0:
                temp.append(self.hand.get_card(k))
                self.hand[k] = Card(-1, -1)
        # self.clear_holds()
        return temp

    def get_hand(self):
        return self.hand

    def get_holds(self):
        return self.holds

    def clear_holds(self):
        temp = [0, 0, 0, 0, 0]
        self.holds = list(temp)

    def print_holds(self):
        for k in range(5):
            print self.holds[k]
