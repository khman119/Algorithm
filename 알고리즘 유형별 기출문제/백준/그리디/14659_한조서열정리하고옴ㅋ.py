n = int(input())
arr = list(map(int, input().split()))
curMax = arr[0]
counts = [0] * n
for i in range(1, n):
    if curMax < arr[i]:
        curMax = arr[i]
        counts[i] = 0
    else:
        counts[i] = counts[i - 1] + 1
print(max(counts))