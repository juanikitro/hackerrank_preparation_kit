#!/bin/python3

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    """Find the lonely integer in an array of integers.

    Args:
        a (int): an array of integers

    Returns:
        int: the length of the array
        int: the lonely integer
    """
    # Create a dictionary with the numbers as keys and the number of times
    # they appear as values.
    d = {}
    for num in a:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    # Return the key with the value of 1.
    for key in d:
        if d[key] == 1:
            return key


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
