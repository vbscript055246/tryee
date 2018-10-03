def checkUpperTriangular(array):
    for i, col in enumerate(array):
        for j, row in enumerate(col):
            if i > j and array[i][j] != 0:
                return False
    return True


def two_to_one_deminsion(array):
    ans = []
    for i, col in enumerate(array):
        for j, row in enumerate(col):
            if i <= j:
                ans.append(array[i][j])
    return ans


data = [[1, 2, 3, 4, 5],
        [0, 2, 3, 4, 5],
        [0, 0, 3, 4, 5],
        [0, 0, 0, 4, 5],
        [0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0]]


print(two_to_one_deminsion(data))
