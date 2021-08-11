import sys
input = sys.stdin.readline
N = int(input())
K = int(input())

count = 1
arr = list(map(int, input().split()))
arr.sort()
distance = []
for i in range(1, N):
    if arr[i] != arr[i - 1]:
        distance.append(arr[i] - arr[i - 1])
if not distance:
    print(0)
else:
    distance.sort()
    while count < K:
        distance.pop(-1)
        count += 1
    print(sum(distance))

# 6
# 2
# 1 3 17 11 10 6