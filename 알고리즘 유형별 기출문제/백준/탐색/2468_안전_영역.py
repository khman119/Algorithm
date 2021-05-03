from collections import deque
n = int(input())


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([])
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > (n - 1) or ny > (n - 1):
                continue
            if graph[nx][ny] > k and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

maximum = 0

for i in range(n):
    for j in range(n):
        maximum = max(graph[i][j], maximum)

result = []

for k in range(maximum):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                bfs(i, j)
                count += 1
    result.append(count)

print(max(result))