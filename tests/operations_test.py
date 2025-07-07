import pytest
from core.operations.base import Operation
from core.operations.filter import FilterOperation
from core.operations.aggregate import AggregateOperation


def test_operation_is_abstract():
    with pytest.raises(TypeError):
        Operation()


def test_filter_operation_implements_interface():
    op = FilterOperation()
    assert isinstance(op, Operation)
    assert hasattr(op, "execute")


def test_aggregate_operation_implements_interface():
    op = AggregateOperation()
    assert isinstance(op, Operation)
