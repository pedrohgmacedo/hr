if __name__ == '__main__':
    s = input()

a = False
for l in s:
    if l.isalnum():
        a = True
        break

b = False
for l in s:
    if l.isalpha():
        b = True
        break

c = False
for l in s:
    if l.isdigit():
        c = True
        break

d = False
for l in s:
    if l.islower():
        d = True
        break

e = False
for l in s:
    if l.isupper():
        e = True
        break

print(*[a, b, c, d, e], sep="\n")

# for i in [a, b, c, d, e]:
#     print(i)

# print(any(c.isalnum() for c in s))
# print(any(c.isalpha() for c in s))
# print(any(c.isdigit() for c in s))
# print(any(c.islower() for c in s))
# print(any(c.isupper() for c in s))
