# 複雜度O(n)
def transpose(array):
    ans = []
    for i in range(len(array)):
        ans.append(list(range(len(array[0]))))
    for i, col in enumerate(array):
        for j, row in enumerate(col):
            ans[j][i] = row
    return ans


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(data))

