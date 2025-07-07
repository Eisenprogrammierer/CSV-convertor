from abc import ABC, abstractmethod
from typing import List


class AggregateStrategy(ABC):

    @abstractmethod
    def compute(self, values: List[float]) -> float:
        pass


class AvgStrategy(AggregateStrategy):
    def compute(self, values: List[float]) -> float:
        return sum(values) / len(values)


class MinStrategy(AggregateStrategy):
    def compute(self, values: List[float]) -> float:
        return min(values)


class MaxStrategy(AggregateStrategy):
    def compute(self, values: List[float]) -> float:
        return max(values)
