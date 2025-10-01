class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLList:
    def __init__(self):
        self.sentinel = Node(None)
        self.size = 0

    def insert_at(self, i, item):
        if i < 0 or i > self.size:   # invalid position
            print("Index out of range")
            return

        new_node = Node(item)

        p = self.sentinel
        # move p to (i-th) position before insert
        for _ in range(i):
            p = p.next

        # ab p i-th se pehle waale node pe hai
        new_node.next = p.next
        p.next = new_node
        self.size += 1

    def show(self):
        p = self.sentinel.next
        while p:
            print(p.data, end=" -> ")
            p = p.next
        print("None")
lst = SLList()
lst.insert_at(0, 10)   # 10
lst.insert_at(1, 30)   # 10 -> 30
lst.insert_at(1, 20)   # 10 -> 20 -> 30
lst.insert_at(3, 40)   # 10 -> 20 -> 30 -> 40

lst.show()
print("Size:", lst.size)
