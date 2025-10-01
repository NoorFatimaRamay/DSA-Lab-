class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SLList:
    def __init__(self):
        self.sentinel = Node(None)   # sentinel node
        self.size = 0

    def insert_first(self, item):
        new_node = Node(item)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        self.size += 1

    def get_first(self):
        if self.sentinel.next is None:   # agar list khali hai
            return None
        return self.sentinel.next.item   # pehle node ka item return karo
lst = SLList()
print(lst.get_first())   # None (kyunki list empty hai)

lst.insert_first(10)
print(lst.get_first())   # 10

lst.insert_first(20)
print(lst.get_first())   # 20 (ab 20 pehla node hai)
