import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())


def bfs(q):
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                if checks[now] == 1:
                    checks[i] = 0
                else:
                    checks[i] = 1
                visited[i] = True
                q.append(i)


for _ in range(tc):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    q = deque([])
    checks = [0] * (v + 1)
    is_check = False

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            q.append(i)
            visited[i] = True
            checks[i] = 1
            bfs(q)

    for i in range(1, v + 1):
        for j in graph[i]:
            if checks[i] == checks[j]:
                is_check = True
                break
        if is_check:
            break
    if is_check:
        print('NO')
    else:
        print('YES')
