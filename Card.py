
class Card(object):
    def __init__(self, suite, value):
        self._suite = suite
        self._value = value

    def get_suite(self):
        return self._suite

    def get_value(self):
        return self._value

    def print_info(self):
        card_suite = None
        if self.get_suite() == 0:
            card_suite = "Hearts"
        elif self.get_suite() == 1:
            card_suite = "Clubs"
        elif self.get_suite() == 2:
            card_suite = "Diamanods"
        elif self.get_suite() == 3:
            card_suite = "Spades"
        if self.get_value() > 1 and self.get_value() < 11:
            print "     %i of %s" % (self.get_value(), card_suite)
        elif self.get_value() == 1:
            print "     Ace of %s" % card_suite
        elif self.get_value() == 11:
            print "     Jack of %s" % card_suite
        elif self.get_value() == 12:
            print "     Queen of %s" % card_suite
        elif self.get_value() == 13:
            print "     King of %s" % card_suite
