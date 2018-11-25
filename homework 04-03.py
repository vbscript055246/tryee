class node:

    def __init__(self, d=None):
        self.data = d

    def printf(self):
        print(self.data)

class DWL:

    def __init__(self):
        self.LL = list()

    def displyAllNode(self):
        for i in self.LL: i.printf()

    def isEmpty(self):
        return not(len(self.LL))

    def insertAtFirstNode(self, newnode):
        self.LL.insert(0, newnode)

    def removeFirstNode(self):
        self.LL.remove(self.LL[0])


A = DWL()
A.insertAtFirstNode(node(100100))
A.insertAtFirstNode(node(100100))
A.insertAtFirstNode(node(100100))
A.insertAtFirstNode(node(100100))
A.insertAtFirstNode(node(100100))
A.insertAtFirstNode(node(100100))

A.removeFirstNode()

A.displyAllNode()