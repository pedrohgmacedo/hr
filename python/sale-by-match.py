#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, socks):
    counter = 0
    while socks:
        sock = socks.pop(0)
        if (sock in socks):
            socks.pop(socks.index(sock))
            counter = counter + 1
    return counter


if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
