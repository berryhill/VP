from Dealer import Dealer
from Player import Player
from HandEvaluator import HandEvaluator
from Card import Card


class VideoPoker(object):
    def __init__(self, player=None, dealer=None, hand_evaluator=None, hand_list=None):
        self.player = Player()
        self.dealer = Dealer()
        self.hand_evaluator = HandEvaluator()

    def deal_player_hand(self):
        for k in range (5):
            self.player.add_card(self.dealer.deal_card())

    def deal_player_card(self):
        # print "hand before deal_player_card"
        # self.hand.print_hand()
        self.player.add_card(self.dealer.deal_card())

    def deal_player_indexed_card(self, index):
        self.player.add_card(self.dealer.deal_indexed_card(index))

    def player_submit_play(self):
        self.discard_pile = self.player.submit_play()

    def player_add_discard_pile(self):
        discard_pile_length = len(self.discard_pile)
        for k in range(discard_pile_length):
            self.player.add_card(self.discard_pile.pop(0))

    def return_card_to_deck(self, index):
        # print k
        # self.hand.print_hand()
        self.player.hand.insert(index, Card(-1, -1))
        self.dealer.deck.append(self.player.hand.pop(index+1))

    def insert_card_to_deck(self, hand_index, deck_index):
        self.player.hand.insert(hand_index, Card(-1, -1))
        self.dealer.deck.insert(deck_index, self.player.hand.pop(hand_index+1))

    def return_hand_to_deck(self):
        for k in range(5):
            self.return_card_to_deck(k)

    def return_hand_to_deck_indexed(self, ls):
        ls.sort()
        for k in range(5):
            self.insert_card_to_deck(k, ls[k])

    def populate(self, ls):
        for k in range(5):
            self.deal_player_indexed_card(ls[k])
        self.hand_list = ls
        ls.sort(reverse=True)
        for k in range(5):
            self.dealer.deck.pop(ls[k])


if __name__ == "__main__":
    print "Started!"
    vp = VideoPoker()
    vp.dealer.deck.print_deck()
    vp.player.hand.print_hand()

















