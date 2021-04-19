n = int(input())
arr_stock = [0] * 1000001
for i in input().split():
    arr_stock[int(i)] = 1

m = int(input())
arr_require = list(map(int, input().split()))

for i in arr_require:
    if arr_stock[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# input
# 5
# 8 3 7 9 2
# 3
# 5 7 9