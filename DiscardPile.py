
class DiscardPile(list):
    def __init__(self):
        super(DiscardPile, self).__init__()

    def print_discard_pile(self):
        print "--------------------------------"
        print "Discard Pile = "
        for k in range(len(self)):
            print "     Card %i %i" % (self[k].get_suite(), self[k].get_value())
        print "--------------------------------"
