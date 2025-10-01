question07.py
# import the SLList class
from sllist import SLList   # assuming your main class file is sllist.py

# create an empty list
lst = SLList()
assert lst.len() == 0      # list should be empty initially
assert lst.get_first() is None

# call AddFirst (insert_first) and test with assertions
lst.insert_first(10)
assert lst.len() == 1
assert lst.get_first() == 10

lst.insert_first(5)
assert lst.len() == 2
assert lst.get_first() == 5   # because 5 is inserted at the front

# call AddLast (insert_last) and test with assertions
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
