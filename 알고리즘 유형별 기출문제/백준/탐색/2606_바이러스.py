n = int(input())
m = int(input())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]
count = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start, visited):
    global count
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            count += 1
            dfs(graph, i, visited)
    return count


print(dfs(graph, 1, visited))