n = int(input())
# once an iterator has been exhausted, there nothing left to be iterated over
# iterating it a second time won't yield anything
arr = list(map(int, input().split()))

z = max(arr)

while max(arr) == z:
    arr.remove(max(arr))

# this is bad code
print(max(arr))
