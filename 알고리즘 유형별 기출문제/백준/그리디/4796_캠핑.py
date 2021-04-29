count = 0
while True:
    count += 1
    # 차례대로 L, P, V
    array = list(map(int, input().split()))
    if array[0] == 0 and array[1] == 0 and array[2] == 0:
        break
    l = array[0]
    p = array[1]
    v = array[2]
    # day = days(l, p, v)
    day = l * (v // p) + min((v % p), l)
    print('Case ' + str(count) + ': ' + str(day))

# def days(l, p, v):
#     day = l * (v // p) + min((v % p), l)
#     return day


