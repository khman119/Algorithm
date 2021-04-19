n = int(input())

count = 0

while True:
    if n == 0:
        break
    elif n == 4 or n == 2 or n == 1:
        count = -1
        break
    else:
        if (n % 5 == 3 or n % 5 == 0) and n >= 5:
            n -= 5
            count += 1
        else:
            n -= 3
            count += 1

print(count)