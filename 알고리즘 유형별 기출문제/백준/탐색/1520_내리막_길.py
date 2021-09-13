import sys
import heapq

input = sys.stdin.readline
m, n = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]
visited = [[0] * n for _ in range(m)]


def bfs():
    q = []
    heapq.heappush(q, (-graph[0][0], 0, 0))
    visited[0][0] = 1
    while q:
        now, x, y = heapq.heappop(q)
        if x == m - 1 and y == n - 1:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[x][y] > graph[nx][ny]:
                if visited[nx][ny] == 0:
                    heapq.heappush(q, (-graph[nx][ny], nx, ny))
                visited[nx][ny] += visited[x][y]


bfs()
print(visited[m - 1][n - 1])


# 4 4
# 16 9 8 1
# 15 10 7 2
# 14 11 6 3
# 13 12 5 4
# ans = 10
