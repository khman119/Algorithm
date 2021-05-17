n = int(input())

data = []

for i in range(n):
    data.append(int(input()))

count = 0

for i in range(n - 1, 0, -1):
    while data[i - 1] >= data[i]:
        print(data[i - 1])
        data[i - 1] -= 1
        count += 1

print(count)