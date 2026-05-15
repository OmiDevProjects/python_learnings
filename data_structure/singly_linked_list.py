""" 
Code: Singly Linked List
Description:
    Implemented a Singly Linked List data structure in Python.

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
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, value):
        node = Node(item=value)
        if not self.is_empty():
            node.next = self.start
        self.start = node
        self.count += 1

    def insert_at_last(self, value):
        node = Node(item=value)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node
        self.count += 1

    def insert_at(self, data, value):
        node = Node(item=data)
        if not self.is_empty():
            temp = self.search_item(value)
            if temp:
                node.next = temp.next
                temp.next = node
                self.count += 1
    
    def show(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=', ')
                temp = temp.next
            print()

    def search_item(self, value):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == value:
                    return temp
                temp = temp.next

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == None:
                self.start = None
            else:
                self.start = self.start.next
            self.count -= 1

    def delete_last(self):
        if not self.is_empty():
            if self.start.next == None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
            self.count -= 1
    
    def delete_item(self, value):
        if not self.is_empty():
            if self.start.item == value:
                self.start = self.start.next
            else:
                temp = self.start
                while temp.next is not None:
                    if temp.next.item == value:
                        temp.next = temp.next.next
                        self.count -= 1
                        break
                    temp = temp.next
            
    def size(self):
        return self.count


s1 = SLL()
s1.insert_at_first(23)
s1.insert_at_last(40)
s1.insert_at_first(30)
s1.insert_at_last(46)
s1.show()
# print(s1.search_item(23).item)

print('Inserting element at')
s1.insert_at(34, 46)
s1.show()

print(s1.size())

print('Deleting First Element')
s1.delete_first()
s1.show()

# print('Deleting Last Element')
# s1.delete_last()
# s1.show()

print('Deleting Element for Linkedlist')
s1.delete_item(23)
s1.show()

print(s1.size())
