from Strategies import Strategies
from VideoPoker import VideoPoker
from PayoutTable import PayoutTable


class OddsSimulator(object):
    def __init__(self, payout_table, video_poker=None, strategies=None):
        self.video_poker = VideoPoker()
        self.strategies = Strategies()
        self.payout_table = PayoutTable(payout_table)

    def run_simulation(self, hand):
        for k in range(32):
            self._run_strategy(hand, self.strategies[k], self.payout_table, self.video_poker.hand_evaluator)

    def populate_list_to_object(self, obj, ls):
        obj.populate(ls)

    def _run_strategy(self, hand, strategy, payout_table, hand_evaluator):
        return strategy.get_payout_from_strategy(hand, payout_table, hand_evaluator)

    def print_object_info(self, obj):
        obj.print_info()
        print ""


if __name__ == "__main__":
    print "Started!"
    o = OddsSimulator("none")
    for k in range(32):
        o.print_object_info(o.strategies[k])
    o.video_poker.dealer.deck.print_deck()

