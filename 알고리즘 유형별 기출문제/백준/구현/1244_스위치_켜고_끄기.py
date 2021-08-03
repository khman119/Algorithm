n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())
for i in range(m):
    a, num = map(int, input().split())
    if a == 1:
        for j in range(1, n + 1):
            for k in range(num, n + 2, +num):
                if j == k:
                    if arr[j] == 1:
                        arr[j] = 0
                    else:
                        arr[j] = 1
    else:
        middle = num
        x = 1
        while 1 < middle and middle < n:
            if middle - x < 1 or middle + x > n:
                break
            if arr[middle - x] == arr[middle + x]:
                if arr[middle - x] == 1:
                    arr[middle - x] = 0
                    arr[middle + x] = 0
                else:
                    arr[middle - x] = 1
                    arr[middle + x] = 1
                x += 1
            else:
                break
        if arr[num] == 1:
            arr[num] = 0
        else:
            arr[num] = 1


if n <= 20:
    for i in range(1, n + 1):
        print(arr[i], end=' ')
    print()
if 20 < n <= 40:
    for i in range(1, 21):
        print(arr[i], end=' ')
    print()
    for i in range(21, n + 1):
        print(arr[i], end=' ')
    print()
if 40 < n <= 60:
    for i in range(1, 21):
        print(arr[i], end=' ')
    print()
    for i in range(21, 41):
        print(arr[i], end=' ')
    print()
    for i in range(41, n + 1):
        print(arr[i], end=' ')
    print()
if 60 < n <= 80:
    for i in range(1, 21):
        print(arr[i], end=' ')
    print()
    for i in range(21, 41):
        print(arr[i], end=' ')
    print()
    for i in range(41, 61):
        print(arr[i], end=' ')
    print()
    for i in range(61, n + 1):
        print(arr[i], end=' ')
    print()
if 80 < n <= 100:
    for i in range(1, 21):
        print(arr[i], end=' ')
    print()
    for i in range(21, 41):
        print(arr[i], end=' ')
    print()
    for i in range(41, 61):
        print(arr[i], end=' ')
    print()
    for i in range(61, 81):
        print(arr[i], end=' ')
    print()
    for i in range(81, n + 1):
        print(arr[i], end=' ')
    print()


# 8
# 0 1 0 1 0 0 0 1
# 1
# 1 1

# 25
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1
# 1 1

