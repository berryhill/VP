from Strategy import Strategy


class TakeZero(Strategy):
    def __init__(self, holds):
        super(TakeZero, self).__init__("Take Zero", holds)

    def get_payout_from_strategy(self, hand, payout_table, video_poker):
        average_payout = float(self.rate_hand_for_payout(hand, payout_table, video_poker))
        # print average_payout
        return average_payout
