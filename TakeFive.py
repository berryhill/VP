from Strategy import Strategy


class TakeFive(Strategy):
    def __init__(self, holds):
        super(TakeFive, self).__init__("Take Five", holds)

    def get_payout_from_strategy(self, hand, payout_table, hand_evaluator):
        pass
