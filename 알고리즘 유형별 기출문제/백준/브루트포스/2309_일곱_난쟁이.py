from itertools import combinations
arr = []
for i in range(9):
    arr.append(int(input()))

answer = []
for i in combinations(arr, 7):
    if sum(i) == 100:
        answer = list(i)

answer.sort()
for i in answer:
    print(i)