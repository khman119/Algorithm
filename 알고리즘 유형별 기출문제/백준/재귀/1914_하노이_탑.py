n = int(input())

dp = [0] * (101)
dp[1] = 1
dp[2] = 3


# def recursive(n):
#     if n == 1:
#         print(str(1) + " " + str(3))
#     else:
#         print(str(1) + " " + str(2))
#     return recursive(n - 1)


for i in range(3, 101):
    dp[i] = 2 * dp[i - 1] + 1

print(dp[n])
# if n <= 20:
