import heapq

n = int(input())
INF = int(1e9)
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
count = 1


def bfs():
    global answer
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    visited[0][0] = True
    while q:
        dist, r, c = heapq.heappop(q)
        if r == n - 1 and c == n - 1:
            answer = dist
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr > n - 1 or nc > n - 1:
                continue
            cost = graph[nr][nc] + distance[r][c]
            if not visited[nr][nc]:
                visited[nr][nc] = True
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heapq.heappush(q, (cost, nr, nc))


while n != 0:
    graph = []
    answer = 0
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[False] * n for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    bfs()
    print("Problem " + str(count) + ": " + str(answer))
    count += 1
    n = int(input())
