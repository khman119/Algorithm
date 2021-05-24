import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[-1] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]


def water(q):
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 'D' or graph[nx][ny] == 'X':
                continue
            if graph[nx][ny] == '.' or graph[nx][ny] == 'S' and not visited[nx][ny]:
                graph[nx][ny] = '*'


def move(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == '*' or graph[nx][ny] == 'X':
                continue
            if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and ((nx, ny) not in q) and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                graph[nx][ny] = 'S'


def bfs(x, y):
    wq = deque([])
    mq = deque([])
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'S':
                mq.append((i, j))
                dist[i][j] = 0
                graph[i][j] = '.'
            if graph[i][j] == '*':
                wq.append((i, j))
    while mq:
        move(mq)
        water(wq)
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'S':
                    if i == x and y == j:
                        return
                    mq.append((i, j))
                if graph[i][j] == '*' and not visited[i][j]:
                    wq.append((i, j))


x = 0
y = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'D':
            x, y = i, j
bfs(x, y)

if dist[x][y] == -1:
    print('KAKTUS')
else:
    print(dist[x][y])
# print(visited)
# print(graph)
# print(dist)