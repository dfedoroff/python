# Знакомство с языком Python, Семинар 1, hw1-4
#
# -----------------
# Задача 4:
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти
# (x и y).

q = int(input('Введите номер четверти от 1 до 4: '))
if q == 1:
     print('Диапазон координат точек в I четверти (x>0; y>0)')
elif q == 2:
     print('Диапазон координат точек в II четверти (x<0; y>0)')
elif q == 3:
     print('Диапазон координат точек в III четверти (x<0; y<0)')
elif q == 4:
     print('Диапазон координат точек в IV четверти (x>0; y<0)')
else:
     print('Повторите ввод. Введите номер четверти от 1 до 4.')