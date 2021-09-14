import sys
from collections import deque
input = sys.stdin.readline
row, col = map(int, input().split())

graph = []
for i in range(row):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def air_bfs():
    visited = [[False] * col for _ in range(row)]
    q = deque([])
    graph[0][0] = -1
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if (graph[nx][ny] == 0 or graph[nx][ny] == -1) and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = -1
                q.append((nx, ny))


def delete_cheese():
    isHole = []
    visited = [[False] * col for _ in range(row)]
    for x in range(row):
        for y in range(col):
            if graph[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= row or ny >= col:
                        continue
                    if graph[nx][ny] == -1:
                        isHole.append((x, y))
                        break
    for i in range(len(isHole)):
        graph[isHole[i][0]][isHole[i][1]] = -1
    return len(isHole)


result = []
while True:
    air_bfs()
    temp = delete_cheese()
    if temp == 0:
        break
    result.append(temp)

print(len(result))
print(result[-1])
