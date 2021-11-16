import sys
from itertools import combinations
input = sys.stdin.readline
arr = list(map(int, input().split()))
while arr[0] != 0:
    sets = [arr[i] for i in range(1, len(arr))]
    for x in combinations(sets, 6):
        for y in x:
            print(y, end=' ')
        print()
    print()
    arr = list(map(int, input().split()))
