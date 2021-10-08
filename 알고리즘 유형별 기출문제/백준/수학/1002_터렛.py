import sys
from math import sqrt
t = int(input())
input = sys.stdin.readline
for _ in range(t):
    ax, ay, ar, bx, by, br = map(int, input().split())
    # 두 원의 중심이 같으면, 지름이 같으면 무한대이고 지름이 다르면 0개.
    d = sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    if ax == bx and ay == by:
        if ar == br:
            print(-1)
        else:
            print(0)
    # 두 원의 중심이 다르면,
    else:
        # 한 원의 안에 다른 원이 있는 경우.
        if d <= max(ar, br):
            if d + min(ar, br) == max(ar, br):
                print(1)
            elif d + min(ar, br) < max(ar, br):
                print(0)
            else:
                print(2)
        # 아니면,
        # 중심의 거리가 두 원의 지름의 합보다 크면
        # 0개, 같으면 1개, 작으면 2개.
        else:
            if d > ar + br:
                print(0)
            elif d < ar + br:
                print(2)
            else:
                print(1)
