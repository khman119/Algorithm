t = int(input())
for testCase in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    account = 0
    maxNum = arr[-1]
    for i in range(n - 2, -1, -1):
        if maxNum > arr[i]:
            account = maxNum - arr[i] + account
        else:
            maxNum = arr[i]
    print("#" + str(testCase) + " " + str(account))
