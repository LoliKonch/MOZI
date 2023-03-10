import numpy as np

input_message = "алексей и владимир учатся в университете ъ"
input_message = input_message.replace(" ", "")
letter_list = list(input_message)

counter = 0
matrix_scheme = np.array([[0, 0, 1, 0, 0, 0],
                          [1, 0, 0, 0, 0, 1],
                          [0, 1, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 1, 0, 0],
                          [0, 0, 1, 0, 0, 1]])

table = [[' ' for k in range(6)] for i in  range(6)]

def write_and_traspose(matrix_scheme, counter, table):
    for i in range(6):
        for j in range(6):
            if matrix_scheme[i][j]:
                table[i][j] = letter_list[counter]
                counter += 1

    trasposed_matrix = matrix_scheme.transpose()
    for i in range(6):
        trasposed_matrix[i] = np.flip(trasposed_matrix[i])

    for i in range(6):
        for j in range(6):
            print(table[i][j], end='')
        print("")
    print("\n")

    return trasposed_matrix, counter, table

for i in range(4):
    matrix_scheme, counter, table = write_and_traspose(matrix_scheme, counter, table)

for i in table:
    print(i)