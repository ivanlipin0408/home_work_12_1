import json
import os
from typing import Any


def read_json_file(json_file: str) -> Any:
    """Функция преобразует json файл в объект питон"""

    if not os.path.isfile(json_file):
        raise FileNotFoundError(f"Файл {json_file} не найден.")
    else:
        with open(json_file, encoding="utf-8") as file:
            python_data = json.load(file)
        if not isinstance(python_data, list) or len(python_data) == 0:
            return []
        else:
            return python_data


json_file = "../data/operations.json"
print(read_json_file(json_file))
