n = int(input())

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = 7

for i in range(n):
    for j in range(n):
        if i >= j:
            if j == 0:
                down = 0
            else:
                down = dp[i - 1][j - 1]
            if i == j:
                right_down = 0
            else:
                right_down = dp[i - 1][j]
            dp[i][j] = array[i][j] + max(down, right_down)
            print(dp)

result = 0
for j in range(n):
    result = max(result, dp[n - 1][j])

print(result)


# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
