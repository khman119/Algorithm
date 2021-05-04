from collections import deque
INF = int(1e9)
m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(m - y2, m - y1):
        for j in range(x1, x2):
            graph[i][j] = INF


def bfs(x, y):
    global count
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([])
    visited[x][y] = True
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > (m - 1) or ny > (n - 1):
                continue
            if graph[nx][ny] == INF:
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    return count


results = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            count = 1
            result = bfs(i, j)
            results.append(result)

results.sort()
print(len(results))
for i in results:
    print(i, end=' ')
