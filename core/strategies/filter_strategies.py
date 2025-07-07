from abc import ABC, abstractmethod
from typing import Any


class FilterStrategy(ABC):

    @abstractmethod
    def compare(self, cell_value: Any, condition_value: Any) -> bool:
        pass


class GreaterThanStrategy(FilterStrategy):
    def compare(self, cell_value: Any, condition_value: Any) -> bool:
        return float(cell_value) > float(condition_value)


class LessThanStrategy(FilterStrategy):
    def compare(self, cell_value: Any, condition_value: Any) -> bool:
        return float(cell_value) < float(condition_value)


class EqualsStrategy(FilterStrategy):
    def compare(self, cell_value: Any, condition_value: Any) -> bool:
        try:
            return float(cell_value) == float(condition_value)
        except ValueError:
            return str(cell_value) == str(condition_value)
