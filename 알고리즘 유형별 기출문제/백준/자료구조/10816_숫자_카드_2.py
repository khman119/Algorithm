import sys
input= sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))
dic = {}
for i in array:
    dic[i] = 0
for i in x:
    if i in dic.keys():
        dic[i] += 1
for i in array:
    print(dic[i], end=' ')
