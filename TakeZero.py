from Strategy import Strategy
import time


class TakeZero(Strategy):
    def __init__(self, holds):
        super(TakeZero, self).__init__("Take Zero", holds)

    def get_payout_from_strategy(self, hand, payout_table, video_poker):
        start = time.clock()
        payout = float(self.rate_hand_for_payout(hand, payout_table, video_poker))
        elapsed_time = time.clock() - start
        print "Time Taken TakeZero = %f " % elapsed_time
        return payout

