array = input()

n = len(array)
num = []
start = 0
minus = False

for i in range(n):
    if array[i] == '-' or array[i] == '+':
        if start == 0:
            num.append((int(array[start:i])))
        elif minus:
            num.append(-(int(array[start:i])))
        else:
            num.append(int(array[start:i]))
        if array[i] == '-':
            minus = True
        start = i + 1
    if i == (n - 1):
        if minus:
            num.append(-(int(array[start:])))
        else:
            num.append(int(array[start:]))

print(sum(num))

# -가 한 번도 없으면 그냥 합 출력.
# -가 한 번이라도 있으면 -가 나온 이후로 나오는 모든 수는 음수