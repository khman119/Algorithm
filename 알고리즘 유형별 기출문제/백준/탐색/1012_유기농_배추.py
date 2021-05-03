import sys
sys.setrecursionlimit(10**7)

tc = int(input())


def dfs(x, y):
    if x < 0 or y < 0 or x > (n - 1) or y > (m - 1):
        return
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
    return


for _ in range(tc):
    count = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)