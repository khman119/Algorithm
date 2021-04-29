n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

array.sort()
result = 0

array_left = [x for x in array if x < 1]
array_one = [x for x in array if x == 1]
array_right = [x for x in array if x > 1]

array_right.sort(reverse=True)

for i in range(0, len(array_right), 2):
    if len(array_right) % 2 == 1 and i == len(array_right) - 1:
        result += array_right[i]
        # 홀수면
    else:
        result += array_right[i] * array_right[i + 1]

for i in range(0, len(array_left), 2):
    if len(array_left) % 2 == 1 and i == len(array_left) - 1:
        result += array_left[i]
        # 홀수면
    else:
        result += array_left[i] * array_left[i + 1]

result += sum(array_one)

print(result)
# print(array_left)
# print(array_one)
# print(array_right)