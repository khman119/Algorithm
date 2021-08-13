import sys
input = sys.stdin.readline
v, e = map(int, input().split())

graph = []

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i


def find_parent(parent, x):
    if (parent[x] != x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0

for i in range(e):
    dist, a, b = graph[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist

print(result)
