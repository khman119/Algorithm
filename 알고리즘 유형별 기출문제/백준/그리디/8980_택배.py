N, C = map(int, input().split())
M = int(input())
arr = [[] for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

# print(len(arr[1]))
# print(arr[1][2][1])
count = 0
truck = [0] * (N + 1)
result = 0
for i in range(1, N + 1):
    for k in range(2, N + 1):  # 하차
        if k == i:
            count -= truck[k]
            result += truck[k]
            truck[k] = 0
    for j in range(0, len(arr[i])):  # 상차
        if count >= C:
            break
        # if arr[i][j][1]
        if arr[i][j][1] + count <= C:
            count += arr[i][j][1]
            truck[arr[i][j][0]] += arr[i][j][1]
        else:
            temp = C - count
            count = C
            truck[arr[i][j][0]] += temp

# print(arr)
print(truck)
print(result)


# 4 40
# 3
# 1 4 40
# 2 3 40
# 3 4 40