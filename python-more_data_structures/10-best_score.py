#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        max_key = None
    else:
        max_key = next(iter(a_dictionary))
        max_val = a_dictionary[max_key]
        for k, v in a_dictionary.items():
            if v > max_val:
                max_val = v
                max_key = k
    return max_key
