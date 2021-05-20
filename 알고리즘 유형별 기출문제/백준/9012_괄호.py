import sys
t = int(input())

for _ in range(t):
    count_l = 0
    count_r = 0
    check = False
    data = (list(sys.stdin.readline().rstrip()))
    for i in data:
        if i == '(':
            count_l += 1
        else:
            count_r += 1
        if count_r > count_l:
            check = True
            break
    if count_l == count_r and not check:
        print('YES')
    else:
        print('NO')