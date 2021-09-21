n = int(input())
arr = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
arr.sort()


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


for i in x:
    if binary_search(i, 0, n - 1) is None:
        print(0)
    else:
        print(1)
