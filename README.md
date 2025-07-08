# CSV-convertor
An CLI utility for aggregation and filtration data from .csv files.

# Инструкция по установке и запуску
1. git clone https://github.com/Eisenprogrammierer/CSV-convertor/ && cd csv*
2. python -m venv venv
3. source ./venv/bin/activate
4. pip install -r requirements.txt
5. python main.py

# P. S.
Запуск main.py выведет справочное сообщение с достаточно подробным объяснением, как пользоваться программой. В случае отсутствия .csv файлов для тестирования программы, можно сгенерировать тестовый файл с помощью соответствующего вспомогательного скрипта в корневой директории проекта.
Пример использования:
```bash
python main.py -f test_data.csv --where "rating>4.5" --aggregate "max(price)"
```
