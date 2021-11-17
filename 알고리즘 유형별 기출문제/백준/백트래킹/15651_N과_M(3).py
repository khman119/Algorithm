from itertools import product
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
for x in product(arr, repeat=m):
    for y in x:
        print(y, end=' ')
    print()
