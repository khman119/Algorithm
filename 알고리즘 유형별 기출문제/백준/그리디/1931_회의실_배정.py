n = int(input())

array = []
result = []

for i in range(n):
    a, b = map(int, input().split())
    array.append((a, b))

array.sort(reverse=True)
print(array)

result.append(array[0])

start = 0
for i in range(1, n):
    if result[start][0] >= array[i][1]:
        result.append(array[i])
        start += 1

print(len(result))

# length = []
# result = []
#
# for i in range(n):
#     length.append(array[i][0] + array[i][1])
#
# for i in range(n):
#     if min(length) == i:
#         result.append(array[i][1])

# 가장 빨리 끝나는 것 선택.
# 다음것 선택

# for i in range(result[0], n):
#     if min(length)

# 시작시간이 가장 빠른 것을 선택, 그 중 가장 빨리 끝나는 것을 선택.

# 0, 4
#
#
# 4, 4