import math
import os
import random
import re
import sys


def countingSort(arr):
    """Counting sort algorithm.

    Args:
        arr (int): arrays of 100 nums > 0

    Returns:
        custom_dict.values: list of cuantity of each num in order exist in arr
    """
    custom_arr = list(range(0, 100))
    custom_dict = dict()

    for x in custom_arr:
        custom_dict[x] = 0

    for x in arr:
        custom_dict[x] += 1

    return list(custom_dict.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
