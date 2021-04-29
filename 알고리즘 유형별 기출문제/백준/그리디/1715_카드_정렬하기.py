import heapq

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

heapq.heapify(array)

# dp = [0] * n
result = 0
total = 0

while len(array) != 1:
    x = heapq.heappop(array)
    y = heapq.heappop(array)
    result = x + y
    # dp.append(result)
    total += result
    heapq.heappush(array, result)
    # if len(array) == 1:
    #     break

print(total)

# 5
# 10
# 70
# 90
# 200
# 300

# 파이썬 while문 코드
# 런타임 에러 (IndexError)
# if len(array) == 1:
#     break
