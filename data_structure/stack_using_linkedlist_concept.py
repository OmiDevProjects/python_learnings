"""
Code: Stack Implementation using linkedlist concept (Singly Linkedlist) (LIFO)

Description:
    Implemented a Stack data structure using the
    Singly Linked List concept to perform standard
    stack operations.

Features:
    - Push elements onto the stack
    - Pop elements from the stack
    - Peek the top element
    - Check stack size
    - Check whether the stack is empty

Concepts Used:
    - Object-Oriented Programming (OOP)
    - Linked List operations
    - Dynamic memory representation using nodes
    - LIFO (Last In First Out) principle

Purpose:
    This project demonstrates the implementation and working of a Stack data structure using the
    Singly Linked List concept following the LIFO principle.


| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |
| is_empty  | O(1)            |
| Size      | O(1)            |


"""

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start == None

    def push(self, item):
        node = Node(item=item, next=self.start)
        self.start = node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            popped_item = self.start.item
            if self.start.next == None:
                self.start = None
            else:
                self.start = self.start.next
            self.count -= 1
            return popped_item
        else:
            return "Stack is Empty!"

    @property
    def size(self):
        return self.count
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            return "Stack is Empty!"

s1 = Stack()
print(s1.is_empty())

s1.push(83)
# s1.push(38)
# s1.push(889)

print('Pop: ', s1.pop())
print('Peek: ', s1.peek())
print('Size: ', s1.size)