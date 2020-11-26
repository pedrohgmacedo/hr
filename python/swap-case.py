import string


def swap_case(s):
    swapped = ""
    for letter in s:
        if letter == letter.upper():
            swapped += letter.lower()
        else:
            swapped += letter.upper()
    return swapped


s = input()
result = swap_case(s)
# result = s.swapcase()
print(result)
