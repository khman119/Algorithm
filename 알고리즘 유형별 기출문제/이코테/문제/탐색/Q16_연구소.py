from collections import deque

n, m = map(int, input().split())

graph = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque([])
wall = 0
result = 0


def virus(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or temp[nx][ny] == 1:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

def getScore():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

def bfs(wall):
    global result
    if wall == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    q.append((i, j))
        virus(q)
        result = max(getScore(), result)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall += 1
                bfs(wall)
                graph[i][j] = 0
                wall -= 1


bfs(wall)
print(result)