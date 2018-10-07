string = "aabzabzabzabcz"
#         0123456789
pattern = "abzabz"
failure = [-1]*1000   # 發現錯誤時查詢字的指針應該推到哪


def get_prefix(pattern):
    j = -1
    for i in range(1, len(pattern)):     # DP建立中

        while j > -1 and pattern[i] != pattern[j+1]:  # 與字串前段"沒"重複, 減少堆移量
            j = failure[j]  # 減少至前一個字元的推移量試試看, 如果還是"沒"重複, 持續減少

        if pattern[j+1] == pattern[i]:   # 與字串前段"有"重複, 增加堆移量
            j += 1

        failure[i] = j  # 當第i個字完錯誤時,指針應該推到j


def Morris_Pratt(string, pattern):
    i = -1
    for j in range(len(string)):

        while i > -1 and pattern[i+1] != string[j]:    # 與字串前段"沒"重複, 修正堆移檢查字串指針
            i = failure[i]  # 根據字串前段的重複, 調整檢查字串指針(某些前段的檢查被省略)

        if pattern[i+1] == string[j]:   # 與字串前段"有"重複, 堆移檢查字串指針
            i += 1

        if i == len(pattern)-1:   # 找到囉, 指針已經推到檢查的最後一個字元
            print(j - i)
            i = failure[i]  # 找下一個字串出現的地方加這行
            #                 因為超過字串長了所以檢查指針會被回推
            #                 但也許是重複出現的形式, string: abcabcabc, search: abc
            #                 所以還是要回推, 不然會找不到"重疊"的(因為字數會不夠)


get_prefix(pattern)
Morris_Pratt(string, pattern)



