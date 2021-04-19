n, m = map(int, input().split())
INF = int(1e9)

# 소개팅 K
# X 회사 방문해 물건 판매
# X 회사에 들르기 전에 K 회사 방문.

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 1에서 x회사로. graph[1][x] = min(graph[1][x] , graph[1][k] + graph[k][n])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5