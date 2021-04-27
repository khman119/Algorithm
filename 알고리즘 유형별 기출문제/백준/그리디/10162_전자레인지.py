t = int(input())

buttons = [300, 60, 10]
count = 0
counts = []

for button in buttons:
    while True:
        if t >= button:
            t -= button
            count += 1
        else:
            counts.append(count)
            count = 0
            break

if t == 0:
    for i in counts:
        print(i, end=' ')

else:
    print(-1)

# 234

