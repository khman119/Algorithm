tc = int(input())
for i in range(tc):
    N, M = map(int, input().split())
    visit = [False] * (N + 1)
    count = 0
    arr = []
    for _ in range(M):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[1])
    # for i in range(M):
    #     for j in range(arr[i][1], arr[i][0] - 1, -1):
    #         if not visit[j]:
    #             visit[j] = True
    #             count += 1
    #             break
    # while arr:
    #     a, b = arr.pop(0)
    #     for j in range(a, b + 1):
    #         if not visit[j]:
    #             visit[j] = True
    #             count += 1
    #             break

    print(count)
    print(visit)


# 1
# 2 3
# 1 2
# 1 2
# 1 2

# 1
# 2 1
# 2 2

# 1
# 4 4
# 1 2
# 2 3
# 3 4
# 1 3

# 1
# 3 3
# 1 3
# 1 3
# 2 2

# 1
# 7 4
# 1 7
# 1 7
# 1 7
# 2 2