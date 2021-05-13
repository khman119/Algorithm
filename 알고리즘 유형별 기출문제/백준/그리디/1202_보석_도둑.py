import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

jews = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jews, (m, v))

for _ in range(k):
    bags.append(int(input()))

bags.sort()

temp_jews = []
result = 0

for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(temp_jews, -heapq.heappop(jews)[1])
    if temp_jews:
        result -= heapq.heappop(temp_jews)

print(result)