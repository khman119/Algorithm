from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # x, y 좌표가 범위를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 1로만 이동해야함
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                count += 1
    return graph[n-1][m-1]

print(bfs(0,0))
