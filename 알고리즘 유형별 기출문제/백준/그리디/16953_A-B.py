from collections import deque

a, b = map(int, input().split())

count = 0

while b != a:
    if b < a:
        count = -1
        break
    if (b - 1) % 10 == 0:
        b = (b - 1) // 10
        count += 1
    elif b % 2 == 0:
        b = b // 2
        count += 1
    else:
        count = -1
        break

if count != -1:
    print(count + 1)
else:
    print(count)

# n = (b + 1) // 2
#
# graph = [[] for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     graph[i].append(i * 2)
#     graph[i].append((i * 10) + 1)
#
#
# def bfs(a, b):
#     count = 0
#     q = deque([])
#     q.append((a, count))
#     while q:
#         now, cnt_temp = q.popleft()
#         if ((now * 10) + 1) == b or (now * 2) == b:
#             return cnt_temp + 1
#         for i in graph[now]:
#             if ((i * 10) + 1) <= b or (i * 2) <= b:
#                 cnt_temp += 1
#                 q.append((i, cnt_temp))
#     return -1
#
#
# print(bfs(a, b))