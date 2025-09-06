#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    print("{} ".format(length-1), end="")
    if length == 1:
        print("arguments.")
    elif length == 2:
        print("argument:")
    else:
        print("arguments:")
    if length > 1:
        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
