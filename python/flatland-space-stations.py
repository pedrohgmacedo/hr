import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.


def flatlandSpaceStations(n, c):
    max_dist = 0
    for i in range(n):
        max_inner_city = min([abs(k-i) for k in c])
        if max_inner_city > max_dist:
            max_dist = max_inner_city
    return max_dist


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    print(flatlandSpaceStations(n, c))
