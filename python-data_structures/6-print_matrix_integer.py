#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                print("{:d}".format(matrix[i][j]), end="")
                if j < len(matrix[0])-1:
                    print(" ", end="")
            print("")
    else:
        print("")
