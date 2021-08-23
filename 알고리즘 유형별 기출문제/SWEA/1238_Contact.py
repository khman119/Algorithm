from collections import deque


def bfs(start):
    q = deque([])
    q.append((start, 0))
    visited[start] = True
    while q:
        now, count = q.popleft()
        result.append((count, now))
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, count + 1))


for testCase in range(1, 11):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [False] * 101
    graph = [[] for i in range(101)]
    for i in range(0, len(arr), 2):
        # from
        graph[arr[i]].append(arr[i + 1])

    result = []
    bfs(start)
    result.sort(key=lambda x: (-x[0], -x[1]))
    print("#" + str(testCase) + " " + str(result[0][1]))

