# Погружение в Python, Часть 1. Модули, Семинар 6, hw6-1
#
# -----------------
# Задача 1:
# В модуль с проверкой даты добавьте возможность запуска
# в терминале с передачей даты на проверку.

import sys
from datetime import datetime


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split("."))
        datetime(year, month, day)
        if is_leap_year(year):
            leap_year_msg = "Високосный год."
        else:
            leap_year_msg = "Не високосный год."
    except ValueError:
        return "Дата заполнена некорректно."

    if month == 2:
        if is_leap_year(year):
            return (
                "Дата корректна. " + leap_year_msg
                if 1 <= day <= 29
                else "Дата заполнена некорректно."
            )
        else:
            return (
                "Дата корректна. " + leap_year_msg
                if 1 <= day <= 28
                else "Дата заполнена некорректно."
            )
    elif month in [4, 6, 9, 11]:
        return (
            "Дата корректна. " + leap_year_msg
            if 1 <= day <= 30
            else "Дата заполнена некорректно."
        )
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return (
            "Дата корректна. " + leap_year_msg
            if 1 <= day <= 31
            else "Дата заполнена некорректно."
        )
    return "Дата заполнена некорректно."


def main():
    if len(sys.argv) == 2:
        print(is_valid_date(sys.argv[1]))
    else:
        print("Дата для проверки не указана.")


if __name__ == "__main__":
    main()
