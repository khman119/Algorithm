t = int(input())
for tc in range(1, t + 2):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    print("#" + str(tc))
    for i in range(n):
        for j in range(n):
            print(graph[n - (j + 1)][i], end='') # 90도 회전
        print(end=' ')
        for j in range(n):
            print(graph[n - (i + 1)][n - (j + 1)], end='') # 180도 회전
        print(end=' ')
        for j in range(n):
            print(graph[j][n - (i + 1)], end='') # 270도 회전
        print()
