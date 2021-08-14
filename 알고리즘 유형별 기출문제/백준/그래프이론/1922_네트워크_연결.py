import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = []
for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

graph.sort()
result = 0


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


for i in range(m):
    dist, a, b = graph[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist

print(result)
