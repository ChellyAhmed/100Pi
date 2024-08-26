#!/bin/python3
from test_PI import test_PI

def leibniz():

    running_sum = 1
    next_denominator = 3
    sign = -1

    while True:
        running_sum += 1 / (sign * next_denominator)
        next_denominator = next_denominator + 2
        sign *= -1

        print(running_sum * 4)
        try:
            test_PI(running_sum * 4)
            return running_sum * 4
        except AssertionError:
            continue

leibniz()
