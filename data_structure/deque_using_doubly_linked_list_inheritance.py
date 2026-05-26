"""
Code: Deque Implementation using Optimized Doubly Linkedlist.

Description:
    Implemented a Deque (Double Ended Queue) data structure
    using an Optimized Doubly Linked List to perform efficient
    insertion and deletion operations from both ends.

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
    - Inheritance
    - Doubly Linked List
    - Head/Tail Pointer Optimization
    - Double Ended Queue (Deque)

Purpose:
    This project demonstrates the implementation and working
    of a Deque data structure using an Optimized Doubly Linked List.


| Operation    | Complexity |
| ------------ | ---------- |
| Insert Front | O(1)       |
| Insert Rear  | O(1)       |
| Delete Front | O(1)       |
| Delete Rear  | O(1)       |
| Get Front    | O(1)       |
| Get Rear     | O(1)       |
| Size         | O(1)       |


"""

from doubly_linked_list_optimized import ODLL

class Deque(ODLL):
    def insert_front(self, item):
        self.insert_at_first(item)

    def insert_rear(self, item):
        self.insert_at_last(item)

    def delete_front(self):
        if not self.is_empty():
            return self.delete_first()
        else:
            raise IndexError('Deque is Empty!')

    def delete_rear(self):
        if not self.is_empty():
            return self.delete_last()
        else:
            raise IndexError('Deque is Empty!')

    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('Deque is Empty!')

    def get_rear(self):
        if not self.is_empty():
            return self.end.item
        else:
            raise IndexError('Deque is Empty!')

    @property
    def size(self):
        return super().size

d1 = Deque()
print('Empty: ', d1.is_empty())

# d1.insert_rear(34)
# d1.insert_rear(27)
# d1.insert_front(389)

# d1.insert_rear(88)
# d1.insert_front(2334)

try:
    print('Front: ', d1.get_front())
    print('Rear: ', d1.get_rear())
except Exception as e:
    print('Exception while fetching front and rear: ', e)

try:
    print('Popped Rear Item: ', d1.delete_rear())
    print('Popped Front Item', d1.delete_front())
except Exception as e:
    print('Exception while deleting front and rear: ', e)

print('Length: ', d1.size)

try:
    print('Front: ', d1.get_front())
    print('Rear: ', d1.get_rear())
except Exception as e:
    print('Exception while fetching front and rear: ', e)