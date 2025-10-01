class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLList:
    def __init__(self):
        self.sentinel = Node(None)
        self.size = 0

    def insert_first(self, item):
        new_node = Node(item)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        self.size += 1

    def insert_last(self, item):
        new_node = Node(item)

        # start from sentinel
        p = self.sentinel
        while p.next is not None:   # jab tak end na aa jaye
            p = p.next

        # ab p last node hai
        p.next = new_node
        self.size += 1

    def show(self):
        p = self.sentinel.next
        while p:
            print(p.data, end=" -> ")
            p = p.next
        print("None")
lst = SLList()
lst.insert_first(10)
lst.insert_last(20)
lst.insert_last(30)

lst.show()
print("Size:", lst.size)
