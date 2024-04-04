# Погружение в Python, Часть 1. Сериализация, Семинар 8, hw8-2
#
# -----------------
# Задача 2:
# Соберите из созданных на уроке и в рамках домашнего задания
# функций пакет для работы с файлами разных форматов.

import json
import csv
from pathlib import Path
from typing import Dict, Any


def write_to_json(data: Dict[str, Any], directory: Path, filename: str) -> None:
    filepath = directory / f"{filename}.json"
    with filepath.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def write_to_csv(data: Dict[str, Any], directory: Path, filename: str) -> None:
    filepath = directory / f"{filename}.csv"
    with filepath.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Path", "Type", "Name", "Size", "Parent Directory"])
        for key, value in data.items():
            writer.writerow(
                [
                    key,
                    value["type"],
                    value["name"],
                    value["size"],
                    value["parent_directory"],
                ]
            )


def calculate_directory_size(directory: Path) -> int:
    return sum(f.stat().st_size for f in directory.glob("**/*") if f.is_file())


def analyze_directory(
    directory: Path, parent_directory: Path = Path("")) -> Dict[str, Any]:
    data = {}
    for item in directory.iterdir():
        item_path = item.resolve()
        if item.is_file():
            data[str(item_path)] = {
                "type": "File",
                "name": item.name,
                "size": item.stat().st_size,
                "parent_directory": str(parent_directory),
            }
        elif item.is_dir():
            data[str(item_path)] = {
                "type": "Directory",
                "name": item.name,
                "size": calculate_directory_size(item_path),
                "parent_directory": str(parent_directory),
            }
            data.update(analyze_directory(item_path, parent_directory=item))
    return data
