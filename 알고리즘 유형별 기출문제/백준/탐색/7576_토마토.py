from collections import deque

INF = int(1e9)

m, n = map(int, input().split())

graph = []
distance = [[0] * m for i in range(n)]
result = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(q):
    global count
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))


q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            distance[i][j] = 0
            q.append((i, j))

bfs(q)


def check(graph, result):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
            result = max(distance[i][j], result)
    return result

print(check(graph, result))
# print(distance)