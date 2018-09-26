class node:

    def __init__(self, n, Obj):
        self.num = n
        self.next = Obj


n = 41
m = 3
head = node(1, None)
temp = head
for i in range(2, n + 1):
    temp.next = node(i, None)
    temp = temp.next
temp.next = head

ans = []
while head != head.next:
    temp = head
    front = None
    for i in range(m - 1):
        front = temp
        temp = temp.next
    head = temp.next
    front.next = temp.next
    ans.append(temp.num)
    del (temp)

ans.append(head.num)
for item in ans:
    print(item)
