#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    prevTrack = 0
    track = 0
    valey = 0
    for i in range(steps):
        if path[i] == "D":
            track = track-1
        if path[i] == "U":
            track = track+1
        if prevTrack == 0 and track == -1:
            valey = valey+1
        prevTrack = track
    return valey


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)
