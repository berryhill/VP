from Strategies import Strategies
from VideoPoker import VideoPoker
from PayoutTable import PayoutTable

class OddsSimulator(object):
    global_calc = 0
    def __init__(self, payout_table, video_poker=None, strategies=None, optimal_hold_list=None):
        self.video_poker = VideoPoker()
        self.strategies = Strategies()
        self.payout_table = PayoutTable(payout_table)
        self.optimal_holds_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def run_simulation(self, hand):
        for k in range(32):
            self.optimal_holds_list[k] = \
                self._run_strategy(hand, self.strategies[k], self.payout_table, self.video_poker)
        max = 0.0
        max_index = -1
        for k in range(32):
            if self.optimal_holds_list[k] > max:
                max_index = k
        # print sum(self.optimal_holds_list) / 32.0
        print ""
        print "/////////////////////////////"
        print "Player Should Hold: "
        self._standard_io_formatter(hand, self.strategies[max_index])
        print "Optimal Payout for this hand: %f" % max

    def populate_list_to_object(self, obj, ls):
        obj.populate(ls)

    def _standard_io_formatter(self, hand, strategies):
        for k in range(5):
            if strategies[k] == 1:
                self.print_object_info(hand[k])

    def _run_strategy(self, hand, strategy, payout_table, video_poker):
        return strategy.get_payout_from_strategy(hand, payout_table, video_poker)

    def print_object_info(self, obj):
        obj.print_info()
        print ""

    def print_percent_done(self, calcs):
        pass

