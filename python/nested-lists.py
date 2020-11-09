import numpy as np

records = np.array([]).reshape(0, 2)

for _ in range(int(input())):
    name = str(input())
    score = float(input())
    record = np.array([[name, score]])
    records = np.r_[records, record]

m0 = min(records[:, 1])

m = np.array([x for x in records if x[1] > m0])
m1 = min(m[:, 1])

for name, score in m:
    if score == m1:
        print(name)
