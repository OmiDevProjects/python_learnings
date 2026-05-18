"""
Code: Implementation of stack using singly linked list class.

Description:
    Implemented a Stack data structure using a
    Singly Linked List to perform standard stack operations.

Features:
    - Push elements onto the stack
    - Pop elements from the stack
    - Peek the top element
    - Check stack size
    - Check whether the stack is empty

Concepts Used:
    - Object-Oriented Programming (OOP)
    - Linked List operations
    - Composition
    - LIFO (Last In First Out) principle

Purpose:
    This project demonstrates the implementation and working
    of a Stack data structure using a Singly Linked List.


| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |
| is_empty  | O(1)            |
| Size      | O(1)            |


"""

from singly_linked_list import SLL

class Stack:
    def __init__(self):
        self.lst = SLL()

    def push(self, item):
        self.lst.insert_at_first(item)
    
    def pop(self):
        if not self.is_empty():
            return self.lst.delete_first()
        else:
            return "Stack is Empty!"

    def peek(self):
        if not self.is_empty():
            return self.lst.start.item
        else:
            return "Stack is Empty!"
    
    def size(self):
        return self.lst.size()

    def is_empty(self):
        return self.lst.is_empty()

s1 = Stack()
print('Empty: ', s1.is_empty())

# print('Inserting elements...')
# s1.push(35)
# s1.push(89)
# s1.push(123)

print('Empty: ', s1.is_empty())

print('Peeking: ', s1.peek())

print('Pop item: ', s1.pop())


print('Peeking: ', s1.peek())

print('Size: ', s1.size())