# Знакомство с языком Python, Семинар 1, hw1-2
#
# -----------------
# Задача 2:
# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Вариант 1:
# x = int(input('Введите 0 или 1 для X: '))
# y = int(input('Введите 0 или 1 для Y: '))
# z = int(input('Введите 0 или 1 для Z: '))
# if (x not in range(2)) or (y not in range(2)) or (z not in range(2)):
#     print('Повторите ввод. Введите 0 или 1.')
# else:
#     print('Проверка истинности:', not (x or y or z) == (not x and not y and not z))

# Вариант 2:
check = range(2)
for x in check:
    for y in check:
        for z in check:
            print(x, y, z)
            print(not(x or y or z) == (not x and not y and not z))