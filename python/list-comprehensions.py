x = int(input())
y = int(input())
z = int(input())
n = int(input())

fullList = [[i, j, k]
            for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1)]

constrainedList = [C for C in fullList if sum(C) != n]

print(constrainedList)
