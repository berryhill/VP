from Strategy import Strategy


class TakeFour(Strategy):
    def __init__(self, holds):
        super(TakeFour, self).__init__("Take Four", holds)

    def get_payout_from_strategy(self, hand, payout_table, video_poker):
        payout = 0.0
        calcs = 0.0
        video_poker.player.add_holds(self.get_holds())
        video_poker.player_submit_play()
        temp = 0
        temp_index_one = 0
        temp_index_two = 0
        temp_index_three = 0
        temp_index_four = 0
        for c in range(5):
            if self.get_holds()[c] == 0:
                temp += 1
                if temp == 1:
                    temp_index_one = c
                elif temp == 2:
                    temp_index_two = c
                elif temp == 3:
                    temp_index_three = c
                elif temp == 4:
                    temp_index_four = c
        for k in range(46, 2, -1):
            video_poker.deal_player_indexed_card_from_strategy(k)
            for j in range(k-1, 1, -1):
                video_poker.deal_player_indexed_card_from_strategy(j)
                for h in range(j-1, 0, -1):
                    video_poker.deal_player_indexed_card_from_strategy(h)
                    for g in range(h):
                        video_poker.hand_evaluator.erase_hand()
                        video_poker.deal_player_indexed_card_from_strategy(g)
                        payout = float(self.rate_hand_for_payout(hand, payout_table, video_poker))
                        calcs += 1.0
                        video_poker.insert_card_to_deck(temp_index_four, g)
                    video_poker.insert_card_to_deck(temp_index_three, h)
                video_poker.insert_card_to_deck(temp_index_two, j)
            video_poker.insert_card_to_deck(temp_index_one, k)
        average_payout = payout / calcs
        video_poker.player_add_discard_pile()
        # print average_payout
        # print calcs
        return average_payout
