import sys
input = sys.stdin.readline().rstrip
arr = list(input())
counts = [0] * 4
n = len(arr)
wrong = False

for i in range(n):
    if counts[1] > counts[0]:
        wrong = True
    if counts[2] > counts[1]:
        wrong = True
    if counts[3] > counts[2]:
        wrong = True
    if arr[i] == 'w':
        if counts[1] != counts[2] or counts[2] != counts[3]:
            wrong = True
            continue
        counts[0] += 1
    if arr[i] == 'o':
        if counts[2] != counts[3]:
            wrong = True
            continue
        counts[1] += 1
    if arr[i] == 'l':
        if counts[0] != counts[1]:
            wrong = True
            continue
        counts[2] += 1
    if arr[i] == 'f':
        if counts[0] != counts[1] or counts[1] != counts[2]:
            wrong = True
            continue
        counts[3] += 1
    if counts[0] == counts[1] == counts[2] == counts[3]:
        for i in range(4):
            counts[i] = 0
    if wrong:
        break


a = counts[0]
for i in counts:
    if i != a:
        wrong = True

if wrong:
    print(0)
else:
    print(1)