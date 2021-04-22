n = int(input())
fears = list(map(int, input().split()))

# 공포도가 가장 낮은 모험가로 파티 구성

fears.sort()
member = 0
group = 0
fear = fears[0]

for i in range(n):
    if member >= fear:
        member = 0
        group += 1
        fear = fears[0]
    else:
        fears.pop(0)
        member += 1

print(group)
# 5
# 2 3 1 2 2