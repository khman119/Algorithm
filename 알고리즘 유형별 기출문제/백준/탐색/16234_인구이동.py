from collections import deque


def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                continue
            if not visited[nx][ny] and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                visited[nx][ny] = True
                check[x][y] = 1
                check[nx][ny] = 1
                q.append((nx, ny))


def union(x, y):
    sum = 0
    country = []
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    country.append((x, y))
    sum += arr[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                continue
            if not visited[nx][ny] and (L <= abs(arr[x][y] - arr[nx][ny]) <= R):
                visited[nx][ny] = True
                check[x][y] = 1
                check[nx][ny] = 1
                q.append((nx, ny))
                country.append((nx, ny))
                sum += arr[nx][ny]
    sum = sum // len(country)
    for i in range(len(country)):
        arr[country[i][0]][country[i][1]] = sum


def move():
    global count
    happen = False
    for i in range(N):
        for j in range(N):
            if check[i][j] == 1 and not visited[i][j]:
                happen = True
                union(i, j)
    if happen:
        count += 1


N, L, R = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

check = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

count = 0
temp = 0

while count <= 2000:
    total = 0
    check = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
    visited = [[False] * N for _ in range(N)]
    move()
    for i in range(N):
        for j in range(N):
            total += check[i][j]
    if total == 0:
        break

print(count)