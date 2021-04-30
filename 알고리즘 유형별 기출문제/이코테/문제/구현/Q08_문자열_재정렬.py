array = input()

alpha = []
sum = 0

for i in array:
    if 65 <= ord(i) <= 90:
        alpha.append(i)
    else:
       sum += int(i)

alpha.sort()

for i in alpha:
    print(i, end='')

print(sum)


# K1KA5CB7
# AJKDLSI412K4JSJ9D