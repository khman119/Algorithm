array = input()

count0 = 0
count1 = 1

if array[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(array) - 1):
    if array[i] != array[i + 1]:
        if array[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))