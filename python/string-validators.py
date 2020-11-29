if __name__ == '__main__':
    s = input()

a = False
for l in s:
    if l.isalnum():
        a = True

b = False
for l in s:
    if l.isalpha():
        b = True

c = False
for l in s:
    if l.isdigit():
        c = True

d = False
for l in s:
    if l.islower():
        d = True

e = False
for l in s:
    if l.isupper():
        e = True

for i in [a, b, c, d, e]:
    print(i)
