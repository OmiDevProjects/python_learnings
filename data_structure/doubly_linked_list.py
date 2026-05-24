"""
Code: Doubly Linked List
Description: 
    Implemented a Doubly Linked List data structure in Python.

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
| Insert at Last  | O(n)            |
| Insert After    | O(n)            |
| Search          | O(n)            |
| Delete First    | O(1)            |
| Delete Last     | O(n)            |
| Delete by Value | O(n)            |
| Traversal       | O(n)            |
| Size            | O(1)            |

"""

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, item):
        node = Node(item=item)
        if not self.is_empty():
            node.next = self.start
            self.start.prev = node
        self.start = node
        self.count += 1

    def insert_at_last(self, item):
        node = Node(item=item)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            node.prev = temp
            temp.next = node
        else:
            self.start = node
        self.count += 1
        
    def search(self, value):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == value:
                    return temp
                temp = temp.next

    def insert_after(self, value, item):
        if not self.is_empty():
            temp = self.search(value)
            if temp:
                node = Node(prev=temp, item=item)
                if temp.next is not None:
                    temp.next.prev = node
                node.next = temp.next
                temp.next = node
                self.count += 1

    def show_(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=', ')
                # try:
                #     print(f'item: {temp.item}, Prev: {temp.prev.item}, Next: {temp.next.item}')
                # except Exception as e:
                #     print(e)
                # print('____')
                temp = temp.next
            print()

    def show(self):
        temp = self.start

        while temp is not None:

            # prev_item = temp.prev.item if temp.prev else None
            # next_item = temp.next.item if temp.next else None

            # print(
            #     f"Item: {temp.item}, "
            #     f"Prev: {prev_item}, "
            #     f"Next: {next_item}"
            # )

            # print("____")
            print(temp.item, end=', ')
            temp = temp.next
        print()

    @property
    def size(self):
        return self.count

    def delete_first(self):
        if not self.is_empty():
            if self.start.next == None:
                self.start = None
            else:
                # self.start.next.prev = None
                self.start = self.start.next
                self.start.prev = None
            self.count -= 1

    def delete_last(self):
        if not self.is_empty():
            if self.start.next == None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                last = temp.next
                temp.next = None
                last.prev = None
            self.count -= 1

    def delete_item(self, value):
        if not self.is_empty():
            if self.start.next == None:
                if self.start.item == value:
                    self.start = None
            else:
                temp = self.start
                while temp is not None:
                    if temp.item == value:
                        if temp.prev is not None:
                            temp.prev.next = temp.next
                        else:
                            self.start = temp.next
                        if temp.next is not None:
                            temp.next.prev = temp.prev

                        self.count -= 1
                        break
                    temp = temp.next
                    

obj = DLL()
obj.insert_at_first(30)
obj.insert_at_last(23)

obj.insert_after(23, 12)
obj.insert_after(30, 89)

print('Size: ', obj.len)
obj.show()

# obj.delete_first()
obj.delete_last()
obj.delete_item(89)

print('Size: ', obj.size)
obj.show()
