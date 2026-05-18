"""
Code: Queue Implementation using list inheritance
Description:
    Implemented a Queue data structure using Python list inheritance
    to perform standard queue operations.

Features:
    - Enqueue elements into the queue
    - Dequeue elements from the queue
    - Access front element
    - Access rear element
    - Check queue size
    - Check whether the queue is empty

Concepts Used:
    - Object-Oriented Programming (OOP)
    - List operations
    - FIFO (First In First Out) principle

Purpose:
    This project demonstrates the implementation and working
    of a Queue data structure using Python's built-in list.

Note:
    Since Python lists are dynamic arrays, dequeue operation
    using pop(0) requires shifting elements and takes O(n) time.
    

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(n)            |
| Get Front | O(1)            |
| Get Rear  | O(1)            |
| Size      | O(1)            |


"""

from collections import deque

class Queue(list):
    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError('Queueu is Empty')

    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError('Queueu is Empty')

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Queueu is Empty')

    @property
    def size(self):
        return len(self)

    def insert(self, index, value):
        raise AttributeError('Invalid Operation on queue!')

    def remove(self, item):
        raise AttributeError('Invalid Operation on queue!')
    

q1 = Queue()
q1.enqueue(23)
q1.enqueue(34)

print('Front: ', q1.get_front())

q1.enqueue(50)

print('Pop: ', q1.dequeue())
print('Front: ', q1.get_front())
print('Rear: ', q1.get_rear())

print('Size: ', q1.size)