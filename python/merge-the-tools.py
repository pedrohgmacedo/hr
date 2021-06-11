import time
import string
import random
from collections import OrderedDict


def merge_the_tools(string, k):
    n = len(string)
    n_sub = int(n/k)
    l = []
    for i in range(n_sub):
        # subsegment string
        t = string[i*k:(i+1)*k]

        # distinct subsequence
        ds = ""
        for c in t:
            if c not in ds:
                ds += c
        l.append([ds])
    return l


def merge_the_tools_dict(string, k):
    n = len(string)
    n_sub = int(n/k)
    l = []

    for i in range(n_sub):
        t = string[i*k:(i+1)*k]

        l.append([''.join(OrderedDict.fromkeys(t).keys())])
    return l


string, k = ''.join([random.choice(string.ascii_uppercase)
                     for i in range(100*1000000)]), 100
t = time.time()
a = merge_the_tools(string, k)
elapsed = time.time() - t
t2 = time.time()
b = merge_the_tools_dict(string, k)
elapsed2 = time.time() - t2
print(a == b)
print(elapsed, elapsed2)
