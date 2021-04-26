import time


n, k = map(int, input().split())

array = []
count = 0

for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    while True:
        if i <= k and k % i == 0:
            count += (k//i)
            k -= i * (k//i)
        if i <= k:
            k -= i
            count += 1
        if i > k:
            break
    if k == 0:
        break

print(count)



# start = time.time()
# finish = time.time()
# print(finish - start)
