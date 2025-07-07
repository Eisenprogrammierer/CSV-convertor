from abc import ABC, abstractmethod
from typing import Any, List, Dict


class Operation(ABC):
	"""Абстрактный базовый класс для всех операций."""

	@abstractmethod
	def execute(self, data: List[Dict[str, Any]], column: str, value: Any) -> Any:
		"""
		Абстрактная операция.

		:param data: Список входящих данных в виде словврей (строк CSV).
		:param column: Колонка, по которой применяется операция.
		:param value: Значение для операции.
		:return: Результат операции.
		"""
		pass
