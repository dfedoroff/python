import csv
import json
import user_interface as ui
from datetime import datetime

def log_to_file(entry):
    with open('data_row.csv', 'a') as file:
        file.write(
            f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};{entry[4]};\n')
    with open('data_col.csv', 'a') as file:
        file.write(
            f'{entry[0]}\n{entry[1]}\n{entry[2]}\n{entry[3]}\n{entry[4]}\n\n')    
    print('---> CSV файл сохранен.')

def write_json(database: dict) -> None:
    with open('data.json', 'a', encoding = 'utf-8') as file:
        json.dump(database, file, indent = 4, ensure_ascii = False)
    print('---> JSON файл сохранен.')

def create_json_data(database: list[list]) -> dict:
    data = {}
    for user_data in database:
        user_id = user_data[0]
        user_name = user_data[1]
        user_surname = user_data[3]
        user_phone = user_data[4]
        user_comments = user_data[7]
        data[user_id] = {
            'Имя': user_name,
            'Фамилия': user_surname,
            'Номер телефона': user_phone,
            'Описание': user_comments,
        }
    return data

def reading_file(param):
    b = ui.choose_style()
    if b == 1:
        with open('data_row.csv', 'r') as file:
            for line in file:
                if param in line:
                    print(line)
    if b == 2:
        lst = []
        with open('data_row.csv', 'r') as file:
            for line in file:
                if param in line:
                    lst = line.split(";")
                    print(f'{lst[0]}\n{lst[1]}\n{lst[2]}\n{lst[3]}\n{lst[4]}\n\n')

def read_all_file():
    b = ui.choose_style()
    if b == 1:
        with open('data_row.csv', 'r') as file:
            for line in file:
                print(line)    
    if b == 2:
        with open('data_col.csv', 'r') as file:
            for line in file:
                print(line)
