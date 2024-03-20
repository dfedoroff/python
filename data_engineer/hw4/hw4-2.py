# Погружение в Python, Часть 1. Функции, Семинар 4, hw4-2
#
# -----------------
# Задача 2:
# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте его
# строковое представление.

def invert_key_value(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[str(value)] = key
    return result


def main():
    data = invert_key_value(students=["Иван", "Маша"], group_friends={1: "Алексей", 2: "Елена", 3: "Николай"})
    print(data)


if __name__ == "__main__":
    main()
