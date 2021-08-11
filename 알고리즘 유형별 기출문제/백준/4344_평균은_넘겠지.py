C = int(input())
arr = []
avg = 0
count = 0
for i in range(C):
    count = 0
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    avg = sum(arr) / len(arr)
    for j in range(N):
        if arr[j] > avg:
            count += 1
    percent = 100 * count / N
    print(f'{percent:.3f}%')