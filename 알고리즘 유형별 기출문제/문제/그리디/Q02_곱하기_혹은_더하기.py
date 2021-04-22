array = input()

# print(array)

result = 0


for i in range(len(array)):
    if result == 0 or int(array[i]) == 0:
        result += int(array[i])
    else:
        result *= int(array[i])

print(result)