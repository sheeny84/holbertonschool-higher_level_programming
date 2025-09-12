#!/usr/bin/python3
"""
This is the "maxtrix_divided" module.

The maxtrix_divided module supplies one function,
maxtrix_divided().  For example,

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix which is the result of the first matrix divided by div
    """
    if not matrix or not div:
        raise ValueError("matrix and div must be provided")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    # Matrix must be a list of integers or floats
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    new_matrix = [[round(x/div, 2) for x in row] for row in matrix]
    return new_matrix
