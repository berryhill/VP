from Strategy import Strategy
import time


class TakeFive(Strategy):
    def __init__(self, holds):
        super(TakeFive, self).__init__("Take Five", holds)

    def get_payout_from_strategy(self, hand, payout_table, video_poker):
        start = time.clock()
        payout = 0.0
        calcs = 0.0
        video_poker.player.add_holds(self.get_holds())
        video_poker.player_submit_play()
        temp = 0
        temp_index_one = 0
        temp_index_two = 0
        temp_index_three = 0
        temp_index_four = 0
        temp_index_five = 0
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
                elif temp == 5:
                    temp_index_five = c
        for k in range(45, 3, -1):
            video_poker.deal_player_indexed_card_from_strategy(k)
            for j in range(k-1, 2, -1):
                video_poker.deal_player_indexed_card_from_strategy(j)
                for h in range(j-1, 1, -1):
                    video_poker.deal_player_indexed_card_from_strategy(h)
                    for g in range(h-1, 0, -1):
                        video_poker.deal_player_indexed_card_from_strategy(g)
                        for f in range(g):
                            video_poker.hand_evaluator.erase_hand()
                            video_poker.deal_player_indexed_card_from_strategy(f)
                            payout = float(self.rate_hand_for_payout(hand, payout_table, video_poker))
                            calcs += 1.0
                            video_poker.insert_card_to_deck(temp_index_five, f)
                        video_poker.insert_card_to_deck(temp_index_four, g)
                    video_poker.insert_card_to_deck(temp_index_three, h)
                video_poker.insert_card_to_deck(temp_index_two, j)
            video_poker.insert_card_to_deck(temp_index_one, k)
        video_poker.player_add_discard_pile()
        elapsed_time = time.clock() - start
        print "Time Taken TakeFive= %f" % elapsed_time
        # print average_payout
        # print calcs
        return payout / calcs