from collections import deque

# 가로, 세로, 높이
m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]

dx = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 1, -1, 0, 0]
result = 0


for j in range(h):
    for i in range(n):
        graph[j].append(list(map(int, input().split())))


# 순서대로 h, n(행), m(열)
# print(graph[0][2][3])


def bfs(q):
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx > (m - 1) or ny > (n - 1) or nz > (h - 1):
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                count[nz][ny][nx] = count[z][y][x] + 1
                q.append((nz, ny, nx))


def check(graph, result):
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 0:
                    return -1
                result = max(count[z][y][x], result)
    return result


count = [[[0] * m for _ in range(n)] for _ in range(h)]
q = deque([])

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                q.append((z, y, x))

bfs(q)

print(check(graph, result))

# 3차원 배열