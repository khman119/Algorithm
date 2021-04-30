array = input()

count_zero_to_one = 0
count_one_to_zero = 0

# start = int(array[0])
#
# if start == 0:
#     count_zero += 1
# else:
#     count_one += 1

for i in range(1, len(array)):
    num_i_1 = int(array[i-1])
    num_i = int(array[i])
    if num_i_1 != num_i and num_i_1 == 0:
        count_zero_to_one += 1
    elif num_i_1 != num_i and num_i_1 == 1:
        count_one_to_zero += 1

# if count_zero_to_one == count_one_to_zero:
#     print(count_zero_to_one)
# else:
print(max(count_zero_to_one, count_one_to_zero))