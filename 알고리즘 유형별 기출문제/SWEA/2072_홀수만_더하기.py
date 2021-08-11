T = int(input())
for test_case in range(1, T + 1):
    result = 0
    arr = list(map(int, input().split()))
    n = len(arr)
    for i in range(n):
        if arr[i] % 2 == 1:
            result += arr[i]
    print("#" + str(test_case) + " " + str(result))