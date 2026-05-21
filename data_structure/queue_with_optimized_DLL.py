"""
Code: Queue Implementation using Optimized Doubly Linked List

Description:
    Implemented an efficient Queue data structure using
    an optimized Doubly Linked List with head and tail pointers.

Features:
    - Enqueue elements into the queue
    - Dequeue elements from the queue
    - Access front element
    - Access rear element
    - Check queue size
    - Check whether the queue is empty

Concepts Used:
    - Object-Oriented Programming (OOP)
    - Inheritance
    - Doubly Linked List
    - Head and Tail pointer optimization
    - FIFO (First In First Out) principle

Purpose:
    This project demonstrates the implementation of an
    optimized Queue data structure with O(1) enqueue
    and dequeue operations.

Time Complexity:
    - Enqueue  : O(1)
    - Dequeue  : O(1)
    - Front    : O(1)
    - Rear     : O(1)
    - Size     : O(1)
"""

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class ODLL:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.count = 0

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, item):
        node = Node(item=item, next=self.start)
        if not self.is_empty():
            self.start.prev = node
        else:
            self.end = node
        self.start = node
        self.count += 1

    def insert_at_last(self, item):
        node = Node(item=item)
        if not self.is_empty():
            node.prev = self.end
            self.end.next = node
            self.end = node
        else:
            self.start = node
            self.end = node
        self.count += 1

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == None:
                popped_item = self.start.item
                self.start = None
                self.end = None
            else:
                # self.start.next.prev = None
                popped_item = self.start.item
                self.start = self.start.next
                self.start.prev = None
            self.count -= 1
            return popped_item

    def delete_last(self):
        if not self.is_empty():
            if self.start.next == None:
                popped_item = self.start.item
                self.start = None
                self.end = None
            else:
                popped_item = self.end.item
                self.end = self.end.prev
                self.end.next = None
            self.count -= 1
            return popped_item

    def show(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=', ')
                temp = temp.next
            print()
    
    @property
    def size(self):
        return self.count

class Queue(ODLL):
    def enqueue(self, item):
        self.insert_at_last(item)

    def dequeue(self):
        if not self.is_empty():
            return self.delete_first()
        else:
            raise IndexError('Queue is Empty')

    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('Queue is Empty')

    def get_rear(self):
        if not self.is_empty():
            return self.end.item
        else:
            raise IndexError('Queue is Empty')
        
    

if __name__ == '__main__':
    q1 = Queue()
    q1.enqueue(23)
    q1.enqueue(89)
    q1.enqueue(893)

    print('Front: ', q1.get_front())
    print('Rear: ', q1.get_rear())

    print('After Deleting...')

    print('Popped: ', q1.dequeue())
    print('Front: ', q1.get_front())
    print('Rear: ', q1.get_rear())