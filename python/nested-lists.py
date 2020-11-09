records = []
n = int(input())

for _ in range(n):
    name = str(input())
    score = float(input())
    records.append([name, score])

names = [name for name, score in records]
scores = [score for name, score in records]

m0 = min(scores)

m1 = min([score for score in scores if score > m0])

mins = []
for i in range(n):
    if scores[i] == m1:
        mins.append(names[i])

[print(name) for name in sorted(mins)]
