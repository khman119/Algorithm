import sys
INF = int(1e10)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]


weights = [0] * (N + 1)
parent = [i for i in range(N + 1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    union_parent(parent, a, b)
    # weights[a] = min(weights[0], c)

print(parent)
print(graph)
# print(weights)


# 4 4
# 1 2 300
# 2 4 200
# 3 4 100
# 1 3 10
