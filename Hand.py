from Card import Card

class Hand(list):
    def __init__(self):
        super(Hand, self).__init__()
        for k in range(5):
            self.append(Card(-1, -1))

    def get_card(self, selection):
        return self[selection]

    def print_info(self):
        print "--------------------------------"
        print "Hand = "
        for k in range(len(self)):
            print "     Card %i = %i %i" % (k, self[k].get_value(), self[k].get_suite())
        print "--------------------------------"