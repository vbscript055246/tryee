class Stack():

    def __init__(self, C):

        if C < 1:
            raise ValueError('StackCapacity需大於0')
        self.array = list([0] * C)
        self.capacity = C
        self.top = -1

    def isEmpty(self):
        return self.top < 0

    def isFull(self):
        return self.top == self.capacity - 1

    def Top(self):
        if self.isEmpty():
            raise ValueError('目前Stack是空的!')
        return self.array[self.top]

    def push(self, value):

        if self.isFull():
            raise ValueError('目前Stack已滿，不可push物件!')

        self.top += 1
        self.array[self.top] = value

    def pop(self):
        if self.isFull():
            raise ValueError('目前Stack是空的，沒有物件可pop!')
        curTop = self.top
        self -= 1
        return self.array[curTop]


obj = Stack(10)
i = 0
while 1:
    try:
        obj.push(1)
        print(obj.array[i])
        i += 1
    except Exception as e:
        print(e)
        exit(0)
