import copy

class Node:

    def __init__(self, n, ptr=None):
        self.num = n
        self.next = ptr


class ringlinklist:

    def __init__(self):
        self.head = None

    def displayAllNode(self):
        temp = self.head
        print(temp.num)
        while temp.next is not self.head:
            temp = temp.next
            print(temp.num)

    def isEmpty(self):
        return self.head is None

    def insertAtFristNode(self, newnode):
        if self.isEmpty():
            self.head = Node(newnode.num)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = Node(newnode.num)
            temp.next.next = self.head
            self.head = temp.next

    def removeLastNode(self):
        if self.isEmpty():
            raise ValueError("空的...")
        temp = self.head
        parent = None
        while temp.next is not self.head:
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
            while temp.next is not self.head:
                temp = temp.next
            temp.next = B.head

            temp = B.head
            while temp.next is not B.head:
                temp = temp.next
            temp.next = self.head

    def inverse(self):
        ptr = self.head
        parent = None
        next = ptr.next
        while ptr.next is not self.head:
            ptr.next, parent, ptr, next = parent, ptr, next, next.next
        self.head.next = ptr

    def length(self):
        counter = 1
        temp = self.head
        while temp.next is self.head:
            counter += 1
            temp = temp.next
        return counter

    def removeFristNode(self):
        if self.isEmpty():
            raise ValueError("空的...")
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        temp.next = self.head.next
        del self.head

    def insertAtLastNode(self, newnode):
        if self.isEmpty():
            self.head = Node(newnode.num)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = Node(newnode.num)
            temp.next.next = self.head

    def insertNode(self, ptr, newnode):
        temp = self.head
        while temp is not ptr:
            temp = temp.next
        temp.next = Node(newnode.num, temp.next)


RLL = ringlinklist()
RLL1 = ringlinklist()

RLL.insertAtFristNode(Node(10))
RLL.insertAtFristNode(Node(11))
try:
    RLL.removeLastNode()
    RLL.removeLastNode()
    RLL.removeLastNode()
    #RLL1.insertAtFristNode(Node(12))
    #RLL.concatenate(RLL1)
    RLL.displayAllNode()
except:
    pass
RLL.insertAtFristNode(Node(10))
RLL.insertAtFristNode(Node(11))

RLL.inverse()
RLL.displayAllNode()
