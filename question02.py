# Node class: represents a single node
class Node:
    def __init__(self, data):
        self.data = data   # value stored in the node
        self.next = None   # pointer to the next node


# SLList class: represents the linked list with a sentinel
class SLList:
    def __init__(self):
        self.sentinel = Node(None)  # sentinel node (no data)
        self.size = 0               # keeps track of length

    # insert_first method
    def insert_first(self, item):
        new_node = Node(item)             # create a new node
        new_node.next = self.sentinel.next  # link new node to old first node
        self.sentinel.next = new_node       # sentinel now points to new node
        self.size += 1                      # increase size by +1

    # helper method (just for checking contents)
    def show(self):
        p = self.sentinel.next
        while p:
            print(p.data, end=" -> ")
            p = p.next #Now go to the next node 
        print("None")
lst = SLList()
lst.insert_first(5)
lst.insert_first(10)
lst.insert_first(15)

lst.show()
print("Size:", lst.size)
