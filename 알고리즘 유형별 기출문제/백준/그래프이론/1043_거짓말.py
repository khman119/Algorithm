import sys
input = sys.stdin.readline


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


n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

trues = list(map(int, input().split()))
if len(trues) == 1:
    print(m)

else:
    for i in range(1, len(trues) - 1):
        union_parent(parent, trues[i], trues[i + 1])
    parties = []
    trueParent = 51
    count = 0
    for i in range(m):
        arr = list(map(int, input().split()))
        arr.pop(0)
        parties.append(arr)
    for i in range(m):
        for j in range(len(parties[i]) - 1):
            union_parent(parent, parties[i][j], parties[i][j + 1])
    for i in range(1, len(trues)):
        trueParent = min(trueParent, trues[i])
    for i in range(m):
        lieParty = True
        for j in range(len(parties[i])):
            if find_parent(parent, parties[i][j]) == find_parent(parent, trueParent):
                lieParty = False
                break
        if lieParty:
            count += 1

    print(count)
