import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    data = []
    n = int(input())
    count = 1
    for i in range(n):
        a, b = map(int, input().split())
        data.append((a, b))
        # a는 서류, b는 면접
    data.sort()
    # 서류 점수가 낮은데, 면접 점수도 낮으면 탈락
    maximum = data[0][1]
    for i in range(1, n):
        if maximum > data[i][1]:
            count += 1
            maximum = data[i][1]
    print(count)


# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1
#

# 5등을 했으면, 1등을 해야함