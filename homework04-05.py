class node:

    def __init__(self, d=None):
        self.data = d

    def printf(self):
        print(self.data)


class queue:

    def __init__(self):
        self.LL = list()

    def isEmpty(self):
        return not(len(self.LL))

    def push(self, newnode):
        self.LL.append(newnode)

    def pop(self):
        temp = self.LL[0]
        self.LL.remove(self.LL[0])
        return temp

    def front(self):
        return self.LL[0]

    def rear(self):
        return self.LL[-1]
