import csv
from typing import List, Dict, Any
from core.operations.filter import FilterOperation
from core.operations.aggregate import AggregateOperation


class CSVProcessor:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self._read_csv()


    def _read_csv(self) -> List[Dict[str, Any]]:
        """Читает CSV-файл и возвращает данные в виде списка словарей."""
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]


    def filter_data(self, column: str, condition: str) -> List[Dict[str, Any]]:
        """Фильтрует данные по условию (>, <, =)."""
        filter_op = FilterOperation()
        return filter_op.execute(self.data, column, condition)


    def aggregate_data(self, column: str, func: str) -> float:
        """Вычисляет агрегацию (avg, min, max) по указанной колонке."""
        aggregate_op = AggregateOperation()
        return aggregate_op.execute(self.data, column, func)


    def get_headers(self) -> List[str]:
        """Возвращает заголовки CSV-файла."""
        return list(self.data[0].keys()) if self.data else []
