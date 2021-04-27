# 버틸 수 있는 중량이 최소인 로프 * N이거나
# 최소인 로프를 제외한 나머지

# => 40이 아니라
# => 100 * 2로 200임
#
# 10 50 100 100
#
# 10 * 4
# 50 * 3

n = int(input())
weight = []
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

for i in range(n):
    weight.append(array[i] * (n-i))

print(max(weight))