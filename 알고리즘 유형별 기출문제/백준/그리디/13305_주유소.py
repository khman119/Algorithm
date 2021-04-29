import sys
input = sys.stdin.readline
n = int(input())

# n - 1 개의 도로길이
length = list(map(int, input().split()))

# n개의 도시
city = list(map(int, input().split()))

result = 0
minimum = min(city[0:n-1])
best = city[0]
result += city[0] * length[0]

for i in range(1, n):
    best = min(best, city[i])
    if best == minimum:
        result += sum(length[i:(n - 1)]) * minimum
        break
    result += best * length[i]

print(result)

# 7
# 2 3 3 1 7 1
# 5 6 3 4 2 5 1

# 5
# 3 2 1 4
# 5 8 9 4 1