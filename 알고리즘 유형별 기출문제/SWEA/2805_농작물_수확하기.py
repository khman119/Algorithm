t = int(input())
for testCase in range(1, t + 1):
    n = int(input())
    graph = []
    total = 0
    for _ in range(n):
        graph.append(list(input().rstrip()))
    mid = n//2
    a = n - 1
    for i in range(mid):
        for j in range(mid - i, mid + i + 1):
            total += int(graph[i][j])
            total += int(graph[a][j])
        a -= 1
    for i in range(n):
        total += int(graph[mid][i])
    print("#" + str(testCase) + " " + str(total))
