import sys
from collections import deque
# 세로 n, 가로 m
n, m = map(int, input().split())
graph = []
input = sys.stdin.readline
for _ in range(n):
    graph.append(list(input().rstrip()))


visited = [[[False] * m for _ in range(n)] for _ in range(1 << 6)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
answer = 0


def bfs(x, y):
    global answer
    q = deque([])
    q.append((x, y, 0, 0))
    visited[0][x][y] = True
    while q:
        x, y, count, key_count = q.popleft()
        if graph[x][y] == '1':
            answer = count
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or graph[nx][ny] == '#' or visited[key_count][nx][ny]:
                continue
            if ord('a') <= ord(graph[nx][ny]) <= ord('f'):
                visited[key_count | (1 << (ord(graph[nx][ny]) - 97))][nx][ny] = True
                q.append((nx, ny, count + 1, key_count | (1 << (ord(graph[nx][ny]) - 97))))
            elif ord('A') <= ord(graph[nx][ny]) <= ord('F'):
                if (key_count & (1 << (ord(graph[nx][ny]) - 65))) != 0:
                    visited[key_count][nx][ny] = True
                    q.append((nx, ny, count + 1, key_count))
            else:
                visited[key_count][nx][ny] = True
                q.append((nx, ny, count + 1, key_count))


finish = False
for r in range(n):
    for c in range(m):
        if graph[r][c] == '0':
            bfs(r, c)
            finish = True
            break
        if finish:
            break

if answer == 0:
    print(-1)
else:
    print(answer)
