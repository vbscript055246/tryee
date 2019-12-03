#1.
bucket = [""] * 26
insert_list = ["GA", "D", "G", "L", "A", "A2", "A1", "A3", "A4", "Z", "ZA", "E"]

for element in insert_list:
    index = ord(element[0]) - 65
    while bucket[index] != "":
        index = (index+1) % 26
    bucket[index] = element

print(bucket)

#2.
def find_bucket(val):
    global bucket
    start = ord(val[0]) - 65
    for i in range(len(bucket)-1):
        if bucket[(start+i) % 26] == val:
            return (start+i) % 26
    return -1

print(find_bucket("A8"))
print(find_bucket("D") , end='\n\n')

#3.
LinkListBucket = [list() for i in range(26)]
for element in insert_list:
    index = ord(element[0]) - 65
    LinkListBucket[index].append(element)

print(LinkListBucket)

#4.
def find_LinkListBucket(val):
    global LinkListBucket
    for element in LinkListBucket[ord(val[0]) - 65]:
        if element == val:
            return ord(val[0]) - 65
    return -1

print(find_bucket("LOL"))
print(find_bucket("A3") , end='\n\n')


#5.      0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
array = [1,1,2,2,3,3,4,5,5,5, 6, 6, 6, 6, 7, 8, 8, 9, 9, 9]

def findValue(val):
    return BinarySearch(val, 0, len(array)-1)

def BinarySearch(val, left, right):
    global array
    if left == right:
        return -1, -1
    if array[(right+left) // 2] == val:
        start_index, end_index = check_side((right+left) // 2, val)
        start_index, end_index = min(end_index, start_index), max(end_index, start_index)
        return start_index, end_index
    else:
        if array[(right + left) // 2] < val :
            return BinarySearch(val, (right + left) // 2 + 1, right)
        else:
            return BinarySearch(val, left, (right + left) // 2 - 1)
    return -1, -1

def check_side(index, val):
    return index + side_extend(val, index, -1), index + side_extend(val, index, 1)

def side_extend(val, ind, way):
    global array
    return side_extend(val, (ind + way), way) + way if (0 <= (ind + way) < len(array)) and array[(ind + way)] == val else 0


for i in range(0, 11):
    print(findValue(i))
