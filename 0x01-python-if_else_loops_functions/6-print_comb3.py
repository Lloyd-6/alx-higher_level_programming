#!/usr/bin/python3
# 6-print_comb3.py

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        if first_digit == 8 and second_digit == 9:
            print("{:02}, {:02}".format(first_digit, second_digit))
        else:
            print("{:02}, {:02}".format(first_digit, second_digit), end=", "
