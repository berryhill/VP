from Strategy import Strategy


class TakeFour(Strategy):
    def __init__(self, holds):
        super(TakeFour, self).__init__("Take Four", holds)

    def get_payout_from_strategy(self, hand, payout_table, hand_evaluator):
        pass