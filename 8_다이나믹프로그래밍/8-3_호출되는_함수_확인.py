array = [0] * 100

def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if array[x] != 0:
        return array[x]
    array[x] = fibo(x-1) + fibo(x-2)
    return array[x]

fibo(10)