import copy

class Strategy(list):
    def __init__(self, _type, _holds):
        super(Strategy, self).__init__()
        self._type = _type
        self._holds = _holds

    def get_take_type(self):
        return self._type

    def get_holds(self):
        return self._holds

    def rate_hand_for_payout(self, hand, payout_table, hand_evaluator):
        # print "Hand before rate_hand_for_payout"
        # self.hand.print_hand()
        rated_hand = hand_evaluator.evaluate_hand(copy.deepcopy(hand))
        # hand.erase_hand()
        if rated_hand == "RoyalFlush":
            return payout_table[0].get_payout_value()
        elif rated_hand == "StraightFlush":
            return payout_table[1].get_payout_value()
        elif rated_hand == "Quads":
            return payout_table[2].get_payout_value()
        elif rated_hand == "FullHouse":
            return payout_table[3].get_payout_value()
        elif rated_hand == "Straight":
            return payout_table[4].get_payout_value()
        elif rated_hand == "Flush":
            return payout_table[5].get_payout_value()
        elif rated_hand == "Trips":
            return payout_table[6].get_payout_value()
        elif rated_hand == "TwoPair":
            return payout_table[7].get_payout_value()
        elif rated_hand == "Pair":
            return payout_table[8].get_payout_value()
        else:
            return 0

    def print_info(self):
        print "Take Type = %s" % self._type
        print "Holds = %s" % self._holds





