TC = int(input())
for tc in range(TC):
    N, L = map(int, input().split())
    arr = []
    score = [0] * N
    for i in range(N):
        t, k = (map(int, input().split()))
        arr.append([k, t])
    arr.sort()
    kcal = arr[0][0]
    score[0] = arr[0][1]
    maxScore = 0
    maxKcal = 0
    # arr[i][0] 칼로리
    # arr[i][1] 점수
    for i in range(1, N):
        if kcal + arr[i][0] <= L:
            kcal += arr[i][0]
            score[i] = arr[i][1] + score[i - 1]
        else:
            if
            limit = L - arr[i][0]
            for j in range(i):
                if arr[j][0] <= limit:
                    maxScore = max(maxScore, arr[j][1])
            for j in range(i):
                if maxScore == arr[j][1]:
                    maxKcal = arr[j][0]
            kcal += maxKcal
            score[i] = arr[i][1] + maxScore
    # print("#" + str(tc + 1) + " " + str(max(score)))
    # print(arr)
    print(score)

# 1
# 5 1000
# 100 200
# 300 500
# 250 300
# 500 1000
# 400 400

# 1
# 5 600
# 100 100
# 10 200
# 3 300
# 60 400
# 70 500