import time

class HandEvaluator(object):
    def __init__(self, histo_value=None, hist_suite=None,
                   histo_primative_results=None, hand=None):
         self.histo_value = [0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0]
         self.histo_suite = [0, 0, 0, 0]
         self.histo_primative_results = {
             'Pair': 0,
             'Trips': 0,
             'Quads': 0,
             'Flush': 0,
             'Straight': 0
         }

    def evaluate_hand(self, hand):
        self._set_hand(hand)
        self._eval_pair()
        self._eval_trips()
        self._eval_quads()
        self._eval_flush()
        self._eval_straight()
        if self._eval_full_house():
            return "FullHouse"
        elif self._eval_straight_flush():
            return "StraightFlush"
        elif self._eval_two_pair():
            return "TwoPair"
        elif self._eval_royal_flush():
            return "RoyalFlush"
        elif self.histo_primative_results.get('Trips') == 1:
            return "Trips"
        elif self.histo_primative_results.get('Quads') == 1:
            return "Quads"
        elif self.histo_primative_results.get('Flush') == 1:
            return "Flush"
        elif self.histo_primative_results.get('Straight') == 1:
            return "Straight"
        elif self._eval_paying_pair():
            return "Pair"
        else:
            return "Nothing"

    def _clear_histos(self):
         for k in range(13):
             self.histo_value[k] = 0
         for k in range(4):
             self.histo_suite[k] = 0
         self.histo_primative_results['Pair'] = 0
         self.histo_primative_results['Trips'] = 0
         self.histo_primative_results['Quads'] = 0
         self.histo_primative_results['Straight'] = 0
         self.histo_primative_results['Flush'] = 0

    def erase_hand(self):
         # self.hand = None
         self._clear_histos()

    def _set_hand(self, hand):
         self.hand = hand
         self.hand.sort(key=lambda x: x._value, reverse=False)
         # self.hand.print_hand()
         self._diagnose_hand(self.hand)

    def _diagnose_hand(self, hand):
         for k in range(5):
             self.histo_value[hand[k].get_value()-1] += 1
             self.histo_suite[hand[k].get_suite()] += 1

    def _eval_pair(self):
        for k in range(13):
            if self.histo_value[k] == 2:
                self.histo_primative_results['Pair'] += 1

    def _eval_paying_pair(self):
        for k in range(13):
            if self.histo_value[k] == 2:
                if k >= 10 or k == 0:
                    return True
                else:
                    return False

    def _eval_trips(self):
        for k in range(13):
            if self.histo_value[k] == 3:
                self.histo_primative_results['Trips'] += 1
            else:
                pass

    def _eval_quads(self):
        for k in range(13):
            if self.histo_value[k] == 4:
                self.histo_primative_results['Quads'] += 1
            else:
                pass

    def _eval_flush(self):
        for k in range(4):
            if self.histo_suite[k] == 5:
                self.histo_primative_results['Flush'] = 1
            else:
                pass

    def _eval_straight(self):
        if self.hand[4].get_value() - self.hand[0].get_value() == 4:
            self.histo_primative_results['Straight'] = 1
        elif self.hand[0].get_value() == 1:
            if self.hand[1].get_value() == 10:
                self.histo_primative_results['Straight'] = 1
                return True
        else:
            return False

    def _eval_two_pair(self):
        if self.histo_primative_results.get('Pair') == 2:
            return True

    def _eval_full_house(self):
        if self.histo_primative_results['Pair'] == 1 and \
                        self.histo_primative_results['Trips'] == 1:
            return True
        else:
            return False

    def _eval_straight_flush(self):
        if self.histo_primative_results['Flush'] and \
            self.histo_primative_results['Straight'] and \
            self.hand[1].get_value() != 10:
                return True
        else:
            return False

    def _eval_royal_flush(self):
        if self.histo_primative_results['Flush'] and \
            self.histo_primative_results['Straight'] and \
            self.hand[1].get_value() == 10:
                return True
        else:
            return False

    def print_histo_value(self):
        print "Value hist:"
        for k in range(13):
            print "     k = %i" % self.histo_value[k]

    def print_histo_suite(self):
        print "Value hist:"
        for k in range(4):
            print "     k = %i" % self.histo_suite[k]

    def print_histo_primative_results(self):
        print "Value histo:"
        print "     Pair = %i" % self.histo_primative_results.get('Pair')
        print "     Trips = %i" % self.histo_primative_results.get('Trips')
        print "     Quads = %i" % self.histo_primative_results.get('Quads')
        print "     Straight = %i" % self.histo_primative_results.get('Straight')
        print "     Flush = %i" % self.histo_primative_results.get('Flush')


