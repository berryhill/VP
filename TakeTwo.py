from Strategy import Strategy


class TakeTwo(Strategy):
    def __init__(self, holds):
        super(TakeTwo, self).__init__("Take Two", holds)

    def get_payout_from_strategy(self, hand, payout_table, hand_evaluator):
        pass
