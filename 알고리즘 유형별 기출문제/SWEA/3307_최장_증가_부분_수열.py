T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * N
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    print(max(dp))

# 2
# 5
# 1 3 2 5 4
# 6
# 4 2 3 1 5 6