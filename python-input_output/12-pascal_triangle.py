#!/usr/bin/python3
""" This is the Pascal Triangle module
"""


def pascal_triangle(n):
    """ Return a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        current_row = [1]
        prev_row = triangle[i-1]
        for j in range(1, i+1):
            try:
                current_row.append(prev_row[j-1] + prev_row[j])
            except IndexError:
                current_row.append(1)
        triangle.append(current_row)
    return triangle
