import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(input().rstrip())
visited = [False] * N
count = 0
for i in range(N):
    if arr[i] == 'P':
        for j in range(i - K, i + K + 1):
            if 0 <= j and j < N and arr[j] == 'H' and not visited[j]:
                count += 1
                visited[j] = True
                break

print(count)

# 8 3
# PPHHHHPP