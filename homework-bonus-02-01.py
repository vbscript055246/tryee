class SparseMatrix:

    def __init__(self, lc, lr, c, r, v):
        self.array_col = c
        self.array_row = r
        self.value = v
        self.cols = lc
        self.rows = lr

    def __mul__(self, other):
        C = []
        R = []
        V = []

        for i in range(self.cols):
            for j in range(other.rows):
                temp = 0
                for k in range(other.cols):
                    temp += self.get_value(i, k)*other.get_value(k, j)
                C.append(i)
                R.append(j)
                V.append(temp)

        return SparseMatrix(self.cols, other.rows, C, R, V)

    def get_value(self, c, r):
        for index, col in enumerate(self.array_col):
            if col == c and self.array_row[index] == r:
                return self.value[index]
        return 0

    def __str__(self):
        temp = ""
        for i in range(self.cols):
            for j in range(self.rows):
                temp += (str(self.get_value(i, j)) + " ")
            temp += "\n"
        return temp


M = SparseMatrix(2, 2, [0]*2+[1]*2, [0, 1]*2, [1, 2, 3, 4])
M = M*M*M
N = SparseMatrix(2, 2, [0]*2+[1]*2, [0, 1]*2, [1, 3, 2, 4])
N = N*N*N
print(M)
print()
print(N)
