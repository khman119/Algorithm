import heapq
import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    a, b = map(int, input().split())
    array.append((a, b))
array.sort()
queue = []
heapq.heappush(queue, array[0][1])
for i in range(1, n):
    if queue[0] > array[i][0]:
        heapq.heappush(queue, array[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, array[i][1])
print(len(queue))
