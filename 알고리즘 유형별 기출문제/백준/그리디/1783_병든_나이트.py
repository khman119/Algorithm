n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    if m <= 6:
        print((m + 1) // 2)
    else:
        print(4)
else:
    if m <= 6:
        print(min(m, 4))
    else:
        count = (m - 2)
        print(count)