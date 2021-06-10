from collections import OrderedDict


def merge_the_tools(string, k):
    n = len(string)
    n_sub = int(n/k)

    for i in range(n_sub):

        # subsegment string
        t = string[i*k: (i+1)*k]

        # distinct subsequence
        ds = ""

        for c in t:
            if c not in ds:
                ds += c
        print(ds)


if __name__ == '__main__':
    string, k = "AABCAAADA", 3
merge_the_tools(string, k)
