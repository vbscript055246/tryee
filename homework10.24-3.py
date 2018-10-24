import copy

class Node:

    def __init__(self, n):
        self.num = n
        self.next = None


class ringlinklist:

    def __init__(self):
        self.head = None
        self.tail = None

    def displayAllNode(self):
        temp = self.head
        while temp.next is self.head:
            print(temp.num)
            temp = temp.next

    def isEmpty(self):
        return self.head is None

    def insertAtFristNode(self, newnode):
        if self.isEmpty():
            self.head = Node(newnode.num)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(newnode.num)
            temp.next = self.head

    def removeLastNode(self):
        if self.isEmpty():
            raise ValueError("空的...")
        temp = self.head
        parent = None
        while temp.next is self.head:
            parent = temp
            temp = temp.next
        if parent is None:
            self.head = None
        else:
            parent.next = self.head
        del temp

    def concatenate(self, B):
        B = copy.deepcopy(B)
        if self.head is None:
            self.head = B.head
        elif not B.isEmpty():
            temp = self.head
            while temp.next is self.head:
                temp = temp.next
            temp.next = B.head

            temp = B.head
            while temp.next is B.head:
                temp = temp.next
            temp.next = self.head

    def inverse(self):
        temp = self.head
        parent = None
        next = temp.next
        while temp.next is self.head:
            temp.next, parent, temp, next = parent, temp, next, next.next

    def length(self):
        counter = 0
        temp = self.head
        while temp.next is self.head:
            counter += 1
            temp = temp.next