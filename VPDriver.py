from OddsSimulator import OddsSimulator

class VPDriver(object):
    def __init__(self, payout_list, odds_simulator=None):
        self.odds_simulator = OddsSimulator(payout_list)


if __name__ == "__main__":
    print "Welcome to the VPDriver"
    print ""

    print "Please enter Payout Table in this format and press enter:"
    vp_driver = VPDriver(map(int, raw_input("     int int int int int int int int int \n").split()))
    print ""

    print "Please enter card in Hand and press enter:"
    vp_driver.odds_simulator.populate_list_to_object(vp_driver.odds_simulator.video_poker,
                                                     map(int, raw_input("     int int int int int \n").split()))
    print ""

    print "VPDriver Calculating"
    vp_driver.odds_simulator.run_simulation(vp_driver.odds_simulator.video_poker.player.hand)

    """
    vp_driver.odds_simulator.video_poker.player.hand.print_hand()
    vp_driver.odds_simulator.video_poker.dealer.deck.print_deck()
    vp_driver.odds_simulator.video_poker.return_hand_to_deck_indexed(vp_driver.odds_simulator.video_poker.hand_list)
    vp_driver.odds_simulator.video_poker.dealer.deck.print_deck()
    """

    vp_driver.odds_simulator.print_object_info(vp_driver.odds_simulator.payout_table)