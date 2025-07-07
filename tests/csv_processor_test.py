import pytest
import csv
import os
from tempfile import NamedTemporaryFile
from core.csv_processor import CSVProcessor
from output.formatter import Formatter


@pytest.fixture
def temp_csv():
    data = [
        {"name": "Product A", "price": "100", "rating": "4.5"},
        {"name": "Product B", "price": "200", "rating": "4.0"}
    ]
    
    with NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        f.flush()
        yield f.name
    os.unlink(f.name)


class TestCSVProcessor:
    def test_read_valid_csv(self, temp_csv):
        """Тест чтения корректного CSV-файла"""
        processor = CSVProcessor(temp_csv)
        assert len(processor.data) == 2
        assert processor.data[0]["name"] == "Product A"
        assert float(processor.data[0]["price"]) == 100.0

    def test_read_nonexistent_file(self):
        """Тест обработки отсутствующего файла"""
        with pytest.raises(FileNotFoundError):
            CSVProcessor("non_existent.csv")

    def test_get_headers(self, temp_csv):
        """Тест получения заголовков"""
        processor = CSVProcessor(temp_csv)
        assert processor.get_headers() == ["name", "price", "rating"]

    def test_filter_data(self, temp_csv):
        """Тест фильтрации данных"""
        processor = CSVProcessor(temp_csv)
        filtered = processor.filter_data("price", ">150")
        assert len(filtered) == 1
        assert filtered[0]["name"] == "Product B"

    def test_aggregate_data(self, temp_csv):
        """Тест агрегации данных"""
        processor = CSVProcessor(temp_csv)
        avg_price = processor.aggregate_data("price", "avg")
        assert avg_price == 150.0

    def test_empty_file(self):
        """Тест пустого CSV-файла"""
        with NamedTemporaryFile(mode="w+", suffix=".csv") as f:
            f.write("name,price\n")
            f.flush()
            processor = CSVProcessor(f.name)
            assert processor.data == []

    def test_invalid_column(self, temp_csv):
        """Тест несуществующей колонки"""
        processor = CSVProcessor(temp_csv)
        with pytest.raises(KeyError):
            processor.filter_data("invalid_col", ">100")
