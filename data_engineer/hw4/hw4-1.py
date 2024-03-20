# Погружение в Python, Часть 1. Функции, Семинар 4, hw4-1
#
# -----------------
# Задача 1:
# Напишите функцию для транспонирования матрицы.

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


def print_matrix(matrix):
    for row in matrix:
        print("\t".join(str(element) for element in row))


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Исходная матрица:")
    print_matrix(matrix)
    print("\nТранспонированная матрица:")
    transposed_matrix = transpose_matrix(matrix)
    print_matrix(transposed_matrix)


if __name__ == "__main__":
    main()
