"""
Allows us write multiple algos in separate classes
use them interchangeably

For example - 
Program for sorting algorithms where we can sort using different
strategies - BS, MS, QS etc
"""

from abc import ABC, abstractmethod
import random

# Here, inheriting from ABC enforces that this class acts as an Abstract class
# this in turns means that this classes cant be diretly instantiated
# without this inheritance, there's nothing stopping this class from instantiation
class SortStrategy(ABC):
    # this decorator ensures that any subclass needs to provide its own implementation
    # of the sort method otherwise an error will be raised.
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        print(f"BS {data = }")


class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        print(f"QS {data = }")


class MergeSortStrategy(SortStrategy):
    def sort(self, data):
        print(f"MS {data = }")


class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        self._strategy.sort(data)


if __name__ == "__main__":
    d = range(10, 100)
    data = [random.choice(d) for _ in range(10)]

    bs = Sorter(BubbleSortStrategy())
    qs = Sorter(QuickSortStrategy())

    bs.sort(data)
    qs.sort(data)

"""
bs = BubbleSortStrategy()
TypeError: Can't instantiate abstract class BubbleSortStrategy without an
implementation for abstract method 'sort'
"""