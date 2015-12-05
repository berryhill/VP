from TakeZero import TakeZero
from TakeOne import TakeOne
from TakeTwo import TakeTwo
from TakeThree import TakeThree
from TakeFour import TakeFour
from TakeFive import TakeFive


class Strategies(list):
    def __init__(self, _top_strategy=None):
        super(Strategies, self).__init__()
        self._populate_strategies()

    def set_top_strategy(self, strategy):
        self._top_strategy = strategy

    def get_top_strategy(self):
        return self._top_strategy

    def _populate_strategies(self):
        self.append(TakeZero([1, 1, 1, 1, 1]))

        self.append(TakeOne([1, 1, 1, 1, 0]))
        self.append(TakeOne([1, 1, 1, 0, 1]))
        self.append(TakeOne([1, 1, 0, 1, 1]))
        self.append(TakeOne([1, 0, 1, 1, 1]))
        self.append(TakeOne([0, 1, 1, 1, 1]))

        self.append(TakeTwo([1, 1, 1, 0, 0]))
        self.append(TakeTwo([1, 1, 0, 1, 0]))
        self.append(TakeTwo([1, 1, 0, 0, 1]))
        self.append(TakeTwo([1, 0, 1, 1, 0]))
        self.append(TakeTwo([1, 0, 1, 0, 1]))
        self.append(TakeTwo([1, 0, 0, 1, 1]))
        self.append(TakeTwo([0, 1, 1, 1, 0]))
        self.append(TakeTwo([0, 1, 1, 0, 1]))
        self.append(TakeTwo([0, 1, 0, 1, 1]))
        self.append(TakeTwo([0, 0, 1, 1, 1]))

        self.append(TakeThree([1, 1, 0, 0, 0]))
        self.append(TakeThree([1, 0, 1, 0, 0]))
        self.append(TakeThree([1, 0, 0, 1, 0]))
        self.append(TakeThree([1, 0, 0, 0, 1]))
        self.append(TakeThree([0, 1, 1, 0, 0]))
        self.append(TakeThree([0, 1, 0, 1, 0]))
        self.append(TakeThree([0, 1, 0, 0, 1]))
        self.append(TakeThree([0, 0, 1, 1, 0]))
        self.append(TakeThree([0, 0, 1, 0, 1]))
        self.append(TakeThree([0, 0, 0, 1, 1]))

        self.append(TakeFour([1, 0, 0, 0, 0]))
        self.append(TakeFour([0, 1, 0, 0, 0]))
        self.append(TakeFour([0, 0, 1, 0, 0]))
        self.append(TakeFour([0, 0, 0, 1, 0]))
        self.append(TakeFour([0, 0, 0, 0, 1]))

        self.append(TakeFive([0, 0, 0, 0, 0]))





