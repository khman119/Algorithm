T = int(input())


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


for test_case in range(1, T + 1):
    count = 0
    v, e = map(int, input().split())
    graph = []
    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i
    for i in range(e):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
    graph.sort(key=lambda x: x[0])
    for i in range(e):
        if find_parent(parent, graph[i][1]) != find_parent(parent, graph[i][2]):
            union_parent(parent, graph[i][1], graph[i][2])
            count += graph[i][0]
    print("#" + str(test_case) + " " + str(count))
