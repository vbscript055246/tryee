def checkUpperTriangular(array):
    for i, col in enumerate(array):
        for j, row in enumerate(col):
            if i > j and array[i][j] != 0:
                return False
    return True


data = [[1, 2, 3, 4, 5],
        [0, 2, 3, 4, 5],
        [0, 0, 3, 4, 5],
        [0, 0, 0, 4, 5],
        [0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0]]
print(checkUpperTriangular(data))
