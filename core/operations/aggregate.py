from typing import List, Dict, Any
from core.operations.base import Operation
from core.strategies.aggregate_strategies import *


class AggregateOperation(Operation):
	"""Агрегация данных (avg, min, max)."""

	def execute(self, data: List[Dict[str, Any]], column: str, func: str) -> float:
		values = [float(row[column]) for row in data]
		strategy = self._get_strategy(func)
		return strategy.compute(values)

	def _get_strategy(self, func: str) -> AggregateStrategy:
		if func == "avg":
			return AvgStrategy()
		elif func == "min":
			return MinStrategy()
		elif func == "max":
			return MaxStrategy()
		raise ValueError(f"Unsupported function: {func}")
