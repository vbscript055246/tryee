# 1
score = int(input())
if score >= 90:
    print("A")
elif 89 >= score > 60:
    print("B")
else:
    print("C")

# 2
for i in range(1, 10):
    for j in range(1, 10):
        print("{:<3d}".format(i*j), end="")
    print()


# 3
meter = 100
sum = 0
for i in range(10):
    sum += meter
    meter = meter / 2

print("共經過:" + str(sum) + "公尺")
print("高度:" + str(meter) + "公尺")

# 4
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp > 0:
        sum += (temp % 10) ** 3
        temp = temp // 10
    if sum == i:
        print(i)


# 5
counter = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j != k != i:
                counter += 1
                print(i * 100 + j * 10 + k)
print("共" + str(counter) + "個")
# 6
start = 1
for i in range(10):
    start += 1
    start *= 2
print(start)

# 7
for i in range(3):
    print(" " * (3 - i) + "*" * (i * 2 + 1))
print("*" * 7)
for i in range(2, -1, -1):
    print(" " * (3 - i) + "*" * (i * 2 + 1))


# 8
a = 2
b = 3
ans = 0
for i in range(20):
    ans += b / a
    a += b
    a, b = b, a
print(ans)

# 9
counter = 0
for i in range(2, 100):
    flag = 1
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break
    if flag:
        counter += 1
        print(i)
print("共" + str(counter) + "個")


