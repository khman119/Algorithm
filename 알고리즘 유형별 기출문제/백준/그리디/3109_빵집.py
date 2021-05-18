import sys

r, c = map(int, input().split())
# r : 행, c: 열

graph = []

for i in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[False] * c for _ in range(r)]
count = 0


def dfs(x, y):
    if x < 0 or x > (r - 1) or y < 0 or y > (c - 1):
        return 0
    if y == c - 1:
        return 1
    if not visited[x][y] and graph[x][y] == '.':
        visited[x][y] = True
        if dfs(x - 1, y + 1):
            return 1
        if dfs(x, y + 1):
            return 1
        if dfs(x + 1, y + 1):
            return 1
    return 0


for i in range(r):
    count += dfs(i, 0)

print(count)