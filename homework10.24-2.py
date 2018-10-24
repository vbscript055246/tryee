import copy

class Node:

    def __init__(self, n):
        self.num = n
        self.next = None


class ringlinklist:

    def __init__(self):
        self.head = None

    def displayAllNode(self):
        temp = self.head
        while temp is not None:
            print(temp.num)
            temp = temp.next


    def isEmpty(self):
        return self.head is None

    def insertAtFristNode(self, newnode):
        if self.isEmpty():
            self.head = Node(newnode.num)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(newnode.num)

    def removeLastNode(self):
        if self.isEmpty():
            raise ValueError("空的...")
        temp = self.head
        parent = None
        while temp.next is not None:
            parent = temp
            temp = temp.next
        parent.next = None
        del temp

    def concatenate(self, B):
        B = copy.deepcopy(B)
        if self.head is None:
            self.head = B.head
        elif not B.isEmpty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = B.head

    def inverse(self):
        temp = self.head
        parent = None
        next = self.head.next
        while temp.next is not None:
            temp.next, parent, temp, next = parent, temp, next, next.next
        self.head = temp
        self.head.next = parent

    def length(self):
        if self.head is None:
            raise ValueError("空的~~~")
        counter = 1
        temp = self.head
        while temp.next is not None:
            counter += 1
            temp = temp.next
        return counter


RLL = ringlinklist()
RLL1 = ringlinklist()
RLL.insertAtFristNode(Node(10))
RLL.insertAtFristNode(Node(11))
#RLL.displayAllNode()
#RLL.removeLastNode()
#RLL1.insertAtFristNode(Node(12))
#RLL.concatenate(RLL1)
#RLL.displayAllNode()
RLL.inverse()
RLL.displayAllNode()
