import pytest
from core.strategies.filter_strategies import *
from core.strategies.aggregate_strategies import *


@pytest.fixture
def sample_data() -> list[dict[str, float]]:
    return [
        {"price": 100, "rating": 4.5},
        {"price": 200, "rating": 4.0},
        {"price": 300, "rating": 5.0}
    ]


class TestFilterStrategies:
    @pytest.mark.parametrize("strategy,value,expected", [
        (GreaterThanStrategy(), 150, [200, 300]),
        (LessThanStrategy(), 250, [100, 200]),
        (EqualsStrategy(), 200, [200])
    ])
    def test_filter_strategies(self, strategy, value, expected):
        result = strategy.compare(200, value)
        if isinstance(strategy, EqualsStrategy):
            assert result == (200 == value)
        else:
            assert result == (200 in expected)


class TestAggregateStrategies:
    @pytest.mark.parametrize("strategy,expected", [
        (AvgStrategy(), 200.0),
        (MinStrategy(), 100.0),
        (MaxStrategy(), 300.0)
    ])
    def test_aggregate_strategies(self, strategy, expected, sample_data):
        values = [row["price"] for row in sample_data]
        result = strategy.compute(values)
        assert result == expected


class TestStrategyErrors:
    def test_equals_strategy_with_different_types(self):
        strategy = EqualsStrategy()
        assert strategy.compare("123", 123) is True
        assert strategy.compare("abc", "abc") is True
        assert strategy.compare(10.5, "10.5") is True

    def test_empty_aggregate(self):
        with pytest.raises(ZeroDivisionError):
            AvgStrategy().compute([])
