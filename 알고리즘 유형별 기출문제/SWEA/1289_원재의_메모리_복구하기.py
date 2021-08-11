TC = int(input())
for i in range(TC):
    arr = input()
    n = len(arr)
    count = 0
    if arr[0] == '1':
        count += 1
    for i in range(1, n):
        if arr[i - 1] == '1' and arr[i] == '0':
            count += 1
        elif arr[i - 1] == '0' and arr[i] == '1':
            count += 1
    print(count)