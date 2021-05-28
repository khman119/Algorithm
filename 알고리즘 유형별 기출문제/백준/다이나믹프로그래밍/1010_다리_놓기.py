import sys
input = sys.stdin.readline
tc = int(input())

# sol1
# for _ in range(tc):
#     n, m = map(int, input().split())
#     array = [[0] * 31 for _ in range(31)]
#     for i in range(31):
#         array[i][0] = 1
#         array[i][i] = 1
#     for k in range(2, 31):
#         for i in range(k, 31):
#             for j in range(i):
#                 array[i][k - 1] += array[j][k - 2]
#     print(array[m][n])

# sol2
for _ in range(tc):
    n, m = map(int, input().split())
    dp = [1] * 31
    for i in range(2, 31):
        dp[i] = i * dp[i - 1]
    print(dp[m]//(dp[m - n] * dp[n]))



# 3
# 2 2
# 1 5
# 13 29
