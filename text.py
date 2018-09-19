import random


# 1.===========================================
class Animal:

    def move(self):
        return "動"


class Cat(Animal):

    def move(self):
        return "跳"


class Tiger(Cat):

    def move(self):
        return"跑"

    def skill(self):
        return "獵殺"


cat = Cat()
print(cat.move())


cat2 = Tiger()  # 這裡還在研究......父類別的型態表現不出來
print(cat2.move())
print(cat2.skill())

# 2.===========================================


class Demo:

    def __init__(self):
        self.__divider = 1

    def getDivider(self):
        return self.__divider

    def setDivider(self, divider):
        if divider == 0:
            print("Divider can not be 0 !")
        else:
            self.__divider = divider

    def dataHidingDemo(self, number):
        result = number/self.__divider
        print(result)

    @staticmethod
    def main(args=None):
        demo = Demo()
        demo.setDivider(0)
        demo.dataHidingDemo(50)


D = Demo()
D.main()

# 3.===========================================


def SelectionSort(array):
    data = array[0]
    for i in range(len(data)):
        temp = min(data[0:len(data) - i])
        data.remove(temp)
        data.append(temp)
    array[0] = data


data = []

for i in range(25):
    data.append(random.randint(0, 1000))

array = [data]
SelectionSort(array)

for item in data:
    print(item)

# 4.===========================================

# 這邊應該是這樣~
# (n^2)*log(n) + log(n) = O((n^2)*log(n))
# 8*log(log(n)) = O(log(log(n)))
# log(n^2) = O(log(n))
# n/100+10000/(n^2) = O(n)
# log(n!) = O(log(n))

# 5.===========================================


def binarySearch(array, search):
    mid = int(len(array)/2)
    if len(array) == 1 and search != array[0]:
        print("Not found!!!")
        return
    if search == array[mid]:
        print("found!!!")
    else:
        if array[mid] > search:
            binarySearch(array[:mid], search)
        else:
            binarySearch(array[mid:], search)


search = data[random.randint(0, len(data)-1)]

binarySearch(data, search)
