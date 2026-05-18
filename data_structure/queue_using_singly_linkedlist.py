"""
Code: Code: Queue Implementation using Singly Linked List (FIFO)
Description:
    Implemented a Queue data structure using a
    Singly Linked List to perform standard queue operations.

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
    of a Queue data structure using Singly Linkedlist.
    
"""

from singly_linked_list import SLL

class Queue:
    def __init__(self):
        self.queue_lst = SLL()
        self.rear = None
        self.front = None

    def is_empty(self):
        return self.queue_lst.is_empty()

    def enqueue(self, item):
        if self.is_empty():
            self.front = item
        self.queue_lst.insert_at_last(item)
        self.rear = item

    def dequeue(self):
        if not self.is_empty():
            poppped_item = self.queue_lst.start.item
            self.queue_lst.delete_first()

            if self.is_empty():
                self.front = None
                self.rear = None
            else:
                self.front = self.queue_lst.start.item

            return poppped_item
        else:
            raise IndexError('Queue is Empty!')

    def get_front(self):
        if not self.is_empty():
            return self.front
        else:
            raise IndexError('Queue is Empty')

    def get_rear(self):
        if not self.is_empty():
            return self.rear
        else:
            raise IndexError('Queue is Empty')
        
    @property
    def size(self):
        return self.queue_lst.size()


q1 = Queue()
print('Empty: ', q1.is_empty())

q1.enqueue(12)
q1.enqueue(28)
q1.enqueue(83)
q1.enqueue(82)

try:
    print('Front: ', q1.get_front())
    print('Popped: ', q1.dequeue())

    print('-'*20)

    print('Front: ', q1.get_front())
    print('Rear: ', q1.get_rear())

    print('Size: ', q1.size)
except Exception as e:
    print('Exception: ', e)

