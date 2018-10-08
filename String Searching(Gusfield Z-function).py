string = "aabzabzabzabcz"
pattern = "abzabz"
Z = []


def get_Z(string):
    global Z
    l = 0
    r = 0
    z = [0] * len(string)
    z[0] = len(string)
    for i in range(1, z[0]):
        z[i] = min([r-i+1, z[z[l]-(r-i+1)]]) if r > i else 0

        while (i+z[i]) < z[0] and string[z[i]] == string[i+z[i]]:
            z[i] += 1

        if (i + z[i] - 1) > r:
            r = i + z[i] - 1
            l = i
    Z = z


if pattern != "":
    get_Z(pattern + "_" + string)
    print(Z)
    print(Z.index(len(pattern)))
else:
    print(-1)
