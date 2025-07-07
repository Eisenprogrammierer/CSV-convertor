from tabulate import tabulate
from typing import List, Dict, Any, Union


class Formatter:
    """Форматирует данные для вывода в консоль."""

    @staticmethod
    def format_table(data: List[Dict[str, Any]]) -> str:
        """
        Форматирует список словарей в таблицу.
        
        :param data: Данные для форматирования (например, результат фильтрации)
        :return: Отформатированная строка таблицы
        """
        if not data:
            return "No data to display"
        
        headers = list(data[0].keys())
        rows = [list(row.values()) for row in data]
        
        return tabulate(rows, headers=headers, tablefmt="grid")


    @staticmethod
    def format_aggregation(operation: str, column: str, result: Union[float, int, str]) -> str:
        """
        Форматирует результат агрегации.
        
        :param operation: Тип операции (avg, min, max)
        :param column: Колонка, по которой проводилась агрегация
        :param result: Результат вычисления
        :return: Отформатированная строка результата
        """
        operation_names = {
            "avg": "Average",
            "min": "Minimum",
            "max": "Maximum"
        }
        name = operation_names.get(operation, operation.capitalize())
        return f"{name} value for '{column}': {result:.2f}" if isinstance(result, float) else f"{name} value for '{column}': {result}"


    @staticmethod
    def format_error(message: str) -> str:
        """
        Форматирует сообщение об ошибке.
        
        :param message: Текст ошибки
        :return: Отформатированное сообщение об ошибке
        """
        return f"Error: {message}"
