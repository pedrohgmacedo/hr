# n, m = list(map(int, input().split()))

# dick = ".|."
# dash = "-"
# wel = "WELCOME"

# middle = int((m-7)/2)*dash+wel+int((m-7)/2)*dash

# # k is the number of iterations on each half without the welcome
# for k in range(int((n - 1) / 2)):
#     # p is the num of dicks
#     p = (2 * k + 1)
#     # l is the number of dashes before dicks
#     l = int((m-3*p)/2)
#     print(l * dash + (p) * dick + l * dash)

# print(middle)

# for k in range(int((n - 1) / 2)-1, -1, -1):
#     p = (2*k+1)
#     l = int((m-3*p)/2)
#     print(l*dash+(p)*dick+l*dash)

N, M = map(int, raw_input().split())
for i in xrange(1, N, 2):
    print(str('.|.')*i).center(M, '-')
print str('WELCOME').center(M, '-')
for i in xrange(N-2, -1, -2):
    print(str('.|.')*i).center(M, '-')
