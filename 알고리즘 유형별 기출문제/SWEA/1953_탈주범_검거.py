from collections import deque
t = int(input())

dx = [[], [-1, 0, 0, 1], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
dy = [[], [0, -1, 1, 0], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]


def bfs(x, y):
    global count
    q = deque([])
    q.append((x, y, 1))
    visited[x][y] = True
    while q:
        x, y, time = q.popleft()
        if time == l + 1:
            break
        k = graph[x][y]
        if k == 1:
            for i in range(4):
                can_go = False
                nx = x + dx[k][i]
                ny = y + dy[k][i]
                if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    can_go = True
                else:
                    for j in range(2):
                        ox = nx + dx[graph[nx][ny]][j]
                        oy = ny + dy[graph[nx][ny]][j]
                        if ox == x and oy == y:
                            can_go = True
                            break
                if not visited[nx][ny] and can_go:
                    visited[nx][ny] = True
                    q.append((nx, ny, time + 1))
        else:
            for i in range(2):
                can_go = False
                nx = x + dx[k][i]
                ny = y + dy[k][i]
                if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    can_go = True
                else:
                    for j in range(2):
                        ox = nx + dx[graph[nx][ny]][j]
                        oy = ny + dy[graph[nx][ny]][j]
                        if ox == x and oy == y:
                            can_go = True
                            break
                if not visited[nx][ny] and can_go:
                    visited[nx][ny] = True
                    q.append((nx, ny, time + 1))
        count += 1


for test_case in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    graph = []
    count = 0
    visited = [[False] * m for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    bfs(r, c)
    print("#" + str(test_case) + " " + str(count))
