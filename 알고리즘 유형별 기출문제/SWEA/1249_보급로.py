import heapq
INF = int(1e9)
tc = int(input())
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
answer = 0


def bfs():
    global answer
    q = []
    heapq.heappush(q, (0, 0, 0))
    visited[0][0] = True
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            answer = dist
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                continue
            cost = distance[x][y] + graph[nx][ny]
            if cost < distance[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = cost
                heapq.heappush(q, (distance[nx][ny], nx, ny))


for test_case in range(1, tc + 1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().rstrip())))
    visited = [[False] * n for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    bfs()
    print("#" + str(test_case) + " " + str(answer))
