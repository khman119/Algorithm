array = input()

result = int(array[0])

for i in range(1, len(array)):
    num = int(array[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# 02984
# 567
# 12