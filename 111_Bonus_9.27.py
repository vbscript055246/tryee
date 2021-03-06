# 最正常寫法
a1 = 0
a2 = 1
temp = -1
print(0)
print(1)
while temp < 6765:
    temp = a1 + a2
    a1 = a2
    a2 = temp
    print(temp)


# ======================================
print("\n")
# ======================================

# 有些小技巧
b = [0, 1]
print(0)
print(1)
while b[1] < 6765:
    b[0] += b[1]
    b[0] ^= b[1]
    b[1] ^= b[0]
    b[0] ^= b[1]
    print(b[1])

# ======================================
print("\n")
# ======================================

# 同學~免修囉~
# 純屬加速, DP = Dynamic Programing
DP = [0]*10000


def F(a):
    if a < 2:
        return a
    else:
        if not DP[a]:
            DP[a] = F(a-1) + F(a-2)
        return DP[a]


i = 0
while DP[i] < 6765 and DP[i]:
    print(F(i))
    i += 1
