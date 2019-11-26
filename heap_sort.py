import random
random.seed()
array = [ i for i in range(10)]

for i in range(len(array)):
    rnd_int = random.randint(0, len(array)-i-1)
    array[rnd_int], array[len(array)-i-1] = array[len(array)-i-1], array[rnd_int]
#要排序的
print(array)

heap = [-1] * (len(array)+1)
#                  1
#            2           3
#         4    5      6     7
#        8 9 10 11  12 13 14 15

for ind, num in enumerate(array, 1):
    index = ind

    heap[index] = num
    while index//2 > 0:
        if heap[index//2] < heap[index]:
            heap[index// 2], heap[index] = heap[index], heap[index // 2]
            index = index// 2
        else:
            break
#最大堆
print(heap[1:])

ans = []
for i in range(1, 11):
    ans.append(heap[1])
    ptr = 1
    while ptr * 2 + 1 < len(heap) and \
            (heap[ptr * 2] if heap[ptr * 2] > heap[ptr * 2 + 1] else heap[ptr * 2 + 1]) > heap[-1]:

        if heap[ptr * 2] > heap[ptr * 2 + 1]:
            heap[ptr], ptr = heap[ptr * 2], ptr * 2
        else:
            heap[ptr], ptr = heap[ptr * 2 + 1], ptr * 2 + 1
    if ptr * 2 < len(heap):
        heap[ptr], heap[ptr * 2] = max(heap[-1], heap[ptr * 2]), min(heap[-1],heap[ptr * 2])
    else:
        heap[ptr] = heap[-1]
    del heap[-1]
# 排序完成
print(ans)
