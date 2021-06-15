# Complete the maxSubsetSum function below.
# mistery dp function
def maxSubsetSum(arr):
    n = len(arr)
    maxes = {0: arr[0],
             1: max(arr[0], arr[1])}

    for i in range(2, n):
        maxes[i] = max(
            arr[i],
            maxes[i-1],
            maxes[i-2]+arr[i]
        )

    return maxes[n-1]


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(maxSubsetSum(arr))
