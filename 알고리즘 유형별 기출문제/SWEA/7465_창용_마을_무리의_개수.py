t = int(input())

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


for testCase in range(1, t + 1):
    n, m = map(int, input().split())
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    for _ in range(m):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
    answer = []
    for i in range(1, n + 1):
        answer.append(find_parent(parent, i))
    answer = set(answer)
    print("#" + str(testCase) + " " + str(len(answer)))
