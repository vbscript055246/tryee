# 純屬加速, DP = Dynamic Programing
DP = [0]*10000


def F(a):
    if a < 2:
        return a
    else:
        if not DP[a]:
            DP[a] = F(a-1) + F(a-2)
        return DP[a]


print(F(998))


def f(n):
    if n == 0 or n == 1:
        return n
    a1 = 0
    a2 = 1
    temp = -1
    for i in range(n-1):
        temp = a1 + a2
        a1 = a2
        a2 = temp
    return temp


print(f(100000))
