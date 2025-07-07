from core.operations.filter import FilterOperation
from core.operations.aggregate import AggregateOperation


class OperationFactory:
    	"""Создаёт экземпляр конкретной операции."""

	@staticmethod
    	def create(op_type: str) -> Operation:
		if op_type == "filter":
            		return FilterOperation()
        	elif op_type == "aggregate":
            		return AggregateOperation()
        	raise ValueError(f"Unknown operation type: {op_type}")
