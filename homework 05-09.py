import random

class Mheap():

    def __init__(self, c):
        self.heap = [-1]
        self.capacity = c

    def isFull(self):
        return len(self.heap)-1 < self.capacity

    def isEmpty(self):
        return len(self.heap) == 1

    def push(self, data):
        ptr = len(self.heap)
        self.heap.append(0)
        while ptr > 1 and self.heap[ptr//2] < data:
            self.heap[ptr] = self.heap[ptr // 2]
            ptr = ptr // 2
        self.heap[ptr] = data

    def pop(self):
        ptr = 1
        ans = self.heap[1]

        while ptr*2+1 < len(self.heap) and (self.heap[ptr*2], ptr*2 if self.heap[ptr*2] > self.heap[ptr*2+1] else self.heap[ptr*2+1], ptr*2+1)[0] > self.heap[-1]:
            if self.heap[ptr*2] > self.heap[ptr*2+1]:
                self.heap[ptr], ptr = self.heap[ptr * 2], ptr*2
            else:
                self.heap[ptr], ptr = self.heap[ptr*2+1], ptr*2+1
        if ptr*2 < len(self.heap):
            self.heap[ptr], self.heap[ptr*2] = max(self.heap[-1], self.heap[ptr*2]), min(self.heap[-1], self.heap[ptr*2])
        del self.heap[-1]
        return ans

    def __str__(self):
        return str(self.heap)



H = Mheap(1000)
for i in range(10):
    H.push(random.randint(0,1000))

print(H)
H.pop()
print(H)
