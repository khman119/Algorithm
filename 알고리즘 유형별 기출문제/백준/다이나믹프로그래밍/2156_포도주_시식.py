import sys
input = sys.stdin.readline
n = int(input())
array = [0] * 10000
for i in range(n):
    array[i] = int(input())

dp = [0] * 10000
dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[0] + array[2], array[1] + array[2])
result = 0
for i in range(3, n):
    dp[i] = max(dp[i - 2] + array[i], dp[i - 3] + array[i - 1] + array[i], dp[i - 4] + array[i - 1] + array[i])

print(max(dp))

# 10
# 0
# 0
# 10
# 0
# 5
# 10
# 0
# 0
# 1
# 10

# 14
# 0
# 0
# 10
# 0
# 10
# 5
# 2
# 0
# 0
# 0
# 0
# 0
# 1
# 10