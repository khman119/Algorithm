import sys
n = int(input())
arr = list(sys.stdin.readline().rstrip())
count = 1
for i in arr:
    if i == 'S':
        count += 1
    elif i == 'L':
        count += 0.5

print(min(int(count), len(arr)))
#
# 4
# LLSS
#
# 5
# SLLSS
#
#
#

