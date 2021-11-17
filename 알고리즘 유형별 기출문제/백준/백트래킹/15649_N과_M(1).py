from itertools import permutations
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
for x in permutations(arr, m):
    for y in x:
        print(y, end=' ')
    print()
