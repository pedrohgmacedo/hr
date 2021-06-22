import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.


def flatlandSpaceStations(n, stations):
    # sorts stations
    ls = len(stations)
    stations = sorted(stations)
    # since we start at city 0, then the distance is that of the nearest  (sorted) stations
    # assume our solution is the distance from city 0 to station 0
    res = stations[0]

    # then, the result is either that, or the largest midpoint between two stations
    for ind in range(1, ls):
        res = max(res, (stations[ind] - stations[ind-1])//2)

    # or, it's the distance from the last city to the last station
    res = max(res, n-1 - stations[-1])

    return res


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    print(flatlandSpaceStations(n, c))
