from collections import deque

# queue = deque()
#
# #삽입5 - 삽입2 - 삽입3 - 삽입7 - 삭제 - 삽입1 - 삽입4 - 삭제
#
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
#
# print(queue)
# queue.reverse()
# print(queue)

start = 1

queue = deque([start])

while queue:
    print("횟수")
    v = queue.popleft()

print(queue)