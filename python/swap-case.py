import string


def swap_case(s):
    swapped = []
    for el in s:
        if el.isupper():
            swapped.append(el.lower())
        elif el.islower():
            swapped.append(el.upper())
        else:
            swapped.append(el)
    return "".join(swapped)


s = input()
result = swap_case(s)
result = s.swapcase()
print(result)
