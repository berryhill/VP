from Strategy import Strategy


class TakeThree(Strategy):
    def __init__(self, holds):
        super(TakeThree, self).__init__("Take Three", holds)

    def get_payout_from_strategy(self, hand, payout_table, hand_evaluator):
        pass
