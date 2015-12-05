
class Histogram(object):
    def __init__(self, hist_suite=None, hist_value=None, hist_primitive_results=None):
        self.histo_suite = [0, 0, 0, 0]
        self.histo_value = [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0]
        self.histo_primative_results = {
            'Pair': 0,
            'Trips': 0,
            'Quads': 0,
            'Flush': 0,
            'Straight': 0
        }

    def diagnose_hand(self, hand):
        hand.sort(key=lambda x: x._value, reverse=False)
        for k in range(5):
            self.histo_value[hand[k].get_value()-1] += 1
            self.histo_suite[hand[k].get_suite()] += 1

    def clear_hand(self):
        for k in range(13):
            self.histo_value[k] = 0
        for k in range(4):
            self.histo_suite[k] = 0
        self.histo_primative_results['Pair'] = 0
        self.histo_primative_results['Trips'] = 0
        self.histo_primative_results['Quads'] = 0
        self.histo_primative_results['Straight'] = 0
        self.histo_primative_results['Flush'] = 0
