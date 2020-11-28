#!/usr/bin/env python3
# Created by: Roman Cernetchi
# Created on: November 2020
# This program calculates the total of 2 numbers

import math


def main():
    # This function calculates the total of 2 numbers

    # Input
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # process
    total = a + b

    # Output
    print("")
    print("Total of both numbers is {}".format(total))


if __name__ == "__main__":
    main()
