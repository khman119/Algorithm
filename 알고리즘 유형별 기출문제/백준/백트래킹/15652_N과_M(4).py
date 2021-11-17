from itertools import combinations_with_replacement
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
for x in combinations_with_replacement(arr, m):
    for y in x:
        print(y, end=' ')
    print()
