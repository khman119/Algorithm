import sys
input = sys.stdin.readline
N = int(input())
arr = []
day = 0
for i in range(N):
    d, w = map(int, input().split())
    day = max(d, day)
    arr.append([d, w])
arr.sort(key=lambda x: x[0], reverse=True)
answer = 0
temp = 0

while day > 0:
    score = 0
    for i in range(N):
        if day <= arr[i][0]:
            score = max(score, arr[i][1])
    for i in range(N):
        if score == arr[i][1] and arr[i][0] != -1:
            arr[i][0] = -1
            break
    answer += score
    day -= 1

print(answer)
# 4
# 9 9
# 9 9
# 9 9
# 1 10