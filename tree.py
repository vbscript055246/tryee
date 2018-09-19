class Tree:

    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d

    def __str__(self):
        return self.data


def getnewnode(root, data):

    if root is None:
        return Tree(data)
    else:
        parent = root
        while parent is not None:
            if parent.data >= data:
                if parent.left is None:
                    parent.left = Tree(data)
                    return root
                else:
                    parent = parent.left
            else:
                if parent.right is None:
                    parent.right = Tree(data)
                    return root
                else:
                    parent = parent.right


def outputtree(root):

    if root is not None:
        outputtree(root.left)
        print(root.data)
        outputtree(root.right)


def finddata(root, data):

    if root is None:
        return None
    else:
        parent = root
        while parent is not None:
            if parent.data == data:
                return parent
            elif parent.data > data:
                parent = parent.left
            else:
                parent = parent.right
        return None


def findfather(root, child):
    parent = root
    father = None
    while parent is not None:
        if parent == child:
            return father
        elif parent.data > child.data:
            father = parent
            parent = parent.left
        else:
            father = parent
            parent = parent.right
    return None


def findminimum(root):

    if root is None:
        return ""

    parent = root
    while parent.left is not None:
        parent = parent.left
    return parent


def findmaximum(root):

    if root is None:
        return ""
    parent = root
    while parent.right is not None:
        parent = parent.right
    return parent


def deletedata(root, data):

    temp = finddata(root, data)
    if temp is not None:
        father = findfather(root, temp)
        if temp.left is None and temp.right is None:
            if father is not None:
                if father.left.data == temp.data:
                    father.left = None
                else:
                    father.right = None
            else:
                return None
        elif temp.left is not None and temp.right is not None:
            nroot = findminimum(temp.right)

            if findfather(root, nroot).data > nroot.data:
                findfather(root, nroot).left = None
            else:
                findfather(root, nroot).right = None
            nroot.left = temp.left

            findmaximum(nroot).right = temp.right

            if father is not None:
                if father.data > nroot.data:
                    father.left = nroot
                else:
                    father.right = nroot
            else:
                return nroot
        else:
            if father is not None:
                if father.left.data == temp.data:
                    father.left = temp.left if temp.left is not None else temp.right
                else:
                    father.right = temp.left if temp.left is not None else temp.right
            else:
                return temp.left if temp.left is not None else temp.right
        del temp
        print("delete succeed~")

    else:
        print("Not found")
    return root


Root = None
while 1:

    print("(i). 插入資料")
    print("(f). 查詢資料")
    print("(d). 刪除資料")
    print("(l). 列出所有資料")
    print("(q). 退出")
    print("max 最大值, min 最小值")
    tmp = input()
    if tmp == 'i':
        Root = getnewnode(Root, input("請輸入資料:"))
    elif tmp == 'l':
        outputtree(Root)
    elif tmp == 'f':
        temp = finddata(Root, input("請輸入要查詢的資料:"))
        if temp is not None:
            print(temp)
        else:
            print("Not found")
    elif tmp == 'd':
        Root = deletedata(Root, input("請輸入要刪除的資料:"))
    elif tmp == 'min':
        print("最小值: " + str(findminimum(Root)))
    elif tmp == 'max':
        print("最大值: " + str(findmaximum(Root)))
    elif tmp == 'q':
        exit(0)
    else:
        pass