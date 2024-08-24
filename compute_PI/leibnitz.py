#!/bin/python3

def main():

    running_sum = 1
    next_denominator = 3
    sign = -1

    while True:
        running_sum += 1 / (sign * next_denominator)
        next_denominator = next_denominator + 2
        sign *= -1

        print(running_sum * 4)

if __name__ == "__main__": main()
