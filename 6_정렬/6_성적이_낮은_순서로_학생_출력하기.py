

n = int(input())

def setting(arr):
    return arr[1]

arr = []

for i in range(n):
    sets = list(map(str, input().split()))
    sets[1] = int(sets[1])
    arr.append(sets)

arr = sorted(arr, key=setting)

# print(arr)
for i in range(len(arr)):
    print(arr[i][0], end=' ')