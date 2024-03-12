# Погружение в Python, Часть 1. Простые типы данных, Семинар 1, hw2-1
#
# -----------------
# Задача 1:
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

def get_number_input():
    while True:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")


def integer_to_hex(number):
    if number == 0:
        return "0x0"
    hex_chars = "0123456789abcdef"
    hex_string = ""
    while number > 0:
        hex_string = hex_chars[number % 16] + hex_string
        number //= 16
    return "0x" + hex_string
