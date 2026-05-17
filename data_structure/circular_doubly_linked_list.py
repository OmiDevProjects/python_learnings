"""
Code: Circular Doubly Linked List
Description: 
    Implemented a Circular Doubly Linked List data structure in Python.

Features:
    - Insert nodes at the beginning, end, or after a specific node
    - Delete nodes by value, at the beginning or end
    - Traverse and display list elements
    - Search for elements in the list
    - Calculate the length of the linked list

Concepts Used:
    - Object-Oriented Programming (OOP)
    - Dynamic memory representation using nodes

Purpose:
    This project demonstrates the implementation and working
    of a dynamic linear data structure without using Python's
    built-in list methods.
    
"""

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, item):
        node = Node(item=item, next=self.start)
        if not self.is_empty():
            node.prev = self.start.prev
            self.start.prev.next = node
            self.start.prev = node
        else:
            node.next = node
            node.prev = node

        self.start = node
        self.count += 1

    def insert_at_last(self, item):
        node = Node(item=item)
        if not self.is_empty():
            node.prev = self.start.prev
            node.next = self.start.prev.next
            self.start.prev.next = node
            self.start.prev = node
        else:
            node.prev = node
            node.next = node
            self.start = node
        self.count += 1

    def search(self, value):
        if not self.is_empty():
            temp = self.start
            while temp.next is not self.start:
                if temp.item == value:
                    return temp
                temp = temp.next
            if temp.item == value:
                return temp
            
    def insert_after(self, value, item):
        if not self.is_empty():
            temp = self.search(value)
            if temp:
                node = Node(prev=temp, item=item, next=temp.next)
                temp.next.prev = node
                temp.next = node
                self.count += 1

    @property
    def len(self):
        return self.count
    
    def show(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not self.start:
                print(temp.item, end=', ')
                temp = temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
            self.count -= 1

    def delete_last(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start.prev.next
                self.start.prev = self.start.prev.prev
            self.count -= 1

    def delete_item(self, value):
        if not self.is_empty():
            if self.start.next == self.start:
                if self.start.item == value:
                    self.start = None
                    self.count -= 1
            else:
                temp = self.start
                if temp.item == value:
                    self.delete_first()
                else:
                    temp = temp.next
                    while temp is not self.start:
                        if temp.item == value:
                            temp.prev.next = temp.next
                            temp.next.prev = temp.prev
                            self.count -= 1
                            break

                        temp = temp.next
    

obj = CDLL()
obj.insert_at_first(34)
obj.insert_at_last(23)
obj.insert_at_last(87)

obj.insert_after(87, 12)
obj.show()
print(obj.len)

# obj.delete_first()
# obj.delete_last()
obj.delete_item(12)
obj.show()
print(obj.len)