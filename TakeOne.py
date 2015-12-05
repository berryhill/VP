from Strategy import Strategy


class TakeOne(Strategy):
    def __init__(self, holds):
        super(TakeOne, self).__init__("Take One", holds)

    def get_payout_from_strategy(self, hand, payout_table, hand_evaluator):
        return self.rate_hand_for_payout(hand, payout_table, hand_evaluator)