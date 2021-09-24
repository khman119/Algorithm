import sys
input = sys.stdin.readline
k, n = map(int, input().split())
array = []
for _ in range(k):
    array.append(int(input()))
answer = 0


def binary_search(target, start, end):
    global answer
    while start <= end:
        count = 0
        mid = (start + end) // 2
        for x in array:
            count += (x // mid)
        #     더 잘게 쪼개야함.
        if target > count:
            end = mid - 1
        #     더 크게 쪼개도 됨.
        elif target <= count:
            answer = mid
            start = mid + 1


binary_search(n, 1, max(array))
print(answer)
