from Card import Card

class Deck(list):
    def __init__(self, num_cards):
        super(Deck, self).__init__()
        self.num_cards = 0
        for k in range(0,num_cards/13,1):
            for j in range(1,num_cards/4+1,1):
                self.append(Card(k, j))

    def print_card(self, arg):
        print "Card = %i" % self[arg].get_suite()

    def print_deck(self):
        print "--------------------------------"
        print "Discard Pile = "
        for k in range(len(self)):
            print "Card = %i %i" % (self[k].get_suite(), self[k].get_value())
        print "--------------------------------"

