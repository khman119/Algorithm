import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
graph = []
for i in range(h):
    graph.append(list(map(int, input().split())))

# 상 하 좌 우 + 대각선
dx = [-1, 0, 0, 1, -2, -2, -1, -1, 1, 1, 2, 2]
dy = [0, -1, 1, 0, -1, 1, -2, 2, -2, 2, -1, 1]

visited = [[[False] * w for _ in range(h)] for _ in range(k + 1)]
q = deque([])
min_move = 40000


def bfs_horse():
    global min_move
    q.append((0, 0, 0, k))
    while q:
        x, y, count, k_count = q.popleft()
        if x == h - 1 and y == w - 1:
            min_move = min(min_move, count)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0 and not visited[k_count][nx][ny]:
                visited[k_count][nx][ny] = True
                q.append((nx, ny, count + 1, k_count))
        if k_count == 0:
            continue
        for i in range(4, 12):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0 and not visited[k_count - 1][nx][ny]:
                visited[k_count - 1][nx][ny] = True
                q.append((nx, ny, count + 1, k_count - 1))


bfs_horse()

if min_move == 40000:
    print(-1)
else:
    print(min_move)
