"""
Code: Optimized version of optimized Doubly Linked List concept
"""

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Queue:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.count = 0

    def is_empty(self):
        return self.start == None and self.end == None

    def enqueue(self, item):
        node = Node(item=item)
        if not self.is_empty():
            self.end.next = node
            self.end = node
        else:
            self.start = node
            self.end = node
        self.count += 1

    def dequeue(self):
        popped_item = None
        if not self.is_empty():
            popped_item = self.start.item
            if self.start.next == None:
                self.start = None
                self.end = None
            else:
                self.start = self.start.next
                self.start.prev = None
            return popped_item
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

    @property
    def size(self):
        return self.count


obj = Queue()
print('Empty: ', obj.is_empty())

obj.enqueue(43)
obj.enqueue(786)

print('Front: ', obj.get_front())
print('Rear: ', obj.get_rear())

print('Removing...')


try:
    print('Popped item: ', obj.dequeue())
    print('Front: ', obj.get_front())
    print('Rear: ', obj.get_rear())
except Exception as e:
    print('Exception: ', e)
