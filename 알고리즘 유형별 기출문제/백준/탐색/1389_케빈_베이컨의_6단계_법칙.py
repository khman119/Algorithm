from collections import deque
INF = int(1e9)
n, m = map(int, input().split())

graph = [set([]) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                dist[i] = 1 + dist[now]
                q.append(i)


num = [INF] * (n + 1)
for i in range(1, n + 1):
    dist = [0] * (n + 1)
    visited = [False] * (n + 1)
    bfs(i)
    num[i] = sum(dist)

minimum = min(num)
for i in range(1, n + 1):
    if minimum == num[i]:
        print(i)
        break
