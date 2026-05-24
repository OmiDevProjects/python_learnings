"""
Code: Deque Implementation using Python List

Description:
    Implemented a Deque (Double Ended Queue) data structure
    using Python lists to perform insertion and deletion
    operations from both ends.

Features:
    - Insert elements at front
    - Insert elements at rear
    - Delete elements from front
    - Delete elements from rear
    - Access front element
    - Access rear element
    - Check deque size
    - Check whether deque is empty

Concepts Used:
    - Object-Oriented Programming (OOP)
    - List operations
    - Double Ended Queue (Deque)

Purpose:
    This project demonstrates the implementation and working
    of a Deque data structure using Python's built-in list.

Time Complexity:
    - Insert Front : O(n)
    - Insert Rear  : O(1)
    - Delete Front : O(n)
    - Delete Rear  : O(1)
    - Get Front    : O(1)
    - Get Rear     : O(1)

"""

class Deque:
    def __init__(self):
        self.lst = []

    def is_empty(self):
        return len(self.lst) == 0

    @property
    def size(self):
        return len(self.lst)

    def insert_front(self, item):
        if not self.is_empty():
            self.lst.insert(0, item)
        else:
            self.lst.append(item)
    
    def insert_rear(self, item):
        self.lst.append(item)

    def get_front(self):
        if not self.is_empty():
            return self.lst[0]
        else:
            raise IndexError("Deque is empty!")

    def get_rear(self):
        if not self.is_empty():
            return self.lst[-1]
        else:
            raise IndexError("Deque is empty!")

    def delete_front(self):
        if not self.is_empty():
            return self.lst.pop(0)
        else:
            raise IndexError("Deque is empty!")

    def delete_rear(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            raise IndexError("Deque is empty!")

d1 = Deque()

print('Empty: ', d1.is_empty())
print('Size: ', d1.size)

d1.insert_rear(34)
d1.insert_front(35)

print('After Insertion...')

print('Empty: ', d1.is_empty())
print('Size: ', d1.size)

d1.insert_rear(89)
d1.insert_front(235)

# d1.delete_front()
d1.delete_rear()

try:
    print('Front: ', d1.get_front())
    print('Rear: ', d1.get_rear())
except Exception as e:
    print('Exception while getting front and rear: ', e)

print('Size: ', d1.size)