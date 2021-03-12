def solve(s):
    old = s.split()
    for el in old:
        s = s.replace(el, el.capitalize(), 1)

    return s


s = input()
result = solve(s)
print(result)
