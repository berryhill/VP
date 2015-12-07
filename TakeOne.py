from Strategy import Strategy


class TakeOne(Strategy):
    def __init__(self, holds):
        super(TakeOne, self).__init__("Take One", holds)

    def get_payout_from_strategy(self, hand, payout_table, video_poker):
        payout = 0.0
        calcs = 0.0
        video_poker.player.add_holds(self.get_holds())
        video_poker.player_submit_play()
        for k in range(47):
            video_poker.hand_evaluator.erase_hand()
            video_poker.deal_player_card()
            temp_payout = float(self.rate_hand_for_payout(hand, payout_table, video_poker))
            payout += temp_payout
            calcs += 1.0
            for j in range(5):
                if self._holds[j] == 0:
                    video_poker.return_card_to_deck(j)
        average_payout = payout / calcs
        video_poker.player_add_discard_pile()
        # print average_payout
        return average_payout

