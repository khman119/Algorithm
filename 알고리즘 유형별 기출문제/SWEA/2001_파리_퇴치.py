
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = []
    total = -1
    visited = [[False] * N for i in range(N)]
    for i in range(N):
        graph.append(list(map(int, input().split())))
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                visited[x][y] = True
                temp = 0
                skip = False
                for nx in range(x, x + M):
                    for ny in range(y, y + M):
                        if nx >= N or ny >= N:
                            skip = True
                            break
                        temp += graph[nx][ny]
                    if skip:
                        break
                total = max(total, temp)
    print("#"+str(test_case)+" "+str(total))
