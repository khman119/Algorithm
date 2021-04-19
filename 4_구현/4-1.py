position = str(input())

print(position)

x =position[0]
y =position[1]


if x == 'a': x = 1
elif x == 'b' : x = 2
elif x == 'c' : x = 3
elif x == 'd' : x = 4
elif x == 'e' : x = 5
elif x == 'f' : x = 6
elif x == 'g' : x = 7
elif x == 'h' : x = 8


range_x = ['1', '2', '3', '4', '5', '6', '7', '8']
range_y = ['1', '2', '3', '4', '5', '6', '7', '8']

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0
for i in range(len(dx)):
    if 1 <= x + dx[i] <= 8:
        if 1 <= int(y) + dy[i] <= 8:
            count += 1


print(count)
