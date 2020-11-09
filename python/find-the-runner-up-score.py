n = int(input())
# once an iterator has been exhausted, there nothing left to be iterated over
# iterating it a second time won't yield anything
arr = list(map(int, input().split()))

runnerUp = [item for item in list(arr) if item < max(list(arr))]

# this is bad code
print(max(runnerUp))
