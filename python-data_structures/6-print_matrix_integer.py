#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        length = len(matrix)
        for i in range(0, length):
            for j in range(0, length):
                print("{:d}".format(matrix[i][j]), end="")
                if j < length:
                    print(" ", end="")
            print("")
    else:
        print("")
