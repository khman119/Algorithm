import sys
from collections import deque
q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == arr[x][y] and not table[nx][ny]:
                    q.append([nx, ny])
                    table[nx][ny] = True


n = int(input())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
table = [[False] * n for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if not table[i][j]:
            bfs(i, j)
            count += 1
print(count, end=' ')

for i in range(n):
    for j in range(n):
        table[i][j] = False
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

count = 0
for i in range(n):
    for j in range(n):
        if not table[i][j]:
            bfs(i, j)
            count += 1
print(count)
