from collections import deque

tc = int(input())
for _ in range(tc):
    l = int(input())
    graph = [[1] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]


    def move(x, y, dest_x, dest_y):
        q = deque([])
        q.append((x, y))
        visited[x][y] = True
        while q:
            x, y= q.popleft()
            if x == dest_x and y == dest_y:
                return graph[x][y] - 1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > l - 1 or ny < 0 or ny > l - 1:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] += graph[x][y]
                    q.append((nx, ny))

    print(move(start_x, start_y, dest_x, dest_y))
