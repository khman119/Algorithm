from collections import deque

n, k = map(int, input().split())
m = int(1e6)
graph = [[] for _ in range(m + 1)]
visited = [False] * (m + 1)

graph[0].append(1)

for i in range(1, m + 1):
    if (2 * i) <= m:
        graph[i].append(2 * i)
    if (i - 1) >= 0:
        graph[i].append(i - 1)
    if (i + 1) not in graph[i] and (i + 1) <= m:
        graph[i].append(i + 1)


def bfs(n, k, graph):
    count = 0
    q = deque([])
    q.append([n, count])
    while q:
        now, count = q.popleft()
        visited[now] = True
        if now == k:
            return count
        count += 1
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append([i, count])
    return count


result = bfs(n, k, graph)

print(result)