from typing import List, Dict, Any
from core.operations.base import Operation
from core.strategies.filter_strategies import *


class FilterOperation(Operation):
	"""Фильтрация данных по условию."""

	def execute(self, data: List[Dict[str, Any]], column: str, condition: str) -> List[Dict[str, Any]]:
        	operator, val = self._parse_condition(condition)
        	strategy = self._get_strategy(operator)
        	return [row for row in data if strategy.compare(row[column], val)]


	def _parse_condition(self, condition: str) -> tuple[str, Any]:
        	"""Разбирает условие на оператор и значение."""
        	for op in (">", "<", "="):
            		if op in condition:
                		return op, condition.split(op)[1]
        	raise ValueError(f"Invalid condition: {condition}")


	def _get_strategy(self, operator : str) -> FilterStrategy:
		if operator == ">":
			return GreaterThanStrategy()
		elif operator == "<":
			return LessThanStrategy()
		elif operator == "=":
			return EqualsStrategy()
		raise ValueError(f"Unknown operator: {operator}")
