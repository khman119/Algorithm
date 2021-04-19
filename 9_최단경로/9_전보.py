# 도시 개수 N, 통로 개수 M, 메시지를 보내고자 하는 도시 C

# 통로 x, y, z에 대한 정보. 도시x to 도시y, 전달되는 시간 z

# 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간 출력

import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())


# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 최단거리 리스트 초기화
distance = [INF] * (n + 1)

# 그래프 만들기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


# 다익스트라 알고리즘 돌리기
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0
for i in distance:
    if i != INF:
       count += 1
       max_distance = max(max_distance, i)
print(count - 1, max_distance)

# 3 2 1
# 1 2 4
# 1 3 2