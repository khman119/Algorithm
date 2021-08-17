n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])
count = 1
temp = arr[0][1]
if n == 1:
    print(count)
else:
    for i in range(1, n):
        if temp >= arr[i][0]: # count 그대로
            continue
        else: # count 하나 증가
            count += 1
            temp = arr[i][1]
    print(count)
