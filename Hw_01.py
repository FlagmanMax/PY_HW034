# Hw_01
# Напишите функцию для транспонирования матрицы

from random import randint

MAX_VALUE = 10


def matrix_create(m: int, n: int):
    matrix = [[randint(1, MAX_VALUE) for j in range(n)] for i in range(m)]
    return matrix

def matrix_print(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

def matrix_print_(matrix):
    for row in matrix:
        print(*row)
    print()


def matrix_transpose(matrix):
    # matrix_t = []
    matrix_t = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # for i in matrix:
    #     for j in i:
    #         matrix_t[j][i] = matrix[i][j]
    return matrix_t

m = int(input("Введите размер матрицы  m: "))
n = int(input("Введите размер матрицы  n: "))

matrix = matrix_create(m, n)
matrix_print_(matrix)

matrix_transpose = matrix_transpose(matrix)
matrix_print_(matrix_transpose)
