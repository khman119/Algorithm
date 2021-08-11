import sys

input = sys.stdin.readline
N = int(input())
arrCrane = list(map(int, input().split()))
M = int(input())
arrBox = list(map(int, input().split()))

arrCrane.sort(reverse=True)
arrBox.sort(reverse=True)

count = 0
if arrCrane[0] < arrBox[0]:
    count = -1
else:
    while arrBox:
        count += 1
        for i in arrCrane:
            for j in range(len(arrBox)):
                if i >= arrBox[j]:
                    del arrBox[j]
                    break
print(count)
