from Strategy import Strategy
import time

class TakeTwo(Strategy):
    def __init__(self, holds):
        super(TakeTwo, self).__init__("Take Two", holds)

    def get_payout_from_strategy(self, hand, payout_table, video_poker):
        start = time.clock()
        payout = 0.0
        calcs = 0.0
        video_poker.player.add_holds(self.get_holds())
        video_poker.player_submit_play()
        temp = 0
        temp_index_one = 0
        temp_index_two = 0
        for c in range(5):
            if self.get_holds()[c] == 0:
                temp += 1
                if temp == 1:
                    temp_index_one = c
                elif temp == 2:
                    temp_index_two = c
        for k in range(46, 0, -1):
            video_poker.deal_player_indexed_card_from_strategy(k)
            for j in range(k):
                video_poker.hand_evaluator.erase_hand()
                video_poker.deal_player_indexed_card_from_strategy(j)
                payout = float(self.rate_hand_for_payout(hand, payout_table, video_poker))
                calcs += 1.0
                video_poker.insert_card_to_deck(temp_index_two, j)
            video_poker.insert_card_to_deck(temp_index_one, k)
        video_poker.player_add_discard_pile()
        elapsed_time = time.clock() - start
        print "Time Taken TakeTwo = %f" % elapsed_time
        # print average_payout
        # print calcs
        return payout / calcs
