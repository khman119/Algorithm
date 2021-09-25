import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
answer = 0


def binary_search(target, start, end):
    global answer
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x <= mid:
                total += 0
            else:
                total += x - mid
        if total == target:
            answer = mid
            break
        # 나무를 더 잘라야함
        elif total < target:
            end = mid - 1
        # 나무를 덜 잘라도 됨
        else:
            answer = mid
            start = mid + 1


binary_search(m, 0, max(array))
print(answer)
