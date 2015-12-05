

class Eval(object):
    def __init__(self, _eval_value):
        self._eval_value = _eval_value

    def get_eval_value(self):
        return self._eval_value

    def print_eval_value(self):
        print "%s" % self._eval_value


class EvalRoyalFlush(Eval):
    def __init__(self):
        super(EvalRoyalFlush, self).__init__("RoyalFlush")

    def evaluate(self, hand, histo):
        pass


class StraightFlush(Eval):
    def __init__(self):
        super(StraightFlush, self).__init__("StraightFlush")

    def evaluate(self, hand, histo):
        pass


class Quads(Eval):
    def __init__(self):
        super(Quads, self).__init__("Quads")

    def evaluate(self, hand, histo):
        pass


class FullHouse(Eval):
    def __init__(self):
        super(FullHouse, self).__init__("FullHouse")

    def evaluate(self, hand, histo):
        pass


class Straight(Eval):
    def __init__(self):
        super(Straight, self).__init__("Straight")

    def evaluate(self, hand, histo):
        pass


class Flush(Eval):
    def __init__(self):
        super(Flush, self).__init__("Flush")

    def evaluate(self, hand, histo):
        pass


class Trips(Eval):
    def __init__(self):
        super(Quads, self).__init__("Trips")

    def evaluate(self, hand, histo):
        pass


class TwoPair(Eval):
    def __init__(self):
        super(TwoPair, self).__init__("TwoPair")

    def evaluate(self, hand, histo):
        pass


class EvalPair(Eval):
    def __init__(self):
        super(EvalPair, self).__init__("Pair")

    def evaluate(self, hand, histo):
        pass