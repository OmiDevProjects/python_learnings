"""
Code: Queue Implementation using list
Description:
    Implemented a Queue data structure using Python lists
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


| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(n)            |
| Get Front | O(1)            |
| Get Rear  | O(1)            |
| Size      | O(1)            |

"""

class Queue:
    def __init__(self):
        self.queue_lst = []
        self.rear = None
        self.front = None

    def is_empty(self):
        return len(self.queue_lst) == 0

    def enqueue(self, item):
        if self.is_empty():
            self.front = item
        self.queue_lst.append(item)
        self.rear = item

    def dequeue(self):
        if not self.is_empty():
            popped_item = self.queue_lst.pop(0)

            if self.is_empty():
                self.front = None
                self.rear = None
            else:
                self.front = self.queue_lst[0]
                self.rear = self.queue_lst[-1]
            return popped_item
        else:
            raise IndexError("Queue is empty")
    
    def get_front(self):
        if not self.is_empty():
            return self.front
        else:
            raise IndexError("Queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.rear
        else:
            raise IndexError("Queue is empty")

    @property
    def size(self):
        return len(self.queue_lst)
    

q1 = Queue()
# q1.enqueue(23)
# q1.enqueue(989)
# q1.enqueue(24)
q1.enqueue(293)

print('Front: ', q1.get_front())

print('Popped item: ', q1.dequeue())

print('After Deleting...')

try:
    print('Front: ', q1.get_front())
    print('Rear: ', q1.get_rear())
except Exception as e:
    print('Exception: ', e)

print('Size: ', q1.size)