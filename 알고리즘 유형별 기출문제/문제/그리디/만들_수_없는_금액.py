n = int(input())

array = list(map(int, input().split()))

array.sort()

target = 1

for i in array:
    if target < i:
        break
    target += i

print(target)