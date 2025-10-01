class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLList:
    def __init__(self):
        # Sentinel node created at the start of the list
        self.sentinel = Node(None)


# Example usage:
mylist = SLList()
print("Sentinel node created with data:", mylist.sentinel.data)  # None
print("Sentinel next:", mylist.sentinel.next)  # None
