n = int(input())

array = []

for i in range(n):
    array.append(input())

dic = {}

for i in array:
    y = len(i) - 1
    for x in i:
        if x in dic:
            dic[x] += 10 ** y
        else:
            dic[x] = 10 ** y
        y -= 1

nums = []
for i in dic.values():
    nums.append(i)
nums.sort(reverse=True)
count = 9
result = 0
for i in nums:
    i *= count
    result += i
    count -= 1

print(result)