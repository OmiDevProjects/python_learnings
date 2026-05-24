"""
Code: Deque Implementation using Python List Inheritance.

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


| Operation    | Complexity |
| ------------ | ---------- |
| Insert Front | O(n)       |
| Insert Rear  | O(1)       |
| Delete Front | O(n)       |
| Delete Rear  | O(1)       |
| Get Front    | O(1)       |
| Get Rear     | O(1)       |
| Size         | O(1)       |


"""

class Deque(list):
    def is_empty(self):
        return len(self) == 0

    def insert_at_front(self, item):
        self.insert(0, item)

    def insert_at_rear(self, item):
        self.append(item)
    
    def delete_at_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        return self.pop(0)
    
    def delete_at_last(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        return self.pop()

    @property
    def size(self):
        return len(self)

    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        return self[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        return self[-1]

    def remove(self, value):
        raise AttributeError("Invalid Deque Operation")


d1 = Deque()
print('Empty: ', d1.is_empty())

# d1.insert_at_rear(34)
# d1.insert_at_front(389)

# d1.insert_at_rear(88)
# d1.insert_at_front(2334)

try:
    print('Front: ', d1.get_front())
    print('Rear: ', d1.get_rear())
except Exception as e:
    print('Exception while fetching front and rear: ', e)

try:
    print('Popped Rear Item: ', d1.delete_at_last())
    print('Popped Front Item', d1.delete_at_front())
except Exception as e:
    print('Exception while deleting front and rear: ', e)

print('Length: ', d1.size)

try:
    print('Front: ', d1.get_front())
    print('Rear: ', d1.get_rear())
except Exception as e:
    print('Exception while fetching front and rear: ', e)