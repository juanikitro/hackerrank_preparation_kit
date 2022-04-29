import math
import os
import random
import re
import sys


def timeConversion(s):
    """Convert a time in 24-hour format to 12-hour format.

    Args:
        s (str): time in 12-hour format
    """

    if s[-2:] == 'AM':  # If two last characters are AM
        if s[:2] == '12':  # If two first characters are 12
            # Return 00 + time without the 12 and the last two characters
            return '00' + s[2:-2]
        else:
            # Return the same string without the last two characters
            return s[:-2]
    else:  # If two last characters are PM
        if s[:2] == '12':  # If a two first characters are 12
            # Return the same string without the last two characters
            return s[:-2]
        else:
            # Return the time +12 hours without the last two characters
            return str(int(s[:2]) + 12) + s[2:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
