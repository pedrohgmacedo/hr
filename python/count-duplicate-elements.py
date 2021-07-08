#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countDuplicate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def countDuplicate(numbers):
    n = len(numbers)
    counter = 0
    dupes = []
    for i in range(0, n):
        if numbers[i] in numbers[i+1:] and numbers[i] not in dupes:
            dupes.append(numbers[i])
            counter += 1
    return counter


if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = countDuplicate(numbers)

    print(result)
