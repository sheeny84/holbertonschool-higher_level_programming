#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        return 0
    else:
        try:
            for i in range(0, x):
                print("{}".format(my_list[i]), end="")
        except IndexError:
            print("")
            return i
        print("")
        return i + 1
