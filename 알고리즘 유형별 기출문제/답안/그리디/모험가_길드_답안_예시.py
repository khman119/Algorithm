n = int(input())
fears = list(map(int, input().split()))

# 공포도가 가장 낮은 모험가로 파티 구성

fears.sort()
member = 0
group = 0

for i in fears:
    member += 1
    if member >= i:
        group += 1
        member = 0

print(group)
# 5
# 2 3 1 2 2