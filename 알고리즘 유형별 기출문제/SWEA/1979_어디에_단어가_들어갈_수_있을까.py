t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = [0] * (n + 1)
    visited = [False] * n
    # 세로탐색
    for r in range(n):
        visited = [False] * n
        for c in range(n):
            if graph[r][c] == 1 and not visited[c]:
                count = 0
                now = c
                visited[now] = True
                while now < n:
                    count += 1
                    now += 1
                    if now >= n or graph[r][now] == 0:
                        break
                    visited[now] = True
                result[count] += 1
    # 가로탐색
    for c in range(n):
        visited = [False] * n
        for r in range(n):
            if graph[r][c] == 1 and not visited[r]:
                count = 0
                now = r
                visited[now] = True
                while now < n:
                    count += 1
                    now += 1
                    if now >= n or graph[now][c] == 0:
                        break
                    visited[now] = True
                result[count] += 1
    print("#" + str(tc) + " " + str(result[k]))
