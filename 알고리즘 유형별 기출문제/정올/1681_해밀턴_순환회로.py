import sys
sys.setrecursionlimit(int(1e6))
INF = int(1e9)
n = int(input())
arr = []
visited = [False] * n
ans = INF
for _ in range(n):
    arr.append(list(map(int, input().split())))
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        else:
            graph[i].append((j, arr[i][j]))


def dfs(now, depth, cost):
    global ans
    if cost >= ans:
        return
    if now == 0 and depth == n:
        ans = min(ans, cost)
        return
    for i in graph[now]:
        if not visited[i[0]]:
            visited[i[0]] = True
            dfs(i[0], depth+1, cost + i[1])
            visited[i[0]] = False


dfs(0, 0, 0)
print(ans)
