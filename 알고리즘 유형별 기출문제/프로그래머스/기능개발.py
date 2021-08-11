# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
answer = []
n = len(progresses)
counts = [0] * len(progresses)
for i in range(n):
    while progresses[i] < 100:
        progresses[i] += speeds[i]
        counts[i] += 1

count = 0


for i in range(n):
    if counts[i] == 0:
        continue
    count += 1
    for j in range(i + 1, n):
        if counts[i] < counts[j]:
            break
        if counts[i] >= counts[j]:
            count += 1
            counts[j] = 0
    counts[i] = 0
    answer.append(count)
    count = 0

print(answer)