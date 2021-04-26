n = int(input())

dp = [0] * (n + 1)
count = 0


def divide_three(x):
    if x % 3 == 0:
        x = (x // 3)
    else:
        x -= 1
    return x


def divide_two(x):
    if x % 2 == 0:
        x = (x // 2)
    else:
        x -= 1
    return x


def minus_one(x):
    x -= 1
    return x


if n >= 2:
    dp[2] = 1

for i in range(3, n + 1):
    dp[i] = 1 + min(dp[divide_three(i)], dp[divide_two(i)], dp[minus_one(i)])

print(dp[n])
