n = int(input())

graph = [[0] * n for i in range(n)]

# 동 남 서 북 방향.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = n
start = 1
x = 0
y = 0
i = 0
graph[0][0] = start
while start < n**2:
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] != 0:
        if i == 3:
            i = 0
        else:
            i += 1
        continue
    if graph[nx][ny] == 0:
        start += 1
        graph[nx][ny] = start
        x = nx
        y = ny

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
