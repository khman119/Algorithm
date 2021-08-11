n = int(input())
total = 0
result = []


def hanoi(count, start, temp, dest):
    global total
    if count == 0:
        return
    # n - 1 개의 기둥 temp 기둥으로 옮기기
    total += 1
    hanoi(count - 1, start, dest, temp)
    result.append((start, dest))
    # n - 1 개의 기둥 end 기둥으로 옮기기
    hanoi(count - 1, temp, start, dest)


hanoi(n, 1, 2, 3)
print(total)
for i in range(len(result)):
    print(result[i][0], result[i][1])

