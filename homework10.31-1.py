import copy

class Node:

    def __init__(self, n, ptr=None, fptr=None):
        self.num = n
        self.next = ptr
        self.front = fptr


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
            self.head = Node(newnode.num, self.head, self.head)
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = Node(newnode.num, self.head, temp)
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
            self.head.front = parent
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
            B.head.front = temp

            temp = B.head
            while temp.next is not B.head:
                temp = temp.next
            temp.next = self.head
            self.head.front = temp

    def inverse(self):
        ptr = self.head
        while ptr.next is not self.head:
            ptr.next, ptr.front, ptr = ptr.front, ptr.next, ptr.next

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
        self.head.next.front = temp
        del self.head

    def insertAtLastNode(self, newnode):
        if self.isEmpty():
            self.head = Node(newnode.num)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = Node(newnode.num, self.head, temp)
            self.head.front = temp.next

    def insertNode(self, ptr, newnode):
        temp = self.head
        while temp is not ptr:
            temp = temp.next
        tmp = temp.next.next
        temp.next = Node(newnode.num, temp.next, temp)
        tmp.front = temp.next