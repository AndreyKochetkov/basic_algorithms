"""
Обойти матрицу по спирали
"""

import random as r


def print_quad(matrix, i):
    branch = []
    for column in range(i, len(matrix) - i):
        branch.append(matrix[i][column])
    for line in range(i + 1, len(matrix) - i - 1):
        branch.append(matrix[line][len(matrix) - 1 - i])
    for column in reversed(range(i, len(matrix) - i)):
        branch.append(matrix[len(matrix) - i - 1][column])
    for line in reversed(range(i + 1, len(matrix) - i - 1)):
        branch.append(matrix[line][i])
    if len(matrix) - 2 * i == 1:
        print([branch[0]])
    else:
        print(branch)


def spiral(matrix):
    a = divmod(len(matrix), 2)
    n = a[0]
    if a[1] != 0:
        n += 1
    for i in range(n):
        print_quad(matrix, i)


def main():
    n = int(input())
    matrix = []
    for i in range(n):
        line = [r.randint(1, 20) for i in range(n)]
        matrix.append(line)
    print(matrix)
    print("\n\n ---- \n\n")
    spiral(matrix)

    return 0


if __name__ == "__main__":
    main()
