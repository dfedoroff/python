# Погружение в Python, Часть 1. Простые типы данных, Семинар 1, hw2-2
#
# -----------------
# Задача 2:
# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction


def get_fraction_input(prompt):
    while True:
        try:
            fraction_str = input(prompt)
            numerator, denominator = map(int, fraction_str.split("/"))
            if denominator == 0:
                raise ValueError("Знаменатель не может быть равен нулю.")
            return Fraction(numerator, denominator)
        except ValueError:
            print("Пожалуйста, введите дробь в формате 'a/b', где a и b - целые числа.")
