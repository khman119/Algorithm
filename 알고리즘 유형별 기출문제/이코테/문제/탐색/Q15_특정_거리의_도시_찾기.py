from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n + 1)]

distance = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start):
    q = deque([])
    q.append(start)
    while q:
        vertex = q.popleft()
        for i in graph[vertex]:
            if distance[i] == -1:
                distance[i] = distance[vertex] + 1
                q.append(i)


distance[x] = 0
bfs(graph, x)


def check(k, distance):
    count = 0
    for i in range(1, n + 1):
        if distance[i] == k:
            count += 1
            print(i)
    if count == 0:
        print(-1)


check(k, distance)

# 속도도 신경써서 나중에 다시 풀어볼것