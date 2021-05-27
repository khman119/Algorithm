n = int(input())

array = [0] * 301
for i in range(n):
    array[i] = int(input())

dp = [0] * 301
dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[0] + array[2], array[1] + array[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + array[i - 1] + array[i], array[i] + dp[i - 2])

print(dp[n - 1])


# 5
# 50
# 40
# 30
# 20
# 10
#
# 6
# 100
# 40
# 10
# 60
# 70
# 20