#!/usr/bin/python3
for first_digit in range(10):
    for second_digit in range(first_digit, 10):
        if first_digit != second_digit:
            current_number = first_digit * 10 + second_digit
            if current_number < 88:
                print('{:02}'.format(current_number), end=', ')
print('89')
