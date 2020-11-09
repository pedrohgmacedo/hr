n = int(input())
arr = list(map(int, input().split()))

# there are 2 maxes
m = max([x for x in arr if x < max(arr)])

# this is bad code
print(m)
