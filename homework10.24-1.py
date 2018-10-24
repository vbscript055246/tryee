class ringqueue:

    def __init__(self, c):
        self.queue = [0]*(c+1)
        self.front = 0
        self.rear = 0
        self.capacity = c+1

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return ((self.rear + 1) % self.capacity) == self.front

    def get_front(self):
        return self.queue[(self.front+1) % self.capacity]

    def get_rear(self):
        return self.queue[self.rear]

    def push(self, num):
        if self.isFull():
            raise ValueError("目前Queue是滿的!")
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = num

    def pop(self):
        if self.isEmpty():
            raise ValueError("目前Queue是空的!")
        else:
            ans = self.get_front()
            self.queue[(self.front+1) % self.capacity] = 0
            self.front = (self.front+1) % self.capacity
            return ans


que = ringqueue(3)
while 1:
    c = input('輸入指令')
    try:
        if c == 'i':
            que.push(int(input('輸入數字!!!')))
        elif c == 's':
            print(que.queue)
        elif c == 'p':
            print(que.pop())
    except Exception as e:
        print(e)

