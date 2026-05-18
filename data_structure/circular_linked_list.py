"""
Code: Circular Linked List
Description: 
    Implemented a Circular Linked List data structure in Python.

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
    

| Operation       | Time Complexity |
| --------------- | --------------- |
| Insert at First | O(1)            |
| Insert at Last  | O(1)            |
| Insert After    | O(n)            |
| Search          | O(n)            |
| Delete First    | O(1)            |
| Delete Last     | O(n)            |
| Delete by Value | O(n)            |
| Traversal       | O(n)            |
| Size            | O(1)            |

"""

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, end=None):
        self.end = end
        self.count = 0

    def is_empty(self):
        return self.end == None

    def insert_at_first(self, item):
        node = Node(item=item)
        if not self.is_empty():
            node.next = self.end.next
            self.end.next = node
        else:
            node.next = node
            self.end = node
        self.count += 1

    def insert_at_last(self, item):
        node = Node(item=item)
        if not self.is_empty():
            node.next = self.end.next
            self.end.next = node
        else:
            node.next = node
        self.end = node
        self.count += 1

    def insert_after(self, value, item):
        if not self.is_empty():
            temp = self.end.next
            while True:
                if temp.item == value:
                    node = Node(item=item)
                    node.next = temp.next
                    temp.next = node

                    if self.end == temp:
                        self.end = node
                    self.count += 1
                    break

                temp = temp.next
                if temp is self.end.next:
                    break
                

    def search(self, value):
        if not self.is_empty():
            temp = self.end.next
            while temp.next is not self.end.next:
                if temp.item == value:
                    return temp
                temp = temp.next
            if temp.item == value:
                return temp

    @property
    def len(self):
        return self.count

    def show(self):
        if not self.is_empty():
            temp = self.end.next
            while temp.next is not self.end.next:
                print(temp.item, end=', ')
                temp = temp.next
            print(temp.item)
        else:
            print('Empty LinkedList!')

    def delete_first(self):
        if not self.is_empty():
            if self.end.next == self.end:
                self.end = None
            else:
                self.end.next = self.end.next.next
            self.count -= 1

    def delete_last(self):
        if not self.is_empty():
            if self.end.next == self.end:
                self.end = None
            else:
                temp = self.end.next
                while temp.next is not self.end:
                    temp = temp.next
                temp.next = temp.next.next
                self.end = temp
            self.count -= 1

    def delete_element(self, value):
        if not self.is_empty():
            if self.end.next == self.end:
                if self.end.item == value:
                    self.end = None
                    self.count -= 1
            else:
                if self.end.next.item == value:
                    self.delete_first()
                else:
                    temp = self.end.next
                    while temp.next is not self.end.next:
                        if temp.next.item == value:

                            if self.end == temp.next:
                                self.end = temp

                            temp.next = temp.next.next
                            self.count -= 1
                            break
                        temp = temp.next


obj = CLL()
obj.insert_at_first(45)
obj.insert_at_last(12)
obj.insert_after(12, 34)
obj.insert_after(12, 67)
print(obj.len)
obj.show()

# obj.delete_first()
# obj.delete_last()
# obj.delete_element(45)
# print(obj.len)
# obj.show()

# print(obj.search(12).item)