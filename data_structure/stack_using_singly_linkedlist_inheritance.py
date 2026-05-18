"""
Code: Implementation of stack using singly linked list class.

Description:
    Implemented a Stack data structure using
    inheritance from a Singly Linked List class.

Features:
    - Push elements onto the stack
    - Pop elements from the stack
    - Peek the top element
    - Check stack size
    - Check whether the stack is empty

Concepts Used:
    - Object-Oriented Programming (OOP)
    - Inheritance
    - Linked List operations
    - LIFO (Last In First Out) principle

Purpose:
    This project demonstrates the implementation and working
    of a Stack data structure using a Singly Linked List.


| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| is_empty  | O(1)       |
| Size      | O(1)       |


"""

from singly_linked_list import SLL

class Stack(SLL):
    def is_empty(self):
        return super().is_empty()

    def push(self, item):
        self.insert_at_first(item)

    def size(self):
        return super().size()

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            return "Stack is Empty!"

    def pop(self):
        if not self.is_empty():
            popped_item = self.start.item
            self.delete_first()
            return popped_item
        else:
            return "Stack is Empty!"

s1 = Stack()
print(s1.is_empty())

s1.push(23)
s1.push(34)
s1.push(29)

print(s1.peek())

print('pop: ', s1.pop())

print(s1.peek())
print(s1.size())