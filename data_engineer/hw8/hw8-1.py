# Погружение в Python, Часть 1. Сериализация, Семинар 8, hw8-1
#
# -----------------
# Задача 1:
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните
# в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
import os


def write_to_json(data, directory, filename):
    filepath = os.path.join(directory, f"{filename}.json")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def write_to_csv(data, directory, filename):
    filepath = os.path.join(directory, f"{filename}.csv")
    with open(filepath, "w", encoding="utf-8", newline="") as file:
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


def write_to_pickle(data, directory, filename):
    filepath = os.path.join(directory, f"{filename}.pickle")
    with open(filepath, "wb") as file:
        pickle.dump(data, file)


def calculate_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        total_size += sum(os.path.getsize(os.path.join(root, name)) for name in files)
    return total_size


def analyze_directory(directory, parent_directory=""):
    data = {}
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            data[item_path] = {
                "type": "File",
                "name": item,
                "size": os.path.getsize(item_path),
                "parent_directory": parent_directory,
            }
        elif os.path.isdir(item_path):
            data[item_path] = {
                "type": "Directory",
                "name": item,
                "size": calculate_directory_size(item_path),
                "parent_directory": parent_directory,
            }
            data.update(analyze_directory(item_path, parent_directory=item))
    return data
