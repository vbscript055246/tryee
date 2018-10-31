class node:

    def __init__(self, n, ptr=None):
        self.next = ptr
        self.num = n


class stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        if self.isEmpty():
            self.head = node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node(data)

    def pop(self):
        if self.isEmpty():
            raise ValueError("空的...")
        else:
            temp = self.head
            parent = None
            while temp.next is not None:
                temp, parent = temp.next, temp
            if parent is not None:
                parent.next = None
            tmp = temp.num
            del temp
            return tmp

    def top(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.num

