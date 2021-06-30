import sys
n, k = map(int, input().split())
num = list(map(int, sys.stdin.readline().rstrip()))
q = []
result = []
delNum = k
for i in range(n):
    while delNum > 0 and result:
        if result[len(result) - 1] < num[i]:
            result.pop()
            delNum -= 1
        else:
            break
    result.append(num[i])
    print(result, delNum)

for i in range(n - k):
    print(result[i], end='')
