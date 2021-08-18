n, r, c = map(int, input().split())

"""
만약 n = 3이면 전체 2**3 * 2**3배열이 만들어질 것이고,
거기서 사분면을 판단하려면 2**3 // 2를 한 값과 row, col을 비교한 후
count 값은 해당 사분면에 맞게 증가시켜준다.
이후 row, col을 좌상으로 모두 바꿔줌.

"""
m = 2**(n - 1)
count = 0


def find(row, col, m, n):
    global count
    while n >= 1:
        # 좌상
        if row < m and col < m:
            count += 0
        # 우상
        elif row < m and col >= m:
            count += 2**(2*(n - 1))
            col -= m
        # 좌하
        elif row >= m and col < m:
            count += (2**(2*(n - 1)))*2
            row -= m
        # 우하
        elif row >= m and col >= m:
            count += (2**(2*(n - 1)))*3
            row -= m
            col -= m
        n -= 1
        m /= 2
    return


find(r, c, m, n)
print(count)
