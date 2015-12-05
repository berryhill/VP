
class Card(object):
    def __init__(self, suite, value):
        self._suite = suite
        self._value = value

    def get_suite(self):
        return self._suite

    def get_value(self):
        return self._value
