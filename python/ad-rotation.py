#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'changeAds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER base10 as parameter.
#

def changeAds(base10):
    n = math.ceil(math.log2(base10))
    mask = 2**n-1
    if mask == base10-1:
        return mask
    return base10 ^ mask


if __name__ == '__main__':

    # base10 = int(input().strip())
    base10 = int(65536)

    result = changeAds(base10)
    print(result)
