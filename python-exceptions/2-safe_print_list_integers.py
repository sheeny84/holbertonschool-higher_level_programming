#!/usr/bin/python3
from safe_print_integer import safe_print_integer
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (TypeError, ValueError):
                pass
    except IndexError:
        pass
    print()
    return count
