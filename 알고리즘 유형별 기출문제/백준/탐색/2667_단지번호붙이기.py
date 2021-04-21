n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

global count
count = 0

result = []


def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(count)
            count = 0

print(len(result))
result.sort()
for i in result:
    print(i)