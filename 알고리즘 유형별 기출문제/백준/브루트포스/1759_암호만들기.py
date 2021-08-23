from copy import deepcopy
from itertools import combinations

l, c = map(int, input().split())
arr = list(input().split())
ja = []
mo = []
result = []
for i in range(c):
    if arr[i] == 'a' or arr[i] == 'e' or arr[i] == 'i' or arr[i] == 'o' or arr[i] == 'u':
        mo.append(arr[i])
    else:
        ja.append(arr[i])

answer = []
for i in range(1, l - 1):
    for j in combinations(mo, i):
        temp = list(j)
        for k in combinations(ja, l - i):
            result = deepcopy(temp)
            result += list(k)
            result.sort()
            answer.append("".join(result))

answer.sort()
for i in answer:
    print(i)
