"""
Code: Deque Implementation using Optimized Doubly Linkedlist Concept.

Description:
    Implemented a Deque (Double Ended Queue) data structure
    using an Optimized Doubly Linked List Concept to perform efficient
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
    - Doubly Linked List
    - Head/Tail Pointer Optimization
    - Dynamic Memory Representation using Nodes
    - Double Ended Queue (Deque)

Purpose:
    This project demonstrates the implementation and working
    of a Deque data structure using an Optimized Doubly Linked List Concept.


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

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.count = 0

    def is_empty(self):
        return self.start == None and self.end == None

    def insert_front(self, item):
        node = Node(item=item, next=self.start)
        if not self.is_empty():
            self.start.prev = node
        else:
            self.end = node
        self.start = node
        self.count += 1

    def insert_rear(self, item):
        node = Node(prev=self.end, item=item)
        if not self.is_empty():
            self.end.next = node
        else:
            self.start = node
        self.end = node
        self.count += 1

    def delete_front(self):
        if not self.is_empty():
            if self.start.next == None:
                popped_item = self.start.item
                self.start = None
                self.end = None
            else:
                popped_item = self.start.item
                self.start = self.start.next
                self.start.prev = None
            self.count -= 1
            return popped_item
        else:
            raise IndexError('Deque is Empty!')

    def delete_rear(self):
        if not self.is_empty():
            if self.start.next == None:
                popped_item = self.end.item
                self.start = None
                self.end = None
            else:
                popped_item = self.end.item
                self.end = self.end.prev
                self.end.next = None
            self.count -= 1
            return popped_item
        else:
            raise IndexError('Deque is Empty!')

    @property
    def size(self):
        return self.count

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
    
d1 = Deque()
print('Empty: ', d1.is_empty())

d1.insert_rear(34)
d1.insert_rear(27)
d1.insert_front(389)

d1.insert_rear(88)
d1.insert_front(2334)

try:
    print('Front: ', d1.get_front())
    print('Rear: ', d1.get_rear())
except Exception as e:
    print('Exception while fetching front and rear: ', e)

try:
    # print('Popped Rear Item: ', d1.delete_rear())
    print('Popped Front Item', d1.delete_front())
except Exception as e:
    print('Exception while deleting front and rear: ', e)

print('Length: ', d1.size)

try:
    print('Front: ', d1.get_front())
    print('Rear: ', d1.get_rear())
except Exception as e:
    print('Exception while fetching front and rear: ', e)

print('Empty: ', d1.is_empty())