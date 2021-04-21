from collections import deque

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, start, visited)
print()
visited = [False] * (n + 1)
bfs(graph, start, visited)