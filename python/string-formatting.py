n = int(input())


def print_formatted(n):
    for k in range(1, n+1):
        width = len("{:b}".format(n))
        print("{0:>{w}} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(k, w=width))


print_formatted(n)
