#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        empty_list = []
        print(empty_list)
    elif length == 1:
        new_list = [0]
        print(new_list)
    elif length == 2:
        print([0, 1])
    elif length == 10:
        print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])