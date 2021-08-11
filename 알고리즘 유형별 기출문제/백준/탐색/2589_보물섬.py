import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())

arr = []
for i in range(r):
    arr.append(list(input().rstrip()))

maxNum = 0
visited = [[False] * c for _ in range(r)]
distance = [[0] * c for _ in range(r)]
check = [[0] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0


def bfs(x, y, dist):
    global count
    q = deque()
    q.append((x, y, dist))
    visited[x][y] = True
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or r <= nx or ny < 0 or c <= ny:
                continue
            if not visited[nx][ny] and arr[nx][ny] == 'L':
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
                distance[nx][ny] = dist + 1


for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            count += 1

for _ in range(count):
    visited = [[False] * c for _ in range(r)]
    distance = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and arr[i][j] == 'L' and check[i][j] == 0:
                bfs(i, j, distance[i][j])
                check[i][j] = 1
                for k in range(r):
                    maxNum = max(maxNum, max(distance[k]))

print(maxNum)
