n, m = list(map(int, input().split(' ')))

array = list(map(int, input().split()))

# print(sum(array))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0 # 떡 길이
    mid = (start + end) // 2
    for x in array:
        if x > mid :
            total += x - mid
    if result == m:
        break
    # 떡 길이가 m보다 작으면 절단기 높이 낮추기
    if total < m :
        end = mid - 1
    # 떡 길이가 m보다 크면 절단기 높이 높이기
    else:
        result = mid # 최대한 덜 달랐을 때가 정답.
        start = mid + 1

print(result)
# input
# 4 6
# 19 15 10 17