# Знакомство с языком Python, Семинар 1, hw1-3
#
# -----------------
# Задача 3:
# Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси
# она находится).
# 
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input("Введите значение X: "))
y = int(input("Введите значение Y: "))
if x > 0 and y > 0:
    print(f'Точка с координатами ({x}; {y}) в I четверти.')
elif x < 0 and y > 0:
    print(f'Точка с координатами ({x}; {y}) в II четверти.')
elif x < 0 and y < 0:
    print(f'Точка с координатами ({x}; {y}) в III четверти.')
elif x > 0 and y < 0:
    print(f'Точка с координатами ({x}; {y}) в IV четверти.')
else:
    print(f'Точка с координатами ({x}; {y}) находится на оси, а не в четверти.')