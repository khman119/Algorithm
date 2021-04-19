array = [0] * 100

array[1] = 1
array[2] = 1
n = 99

for i in range(3, n+1):
    array[i] = array[i - 1] + array[i - 2]

print(array[99])