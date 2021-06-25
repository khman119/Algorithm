tc = int(input())

def dfs(x):
    visited[x] = True
    x = array[x]
    if not visited[x]:
        dfs(x)

for i in range(tc):
    count = 0
    n = int(input())
    visited = [False] * (n + 1)
    array = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)
