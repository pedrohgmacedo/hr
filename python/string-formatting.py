n = int(input())


def print_formatted(n):
    for k in range(1, n+1):
        l = len("{:b}".format(n))
        print("{:>{l}} {:>{l}o} {:>{l}X} {:>{l}b}".format(k, k, k, k, l=l))


print_formatted(n)
