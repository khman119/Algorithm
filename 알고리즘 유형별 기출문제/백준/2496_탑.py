import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = []
result = []
for i in range(n):
    while stack:
        if stack[-1][0] > arr[i]:  # 스택의 값이 arr의 값보다 더 크다면 해당 스택의 인덱스값 추가.
            result.append(stack[-1][1])
            break
        else:
            stack.pop()
    if len(stack) == 0: #스택이 비어있으면 값 넣기
        result.append(0)
    stack.append((arr[i], i + 1))
    print(stack)

for i in result:
    print(i, end=' ')