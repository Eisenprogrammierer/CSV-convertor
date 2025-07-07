import csv
from pathlib import Path
from random import uniform, randint


def generate_csv(file_path: str, rows: int = 10):
    """
    Генерирует тестовый CSV-файл с данными о товарах.
    
    :param file_path: Путь для сохранения файла (например, 'test_data.csv')
    :param rows: Количество строк данных (по умолчанию 10)
    """
    headers = ["name", "brand", "price", "rating", "stock"]
    brands = ["Apple", "Samsung", "Xiaomi", "Huawei", "Sony"]
    
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        
        for i in range(1, rows + 1):
            writer.writerow({
                "name": f"Product {i}",
                "brand": brands[randint(0, len(brands)-1)],
                "price": round(uniform(100, 2000), 2),
                "rating": round(uniform(3.5, 5.0), 1),
                "stock": randint(0, 100)
            })
    
    print(f"Сгенерирован тестовый файл: {Path(file_path).absolute()}")


if __name__ == "__main__":
    generate_csv("test_data.csv")
