import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    """Absolute difference between square matriz diagonal sums

    Args:
        arr (integer array): a square matriz
        n (int): the size of the matriz

    Returns:
        int: the absolute difference between the two diagonals
    """

    arr2 = arr[::-1]
    fst_diag = 0
    snd_diag = 0

    for i in range(n):
        fst_diag += arr[i][i]
        snd_diag += arr2[i][i]

    return abs(fst_diag - snd_diag)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
