n = int(input())
dp = [[0 for _ in range(10)] for _ in range(1001)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        for k in range(9, j - 1, -1):
            dp[i][j] += dp[i - 1][k]
print(sum(dp[n]) % 10007)
