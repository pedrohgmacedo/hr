import re
import cmath

inpt = str(input())
_, x, y, *_ = re.split(r"(\S+)([\+\-]\S+)[j|i]", inpt)

x = float(x)
y = float(y)
z = complex(x, y)

print(abs(z))
print(cmath.phase(z))
