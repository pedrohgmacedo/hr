from collections import OrderedDict


def merge_the_tools(string, k):
    l = len(string)
    for i in range(0, l, k):
        # a dict has unique keys
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))


if __name__ == '__main__':
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)
