n = int(input())

n = str(n)

sum_right = 0
sum_left = 0

for i in range(len(n)//2):
    sum_right += int(n[i])

for j in range(len(n)//2, len(n)):
    sum_left += int(n[j])

print('sum_right: ', sum_right)
print('sum_left: ', sum_left)

if sum_right == sum_left:
    print('LUCKY')
else:
    print('READY')