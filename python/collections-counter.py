from collections import Counter

x = int(input())
sizes = Counter(list(map(int, input().split())))
n = int(input())
p = 0

for i in range(n):
    k, v = list(map(int, input().split()))
    if sizes[k] > 0:
        sizes[k] -= 1
        p += v


print(p)
