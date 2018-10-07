def collatz(x):
    if x <= 0: print("no");return
    while x != 1:x = (3 * x + 1) if (x & 1) else x // 2;print(x)


collatz(int(input("請輸入:\n")))


# ======想覺得有趣的話看看你家電腦可以算到多少XD~

#i = 1
#try:
#    while 1:
#        a = i
#       while a != 1: a = (3 * a + 1) if (a & 1) else a // 2
#        i += 1
#        print(i)
#except:
#    print(i)

