
class PayoutTable(list):
    def __init__(self, payout_list):
        super(PayoutTable, self).__init__()
        self.populate(payout_list)

    def populate(self, payout_list):
        self.append(RoyalFlushPayout(payout_list[0]))
        self.append(StraightFlushPayout(payout_list[1]))
        self.append(QuadsPayout(payout_list[2]))
        self.append(FullHousePayout(payout_list[3]))
        self.append(StraightPayout(payout_list[4]))
        self.append(FlushPayout(payout_list[5]))
        self.append(TripsPayout(payout_list[6]))
        self.append(TwoPairPayout(payout_list[7]))
        self.append(PairPayout(payout_list[8]))

    def print_info(self):
        for k in range(9):
            print "Payout k = "
            print "     Payout Type = %s" % self[k].get_payout_type()
            print "Payout Value = "
            print "     Payout Value = %i" % self[k].get_payout_value()


class Payout(object):
    def __init__(self, _payout_value, _payout_type):
        self._payout_value = _payout_value
        self._payout_type = _payout_type

    def get_payout_value(self):
        return self._payout_value

    def get_payout_type(self):
        return self._payout_type

    def print_info(self):
        print "Payout k = "
        print "     Payout Type = %s" % self._payout_type
        print "Payout Value = "
        print "     Payout Value = $i" % self._payout_value


class RoyalFlushPayout(Payout):
    def __init__(self, _payout_value):
        super(RoyalFlushPayout, self).__init__(_payout_value, "Royal Flush Payout")


class StraightFlushPayout(Payout):
    def __init__(self, _payout_value):
        super(StraightFlushPayout, self).__init__(_payout_value, "Straight Flush Payout")


class QuadsPayout(Payout):
    def __init__(self, _payout_value):
        super(QuadsPayout, self).__init__(_payout_value, "Quads Payout")


class FullHousePayout(Payout):
    def __init__(self, _payout_value):
        super(FullHousePayout, self).__init__(_payout_value, "Full House Payout")


class StraightPayout(Payout):
    def __init__(self, _payout_value):
        super(StraightPayout, self).__init__(_payout_value, "Straight Payout")


class FlushPayout(Payout):
    def __init__(self, _payout_value):
        super(FlushPayout, self).__init__(_payout_value, "Flush Payout")


class TripsPayout(Payout):
    def __init__(self, _payout_value):
        super(TripsPayout, self).__init__(_payout_value, "Trips Payout")


class TwoPairPayout(Payout):
    def __init__(self, _payout_value):
        super(TwoPairPayout, self).__init__(_payout_value, "Two Pair Payout")


class PairPayout(Payout):
    def __init__(self, _payout_value):
        super(PairPayout, self).__init__(_payout_value, "Pair Payout")






