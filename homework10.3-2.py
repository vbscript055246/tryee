class SparseMatrixItem:

    def __init__(self, c, r, v):
        self.value = v
        self.col = c
        self.row = r

    def __int__(self):
        return self.value


class SparseMatrix:

    def __init__(self, length, Item):
        self.length = length
        self.Item = Item
        # self.Item.sort(key=attrgetter('col'))  # , reverse=True
        for index, i in enumerate(self.Item):
            print("index:" + str(index) + ", " + "{:2d}".format(int(i)))

    def get_value(self, c, r):
        for item in self.Item:
            if item.col == c and item.row == r:
                return item.value
        return 0

    def __str__(self):
        temp = ""
        for i in range(self.length):
            for j in range(self.length):
                temp += "{:2d} ".format(self.get_value(i, j))
            temp += "\n"
        return temp


def fastTranspose(array):
    temp = []
    for i in range(len(array[0])):
        temp.append(list())

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]:
                temp[j].append(SparseMatrixItem(j, i, array[i][j]))

    ans = []
    for item in temp:
        ans += item
    return SparseMatrix(len(array), ans)


data = [[0, 0, 0, 3, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -3, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 2, 0]]

print(fastTranspose(data))
