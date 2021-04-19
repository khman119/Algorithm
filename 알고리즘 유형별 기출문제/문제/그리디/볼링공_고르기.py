n, m = map(int, input().split())

array = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i, n):
        if i != j and array[i] != array[j]:
            count += 1

print(count)

# 5 3
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2