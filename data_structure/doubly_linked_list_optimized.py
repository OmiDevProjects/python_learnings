"""
Code: Optimized version of Doubly Linked List.
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