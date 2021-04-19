
# for i in range(m):
#     for j in range(n):
#         if arr_stock[j] == arr_require[i]:
#             print('yes', end=' ')
#             break
#         elif j == n-1:
#             print('no', end=' ')

# 이진 탐색
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         # 있으면
#         if array[mid] == target:
#             return mid
#         # mid 값보다 target이 작으면
#         elif array[mid] > target:
#             end = mid - 1
#         # mid 값보다 target이 크면
#         else:
#             start = mid + 1
#     return None

# for i in arr_require:
#     result = binary_search(arr_stock, i, 0, n-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

n = int(input())
arr_stock = list(map(int, input().split()))

m = int(input())
arr_require = list(map(int, input().split()))

arr_stock = sorted(arr_stock)



# input
# 5
# 8 3 7 9 2
# 3
# 5 7 9