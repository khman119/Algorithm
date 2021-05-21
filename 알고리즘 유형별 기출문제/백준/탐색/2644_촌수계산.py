from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

visited = [False] * (n + 1)
dist = [0] * (n + 1)


def bfs(a):
    q = deque([])
    q.append(a)
    visited[a] = True
    while q:
        now = q.popleft()
        if now == b:
            return dist[now]
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[now] + 1
                q.append(i)
    return -1


print(bfs(a))


# 9
# 7 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6


# 10
# 7 6
# 9
# 1 2
# 1 3
# 1 4
# 9 1
# 9 10
# 3 5
# 3 6
# 2 7
# 2 8

# 5
# 1 5
# 4
# 1 2
# 1 3
# 2 4
# 3 5