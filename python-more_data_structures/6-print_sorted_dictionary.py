#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary)
    for k in sorted_list:
        print(f"{k}: {a_dictionary[k]}")
