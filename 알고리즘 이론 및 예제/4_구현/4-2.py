pos = input()

x = (ord(pos[0]) - ord('a')) + 1
y = int(pos[1])

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

count = 0
for step in steps:
    if 1 <= x + step[0] <= 8:
        if 1<= y + step[1] <= 8:
            count += 1

print(count)