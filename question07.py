# -----------------------------
# Node and SLList class
# -----------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLList:
    def __init__(self):
        self.sentinel = Node(None)   # dummy head
        self.size = 0

    def insert_first(self, item):
        new_node = Node(item)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node
        self.size += 1

    def insert_last(self, item):
        new_node = Node(item)
        p = self.sentinel
        while p.next is not None:
            p = p.next
        p.next = new_node
        self.size += 1

    def get_first(self):
        if self.sentinel.next is None:
            return None
        return self.sentinel.next.data

    def len(self):
        return self.size

    def to_list(self):
        result = []
        p = self.sentinel.next
        while p:
            result.append(p.data)
            p = p.next
        return result


# -----------------------------
# Testing Section
# -----------------------------

# create an empty list
lst = SLList()
assert lst.len() == 0              # initially empty
assert lst.get_first() is None     # first element should be None

# call AddFirst and test with assertions
lst.insert_first(10)
assert lst.len() == 1
assert lst.get_first() == 10

lst.insert_first(5)
assert lst.len() == 2
assert lst.get_first() == 5

# call AddLast and test with assertions
lst.insert_last(20)
assert lst.len() == 3
assert lst.to_list() == [5, 10, 20]

lst.insert_last(30)
assert lst.len() == 4
assert lst.to_list() == [5, 10, 20, 30]

# print results
print("All tests passed ✅")
print("Final List:", lst.to_list())
print("First Element:", lst.get_first())
print("Size:", lst.len())
