import cmath

z = complex(input())
z = cmath.polar(z)

print(*z, sep="\n")
